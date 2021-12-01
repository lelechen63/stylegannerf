import os 
import cv2
path = '/home/uss00022/lelechen/github/stylegan2-ada-pytorch-lele/out'

proj_imgs = []
for i in os.listdir(path):
    if '_proj.png' in i:
        proj_imgs.append(i)

proj_imgs.sort()
proj_imgs = proj_imgs[:10]
for i in proj_imgs:
    proj =cv2.imread( path + '/' + i )
    gt = cv2.imread(path +'/' + i.replace('proj', 'target'))
    print (proj.shape, gt.shape)