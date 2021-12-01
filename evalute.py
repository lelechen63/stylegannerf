import os 
import cv2
path = '/home/uss00022/lelechen/github/stylegan2-ada-pytorch-lele/out'
import PIL.Image
import numpy as np
# Load mask
mask = PIL.Image.open("/home/uss00022/lelechen/github/lighting/predef/facial_mask_v10.png")
# mask = PIL.Image.open("/home/uss00022/lelechen/github/lighting/predef/facial_mask_v10.png")

mask = np.array(mask)[500:2500, 1019 : 3019]/ 255.0
mask = cv2.resize(mask, (256,256))
mask = np.expand_dims(mask, axis=2)

proj_imgs = []
for i in os.listdir(path):
    if '_proj.png' in i:
        proj_imgs.append(i)

proj_imgs.sort()
proj_imgs = proj_imgs[:10]
for i in proj_imgs:
    synth_image =cv2.imread( path + '/' + i )
    target_pil = PIL.Image.open(path +'/' + i.replace('proj', 'target'))

    image = np.array(target_pil)[500:2500, 1019 : 3019]
    image = cv2.resize(image, (256,256) ) * mask
    target_uint8 = image.astype(np.uint8)

    tmp =np.concatenate([target_uint8, synth_image], axis=1)
    cv2.imwrite('./tmp.png', tmp)
    break