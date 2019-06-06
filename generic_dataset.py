from torch.utils.data import Dataset
import os
from PIL import Image
import json

# ==================================================================================
# code by Changsheng Lu, 2019/6/6
# usage example
# ==================================================================================
# path1 = 'kittycat_slegdog_car.json'
# path2 = 'tiger_wolf_truck.json'
# source_set = GenericDataset(
#     filepath=path1,
#     input_transform=transforms.Compose([
#         Resize((300, 300)),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#     ])
# )
# target_set = GenericDataset(
#     filepath=path2,
#     input_transform=transforms.Compose([
#         Resize((300, 300)),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#     ])
# )
# ==================================================================================

class GenericDataset(Dataset):
    def __init__(self, filepath, input_transform=None, target_transform=None):
        self.filepath = filepath
        self.input_transform = input_transform
        self.target_transform = target_transform
        with open(self.filepath, 'r') as fin:
            self.samples = json.load(fin)  # 'self.samples' is a list including n samples [(imagepath, label), ...]

    def __getitem__(self, item):
        (image_path, label) = self.samples[item]
        input_image = Image.open(image_path).convert('RGB')
        if self.input_transform is not None:
            image = self.input_transform(input_image)
        if self.target_transform is not None:
            label = self.target_transform(label)
        return image, label

    def __len__(self):
        return len(self.samples)
		

# ===============================
# show an image
# ===============================
# import matplotlib.pyplot as plt
# source_set = GenericDataset(
#     filepath='kittycat_slegdog_car.json',
#     input_transform=transforms.Compose([
#         Resize((300, 300)),
#         transforms.ToTensor()
#     ])
# )
#
# dataloader = DataLoader(source_set, 1)
# data_iter = iter(dataloader)
# image, label = data_iter.next()
# image2 = image.squeeze().permute(1,2,0)
# plt.imshow(image2)
# plt.show()

