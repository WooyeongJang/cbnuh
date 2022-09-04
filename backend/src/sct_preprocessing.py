import os
import sys
sys.path.append('/home/wyjang/program/MRItoCTDCNN/MRI-to-CT-DCNN-TensorFlow/src/')

import argparse
import cv2
import numpy as np

from utils import all_files_under, n4itk, histogram_matching, get_mask

project_path = '/home/wyjang/IdeaProjects/cbnuh/backend/sct_tmp'
pat = sys.argv[1]
data = project_path + '/raw/' + pat 
save_folder = project_path + '/preprocessing/' + pat
save_folder2 = project_path + '/post/' + pat
temp_id = 0
size = 256
delay = 0
is_save = True

# save_folder = os.path.join(os.path.dirname(data), 'preprocessing')
if is_save and not os.path.exists(save_folder):
    os.makedirs(save_folder)
# save_folder2 = os.path.join(os.path.dirname(data), 'post')
if is_save and not os.path.exists(save_folder2):
    os.makedirs(save_folder2)
    

# read all files paths
filenames = all_files_under(data, extension='jpg')
# read template image
temp_filename = filenames[temp_id]

# read template image
filenames[temp_id]
ref_img = cv2.imread(temp_filename, cv2.IMREAD_GRAYSCALE)
ref_img = ref_img[:, -size:].copy()
_, ref_img = n4itk(ref_img) 


def imshow(ori_mr, cor_mr, his_mr, masked_mr, mask, ori_ct, masked_ct, size=256, delay=0, himgs=2, wimgs=5, margin=5):
    canvas = 255 * np.ones((himgs * size + (himgs-1) * margin, wimgs * size + (wimgs-1) * margin), dtype=np.uint8)

    first_rows = [ori_mr, cor_mr, his_mr, masked_mr, mask]
    second_rows = [ori_ct, 255*np.ones(ori_ct.shape), 255*np.ones(ori_ct.shape), masked_ct, mask]
    for idx in range(len(first_rows)):
        canvas[:size, idx*(margin+size):idx*(margin+size)+size] = first_rows[idx]
        canvas[-size:, idx*(margin+size):idx*(margin+size)+size] = second_rows[idx]

    return canvas

    
for idx, filename in enumerate(filenames):
        print('idx: {}, filename: {}'.format(idx, filename))
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)        
        ct_img = img[:, :size]
        mr_img = img[:, -size:]
        # N4 bias correction
        ori_img, cor_img = n4itk(mr_img)
        # Dynamic histogram matching between two images
        his_mr = histogram_matching(cor_img, ref_img)
        # Mask estimation based on Otsu auto-thresholding
        mask=get_mask(his_mr, task='m2c')
        # Masked out
        masked_ct = ct_img & mask
        masked_mr = his_mr & mask
        canvas = imshow(ori_img, cor_img, his_mr, masked_mr, mask, ct_img, masked_ct, size=size, delay=delay)
        canvas2 = np.hstack((masked_mr, masked_ct, mask))
        if is_save:
            cv2.imwrite(os.path.join(save_folder, os.path.basename(filename)), canvas)
            cv2.imwrite(os.path.join(save_folder2, os.path.basename(filename)), canvas2)


