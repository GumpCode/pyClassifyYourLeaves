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

from datasets.dataset_split import XmlReader4Clef
from datasets.dataset_split import ExcelReader4Clef

def tripleSplit(record_list):
    point = int(len(record_list)/3)
    list = []
    list.append(record_list[0:point-1])
    list.append(record_list[point-1:2*point-1])
    list.append(record_list[2*point-1: len(record_list)-1])

    return list


if __name__ == '__main__':
    data_dir = 'data/CLEF_data/FourniApresCLEF2012/data/train'
    excel_file = 'data/CLEF_data/perClassNum.xls'
    splited_data_dir = 'splited_data'
    xml_list = glob.glob('{}/*.xml'.format(data_dir))
    #saved_format: {name: [[scan], [pseudoscan], [photograph]]}
    #init state
    record = {}
    excel = ExcelReader4Clef(excel_file)
    for name in excel.names:
        print name
        record[name] = [[], [], []]

    for xml in xml_list:
        obj = XmlReader4Clef(xml)
        if obj.classId in record.keys():
            if obj.leaftype == 'Scan':
                record[obj.classId][0].append(obj.filename)
            elif obj.leaftype == 'pseudoscan':
                record[obj.classId][1].append(obj.filename)
            if obj.leaftype == 'photograph':
                record[obj.classId][2].append(obj.filename)

    data_dir
    for

    #print len(record['Arbutus unedo'][1])
    #print len(record['Arbutus unedo'][2])
