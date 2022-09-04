import cv2
import sys
import os 

sys.path.append('/home/wyjang/program/MRItoCTDCNN/MRI-to-CT-DCNN-TensorFlow/src/')
from utils import all_files_under

eh_temp_path_backend_jpg = sys.argv[1]
esct_temp_path_backend_jpg = sys.argv[2]


if os.path.isdir(eh_temp_path_backend_jpg):
    filenames = all_files_under(eh_temp_path_backend_jpg, extension='jpg')
    for filename in filenames:
        img = cv2.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE), dsize = (256, 256))
        f = filename.split('/')[-1]
        if not os.path.exists(esct_temp_path_backend_jpg):
            os.makedirs(esct_temp_path_backend_jpg)

        img = cv2.hconcat([img, img])
        cv2.imwrite(esct_temp_path_backend_jpg + '/' + f, img)
        
    
