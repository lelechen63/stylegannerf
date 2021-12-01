import os

for i in range(360,1000):
    if os.path.exists('/data/home/uss00022/lelechen/data/Facescape/textured_meshes/%d/models_reg/17_cheek_blowing.jpg'%i):
        out_p = './out/%d'%i 
        os.makedirs(out_p, exist_ok = True)
        command = 'python projector.py --outdir=%s --target=/data/home/uss00022/lelechen/data/Facescape/textured_meshes/%d/models_reg/17_cheek_blowing.jpg --network=./checkpoints/00012-target-face256/network-snapshot-002400.pkl'%(out_p,i)
        os.system(command)