import cv2
import sys
import os 

sys.path.append('/home/wyjang/program/MRItoCTDCNN/MRI-to-CT-DCNN-TensorFlow/src/')
from utils import all_files_under

mri_temp_path_backend_png = sys.argv[1]
mri_temp_path_backend_jpg = sys.argv[2]
mri_temp_path_frontend_jpg = sys.argv[3]


    
if os.path.isdir(mri_temp_path_backend_png):
    filenames = all_files_under(mri_temp_path_backend_png, extension='png')
    for filename in filenames:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        f = filename.split('/')[-1].replace('png','jpg')
        f1 = filename.split('/')[-1] + '.jpg'
        
        if not os.path.exists(mri_temp_path_frontend_jpg):
            os.makedirs(mri_temp_path_frontend_jpg)
        if not os.path.exists(mri_temp_path_backend_jpg):
            os.makedirs(mri_temp_path_backend_jpg)
    
        img_ct = img[:, :256]
        mri_img = img[:, 256:]
        cv2.imwrite(mri_temp_path_frontend_jpg + '/' + f1, mri_img)
        
        img = cv2.hconcat([mri_img, mri_img])
        cv2.imwrite(mri_temp_path_backend_jpg + '/' + f1, img)
        