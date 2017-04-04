#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Gump from CQU
# * Email         : gumpglh@qq.com
# * Create time   : 2017-04-03 15:04
# * Last modified : 2017-04-03 15:04
# * Filename      : dataset_split.py
# * Description   :
# * Copyright © gumpglh. All rights reserved.
# **********************************************************

import os
import sys
import glob
import shutil
import random
import cv2
import numpy as np
import tensorflow as tf

#from datasets.dataset_split import XmlReader4Clef
#from datasets.dataset_split import ExcelReader4Clef
from dataset_split import XmlReader4Clef
from dataset_split import ExcelReader4Clef


tf.app.flags.DEFINE_string('data_dir', 'data/CLEF_data/FourniApresCLEF2012/data/train',
                           'data_dir')
tf.app.flags.DEFINE_string('excel_file', 'data/CLEF_data/perClassNum.xls',
                           'excel file')
tf.app.flags.DEFINE_string('splited_data_dir', 'splited_data',
                           'splited data_dir')
tf.app.flags.DEFINE_string('resize_type', 'resize',
                           'splited data_dir')

FLAGS = tf.app.flags.FLAGS

def computeMean(im):
    b_mean = 0
    g_mean = 0
    r_mean = 0
    for (b,g,r) in im:
        b_mean += b
        g_mean += g
        r_mean += r
    b_mean /= len(im[:,:,0])
    g_mean /= len(im[:,:,0])
    r_mean /= len(im[:,:,0])
    return [r_mean, g_mean, b_mean]


def addPad(img, width, height):
    mean = computeMean(img)
    b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
    g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
    r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
    width_break_point = int((width - img.shape[0])/2)
    height_break_point = int((height - img.shape[1])/2)
    new_img = [b,g,r]
    for channel in range(img.shape[2]):
        for i in new_img[:,:,channel]:
            i = mean[channel]
    for channel in range(img.shape[2]):
        new_img[width_break_point:width_break_point+img.shape[1]+1,
            height_break_point:height_break_point+img.shape[1]+1,
            channel] = img[:,:,channel]

    return new_img

def doubleSplit(record_list):
    point = int(len(record_list)/10*3)
    random.shuffle(record_list)
    list = []
    list.append(record_list[0:point+1])
    list.append(record_list[point+1: len(record_list)])

    return list

def copyImg(list, dir, classnum, tp, shape):
    width = shape[0]
    height = shape[1]
    for im in list:
        src = '{}/{}'.format(data_dir, im)
        dst = '{}/{}/{}/{}'.format(splited_data_dir, dir, str(classnum), im)
        if tp == 'resize':
            im = cv2.imread(src)
            re_img = cv2.resize(im, (width, height))
            cv2.imwrite(dst, re_img)
        elif tp == 'padding':
            im = cv2.imread(src)
            new_img = addPad(img, width, height)
            cv2.imwrite(dst, re_img)

if __name__ == '__main__':
    data_dir = FLAGS.data_dir
    excel_file = FLAGS.excel_file
    splited_data_dir = FLAGS.splited_data_dir
    tp=FLAGS.resize_type
    width = 256
    height = 256
    shape = [width, height]
    dirsets = ['test', 'train']
    xml_list = glob.glob('{}/*.xml'.format(data_dir))
    class2num_file = 'class2num.txt'
    #init state
    record = {}
    excel = ExcelReader4Clef(excel_file, threshold=40)
    for name in excel.names:
        record[name] = [[], [], []]

    #record_format: {name: [[scan], [pseudoscan], [photograph]]}
    num = 0
    for xml in xml_list:
        obj = XmlReader4Clef(xml)
        if obj.classId in record.keys():
            if obj.leaftype == 'Scan':
                record[obj.classId][0].append(obj.filename)
            elif obj.leaftype == 'pseudoscan':
                record[obj.classId][1].append(obj.filename)
            elif obj.leaftype == 'photograph':
                record[obj.classId][2].append(obj.filename)
            num += 1
    print num

    i = 0
    with open(class2num_file, 'w') as f:
        for key in record.keys():
            f.write(key + ' ' + str(i))
            i += 1

    #make dir for splited data
    for dir in dirsets:
        for num in range(len(record.keys())):
            if not os.path.exists(splited_data_dir):
                os.mkdir(splited_data_dir)
            part_dir_path = '{}/{}'.format(splited_data_dir, dir)
            if not os.path.exists(part_dir_path):
                os.mkdir(part_dir_path)
            dir_path = '{}/{}'.format(part_dir_path, str(num))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

    j = 0
    for key in record.keys():
        for l in record[key]:
            if len(l) >= 2:
                splited_result = doubleSplit(l)
                copyImg(splited_result[0], dirsets[0], j, tp, shape)
                copyImg(splited_result[1], dirsets[1], j, tp, shape)
            else:
                n = random.randint(0,1)
                copyImg(l, dirsets[n], j, tp, shape)
        j += 1
