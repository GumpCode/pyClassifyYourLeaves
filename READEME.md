cd pyClassifyYourLeaves

#split data to train and test dir. size(256x256)
sh scripts/splited_data_for_clef.sh

#convert data to tfrecord format
sh scripts/build_data_for_clef.sh

#open datasets/clef.py
vim datasets/clef.py
#write the num of train/test to datasets/clef.py

#check the parameter for scripts/train_on_clef.sh
vim scripts/train_on_clef.sh

#start to training
sh scripts/train_on_clef.sh
