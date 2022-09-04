import cv2
import sys
import os 

sys.path.append('/home/wyjang/program/MRItoCTDCNN/MRI-to-CT-DCNN-TensorFlow/src/')
from utils import all_files_under

sct_temp_path_frontend_png = sys.argv[1]
sct_temp_path_frontend_jpg = sys.argv[2]

if not os.path.exists(sct_temp_path_frontend_jpg):
    os.makedirs(sct_temp_path_frontend_jpg)

if os.path.isdir(sct_temp_path_frontend_png):
    filenames = all_files_under(sct_temp_path_frontend_png, extension='jpg')
    if len(filenames) == 0:
        filenames = all_files_under(sct_temp_path_frontend_png, extension='png')
    for filename in filenames:
        f = filename.split('/')[-1]
        res = cv2.imread(filename, cv2.IMREAD_COLOR)
        res = res[0:256, 256:512]
        cv2.imwrite(sct_temp_path_frontend_jpg + '/' + f, res)
        
else:
    res = cv2.imread(sct_temp_path_frontend_png, cv2.IMREAD_COLOR)
    res = res[0:256, 256:512]
    cv2.imwrite(sct_temp_path_frontend_jpg, res)
