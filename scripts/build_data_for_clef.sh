#!/bin/bash
#
# This script performs the following operations:
# 1. build the data for clef
#
# Usage:
# cd pyClassifyYourLeaves
# ./scripts/build_data_for_clef.sh

DATA_DIR=splited_data
FIRST_DIR=${DATA_DIR}/part_first
SECOND_DIR=${DATA_DIR}/part_second
LABEL_FILE=${DATA_DIR}/label.txt
OUTPUT_DIR=${DATA_DIR}/output
SHARDS=1

# Run processing.
python datasets/preSplitDataset.py \
  --PART_first_directory=${FIRST_DIR} \
  --PART_second_directory=${SECOND_DIR} \
  --output_directory=${OUTPUT_DIR} \
  --shards=${SHARDS} \
  --labels_file=${LABEL_FILE} \
  --num_threads=1
