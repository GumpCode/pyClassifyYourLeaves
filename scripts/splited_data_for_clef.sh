#!/bin/bash
#
# This script performs the following operations:
# 1. build the data for clef
#
# Usage:
# cd pyClassifyYourLeaves
# ./scripts/build_data_for_clef.sh

DATA_DIR=data/CLEF_data/FourniApresCLEF2012/data/train
EXCEL_FILE=data/CLEF_data/perClassNum.xls
RESIZE_TYPE=resize
SPLITED_DATA_DIR=splited_data

# Run processing.
python datasets/preSplitDataset.py \
  --data-dir=${DATA_DIR} \
  --excel_file=${EXCEL_FILE} \
  --splited_data_dir=${SPLITED_DATA_DIR} \
  --resize=${RESIZE_TYPE} 
