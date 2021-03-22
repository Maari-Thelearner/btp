from _main import prep
import os
from PIL import Image
import glob
d = r"C:\Users\Sameer\Desktop\BTP-1\tamil_dataset_offline_conv/"
dest = r"C:\Users\Sameer\Desktop\BTP-1\tamil_dataset_offline_processed/"
_dirs = [ f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f)) ]
os.mkdir(dest)
print ("dirs: " + str(_dirs))
for _dir in _dirs:
    print ("under dir: " + _dir)
    i = 0
    os.mkdir(dest+_dir)
    files = [ f for f in os.listdir(d + _dir) if os.path.isfile(os.path.join(d + _dir,f)) ]
    t = len(files)
    for f in files:
        prep(d+_dir+'/'+f,dest+_dir)