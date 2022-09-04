import sys
import os
sys.path.append('/home/wyjang/program/MRItoCTDCNN/MRI-to-CT-DCNN-TensorFlow/src/')
import logging
import argparse
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import tensorflow as tf
from datetime import datetime

from dataset import Dataset
from Model import Model
from solver import Solver
pat = sys.argv[1]
project_path = '/home/wyjang/IdeaProjects/cbnuh/backend/sct_tmp'
log_dir = project_path + "/log" 
model_dir = project_path + "/model"
test_dir = project_path + "/test/" + pat
parser = argparse.ArgumentParser(description='main')
parser.gpu_index ='0'
parser.is_train = False
parser.batch_size = 100
parser.dataset =''
parser.learning_rate = 1e-3
parser.weight_decay = 1e-4
parser.epoch = 600
parser.print_freq = 100
parser.load_model = ''
args = parser
logger = logging.getLogger(__name__)  # logger
logger.setLevel(logging.INFO)
os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu_index

def init_logger(log_dir):
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    # file handler
    file_handler = logging.FileHandler(os.path.join(log_dir, 'main.log'))
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    # stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    # add handlers
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info('gpu_index: {}'.format(args.gpu_index))
    logger.info('is_train: {}'.format(args.is_train))
    logger.info('batch_size: {}'.format(args.batch_size))
    logger.info('dataset: {}'.format(args.dataset))
    logger.info('learning_rate: {}'.format(args.learning_rate))
    logger.info('weight_decay: {}'.format(args.weight_decay))
    logger.info('epoch: {}'.format(args.epoch))
    logger.info('print_freq: {}'.format(args.print_freq))
    logger.info('load_model: {}'.format(args.load_model))


init_logger(log_dir) 

# Initialize session
run_config = tf.ConfigProto()
run_config.gpu_options.allow_growth = False
sess = tf.Session(config=run_config)

# Initialize model and solver
num_cross_vals = 6  # num_cross_vals have to bigger than 3 (train dataset, validation dataset, and test dataset)
model = Model(args, name='UNet', input_dims=(256, 256, 1), output_dims=(256, 256, 1), log_path=log_dir)
solver = Solver(sess, model)

mae = np.zeros(num_cross_vals, dtype=np.float32)    # Mean Absolute Error
me = np.zeros(num_cross_vals, dtype=np.float32)     # Mean Error
mse = np.zeros(num_cross_vals, dtype=np.float32)    # Mean Squared Error
pcc = np.zeros(num_cross_vals, dtype=np.float32)    # Pearson Correlation Coefficient

model_sub_dir = os.path.join(model_dir)
test_sub_dir = os.path.join(test_dir)
if not os.path.isdir(test_sub_dir):
    os.makedirs(test_sub_dir)
    
saver = tf.train.Saver(max_to_keep=1)
solver.init()

def restore_model(saver, solver, model_dir, model_id):
    logger.info(' [*] Reading model: {} checkpoint...'.format(model_id))

    ckpt = tf.train.get_checkpoint_state(model_dir)
    if ckpt and ckpt.model_checkpoint_path:
        ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
        saver.restore(solver.sess, os.path.join(model_dir, ckpt_name))
        return True
    else:
        return False


model_id = parser.load_model
if restore_model(saver, solver, model_sub_dir, model_id):  # Restore models
    logger.info(' [*] Load model ID: {} SUCCESS!'.format(model_id))
else:
    logger.info(' [!] Load model ID: {} Failed...'.format(model_id))
    sys.exit(' [!] Cannot find checkpoint...')
    
from utils import all_files_under, load_data
filenames = all_files_under(os.path.join(project_path + '/post/' + pat), extension='jpg')
mrImgs, ctImgs, maskImgs = load_data(filenames, is_test=True)
preds = solver.test(mrImgs, batch_size=args.batch_size)
print("finish pred")
save_filenames = []
for filename in filenames:
    f = filename.split("/")[-1]
    save_filenames.append(test_dir + '/' + f)

num_data, h, w, c = mrImgs.shape

import cv2
from utils import inv_transform

for i in range(num_data):
    mask = np.squeeze(maskImgs[i])
    canvas = np.zeros((h, 3*w), dtype=np.uint8)
    canvas[:, :w] = inv_transform(mrImgs[i])          # Input MR image
    canvas[:, w:2*w] = inv_transform(preds[i]) * mask  # Predicted CT image
    canvas[:, -w:] = inv_transform(ctImgs[i])         # GT CT image
    imgName = save_filenames[i]
    cv2.imwrite(imgName, canvas)