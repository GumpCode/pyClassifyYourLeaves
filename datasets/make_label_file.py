#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : Gump from CQU
# * Email         : gumpglh@qq.com
# * Create time   : 2017-04-05 12:53
# * Last modified : 2017-04-05 12:53
# * Filename      : make_label_file.py
# * Description   :
# * Copyright © gumpglh. All rights reserved.
# **********************************************************

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Get the image size from an annotation file.")
    parser.add_argument("class_num",
            help = "the number of classes")


    args = parser.parse_args()
    num = int(args.class_num)
    with open('label.txt', 'w') as f:
        for i in range(num):
            f.write(str(i) + '\n')
