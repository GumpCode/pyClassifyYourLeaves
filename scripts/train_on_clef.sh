#!/bin/bash
#
# This script performs the following operations:
# 1. Downloads the Cifar10 dataset
# 2. Trains a CifarNet model on the Cifar10 training set.
# 3. Evaluates the model on the Cifar10 testing set.
#
# Usage:
# cd slim
# ./scripts/train_cifar_net_on_mnist.sh

# Where the checkpoint and logs will be saved to.
TRAIN_DIR=log

# Where the dataset is saved to.
DATASET_DIR=splited_data/output


# Run training.
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR} \
  --dataset_name=clef \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --model_name=vgg_16 \
  --preprocessing_name=clef \
  --max_number_of_steps=100000 \
  --batch_size=8 \
  --save_interval_secs=120 \
  --save_summaries_secs=120 \
  --log_every_n_steps=100 \
  --optimizer=sgd \
  --learning_rate=0.0001 \
  --learning_rate_decay_factor=0.1 \
  --num_epochs_per_decay=200 \
  --weight_decay=0.004 \
  --train_image_size=224

# Run evaluation.
#python eval_image_classifier.py \
#  --checkpoint_path=${TRAIN_DIR} \
#  --eval_dir=${TRAIN_DIR} \
#  --dataset_name=cifar10 \
#  --dataset_split_name=test \
#  --dataset_dir=${DATASET_DIR} \
#  --model_name=cifarnet
