import mritopng
import sys
import os 

dic_path = sys.argv[1]
png_path = sys.argv[2]

if os.path.isdir(dic_path):
    mritopng.convert_folder(dic_path, png_path)
else:
    mritopng.convert_file(dic_path, png_path)
