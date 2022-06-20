import os
import glob
from PIL import Image

source_dir = 'D:\dataset\Copy of CASIA2.0_revised\CASIA2.0_revised\Tp\\'
target_dir = 'D:\dataset\Copy of CASIA2.0_revised\CASIA2.0_revised\\JPEGImages\\'

# 如果目标目录不存在的话，进行目录的新建
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 得到源目录中的tif格式文件
files = glob.glob(source_dir + "*.tif")

# 进行文件格式转化与转存
for image_file in files:
    image_name = target_dir+image_file[len(source_dir):-4] + '.jpg'
    with Image.open(image_file) as f:
        rgb_im = f.convert('RGB')
        rgb_im.save(image_name, quality=95, subsampling=0)#quality最高95
