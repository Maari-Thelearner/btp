import os
from PIL import Image
import glob
d = r"C:/Users/Sameer/Desktop/BTP-1/tamil_dataset_offline/"
dest = r"C:\Users\Sameer\Desktop\BTP-1\tamil_dataset_offline_conv/"
_dirs = [ f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f)) ]

print ("dirs: " + str(_dirs))
for _dir in _dirs:
    print ("under dir: " + _dir)
    i = 0
    #os.mkdir(dest+_dir)
    files = [ f for f in os.listdir(d + _dir) if os.path.isfile(os.path.join(d + _dir,f)) ]
    t = len(files)
    for f in files:
        #if not os.path.exists(dest+_dir):
            
        #print(f[-5:])
        #if f[-5:]==".tiff":
        #    print (' ... processing image ' + str(i) + '/' + str(t) + ' --- '  + f + ' '+ str (int(float(i)/float(t) * 100)) + '% complete.')
        #    im = Image.open(d+_dir+'/'+f)
        #    f = str(f).rstrip(".tiff")
        #    im.save(dest+_dir+'/'+f + '.jpg', 'JPEG')
        if f[-4:]==".png":
            print (' ... processing image ' + str(i) + '/' + str(t) + ' --- '  + f + ' '+ str (int(float(i)/float(t) * 100)) + '% complete.')
            im = Image.open(d+_dir+'/'+f)
            f = str(f).rstrip(".png")
            im.save(dest+_dir+'/'+f + '.jpg', 'JPEG')