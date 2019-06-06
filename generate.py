import os
import json
import numpy as np
import random

# =========================================================
# code by Changsheng Lu, 2019/6/6
# usage example
# python generate.py
# =========================================================

# the directory of ImageNet based dataset. Please modify to yours.
root = './ImageNet-Based-Dataset'

# the folder names of each class. Please modify to yours.
kittycat_dir = '1.kittycat'
tiger_dir = '2.tiger'
slegdog_dir = '3.slegdog'
wolf_dir = '4.wolf'
car_dir = '5.car'
truck_dir = '6.truck'
label = {
    '1.kittycat':0,  
    '2.tiger':0,  
    '3.slegdog':1,
    '4.wolf':1,
    '5.car':2,
    '6.truck':2
} 

# build the pairs of (image path, label) 
kittycat_imagefiles = [(os.path.join(root, kittycat_dir, filename), label[kittycat_dir]) for filename in os.listdir(os.path.join(root, kittycat_dir))]
tiger_imagefiles = [(os.path.join(root, tiger_dir, filename), label[tiger_dir]) for filename in os.listdir(os.path.join(root, tiger_dir))]
slegdog_imagefiles = [(os.path.join(root, slegdog_dir, filename), label[slegdog_dir]) for filename in os.listdir(os.path.join(root, slegdog_dir))]
wolf_imagefiles = [(os.path.join(root, wolf_dir, filename), label[wolf_dir]) for filename in os.listdir(os.path.join(root, wolf_dir))]
car_imagefiles = [(os.path.join(root, car_dir, filename), label[car_dir]) for filename in os.listdir(os.path.join(root, car_dir))]
truck_imagefiles = [(os.path.join(root, truck_dir, filename), label[truck_dir]) for filename in os.listdir(os.path.join(root, truck_dir))]

cat_dog_car_sourcefiles = kittycat_imagefiles + slegdog_imagefiles + car_imagefiles
tiger_wolf_truck_targetfiles = tiger_imagefiles + wolf_imagefiles + truck_imagefiles


random.shuffle(cat_dog_car_sourcefiles)
random.shuffle(tiger_wolf_truck_targetfiles)

# write the json file 
with open("kittycat_slegdog_car.json", 'w') as fout:
    json.dump(cat_dog_car_sourcefiles, fout, indent=4)
fout.close()

with open("tiger_wolf_truck.json", 'w') as fout:
    json.dump(tiger_wolf_truck_targetfiles, fout, indent=4)
fout.close()

