#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Gump from CQU
# * Email         : gumpglh@qq.com
# * Create time   : 2017-03-15 18:53
# * Last modified : 2017-04-03 15:03
# * Filename      : dataset_split.py
# * Description   :
# * Copyright © 2016. All rights reserved.
# **********************************************************

import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from lxml import etree
import xlrd


class XmlReader4Clef:

    def __init__(self, filepath):
        # shapes type:
        # [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color]
        self.filepath = filepath
        self.parseXML()

    def parseXML(self):
        assert self.filepath.endswith('.xml'), "Unsupport file format"
        parser = etree.XMLParser(encoding='utf-8')
        xmltree = ElementTree.parse(self.filepath, parser=parser).getroot()
        self.filename = xmltree.find('FileName').text
        self.leaftype = xmltree.find('Type').text
        self.classId = xmltree.find('ClassId').text

        return True

class ExcelReader4Clef:

    def __init__(self, filepath):
        self.filepath = filepath
        self.parseEXCEL()

    def parseEXCEL(self):
        assert self.filepath.endswith('.xls'), "Unsupport file format"
        data = xlrd.open_workbook(self.filepath)
        table = data.sheets()[0]
        nrows = table.nrows
        self.names = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            count = int(row[1]) + int(row[4]) + int(row[7])
            if count > 40:
                self.names.append(row[0])
