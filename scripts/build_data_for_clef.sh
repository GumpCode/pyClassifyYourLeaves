#!/bin/bash
#
# This script performs the following operations:
# 1. build the data for clef
#
# Usage:
# cd pyClassifyYourLeaves
# ./scripts/build_data_for_clef.sh

DATA_DIR=splited_data
TRAIN_DIR=${DATA_DIR}/train
TEST_DIR=${DATA_DIR}/test
LABEL_FILE=label.txt
OUTPUT_DIR=${DATA_DIR}/output
CLASS_NUM=72
SHARDS=1

#make label_file 
python datasets/make_label_file.py \
  ${CLASS_NUM}

# Run processing.
python datasets/build_data_for_clef.py \
  --train_directory=${TRAIN_DIR} \
  --test_directory=${TEST_DIR} \
  --output_directory=${OUTPUT_DIR} \
  --shards=${SHARDS} \
  --labels_file=${LABEL_FILE} \
  --num_threads=1
