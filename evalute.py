import os 
import cv2
path = '/home/uss00022/lelechen/github/stylegan2-ada-pytorch-lele/out'
import PIL.Image
import math

import numpy as np
def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR

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

# proj_imgs.sort()
proj_imgs = proj_imgs[:100]

gg = []
for i in proj_imgs:
    synth_image =cv2.imread( path + '/' + i )
    target_pil = PIL.Image.open(path +'/' + i.replace('proj', 'target'))

    image = np.array(target_pil)[500:2500, 1019 : 3019]
    image = cv2.resize(image, (256,256) ) * mask
    target_uint8 = image.astype(np.uint8)
    target_uint8 = cv2.cvtColor(target_uint8, cv2.COLOR_RGB2BGR)

    tmp =np.concatenate([target_uint8, synth_image], axis=1)
    gg.append(psnr(target_uint8, synth_image))
    print (gg[-1])

print (sum(gg)/len(gg))