# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZoR9E0cGekKLIe_ZoSXqDNth-6xojpDO

# Import libraries
"""

import os
import pandas as pd
from torchvision.io import read_image
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

# import google drive
from google.colab import drive
drive.mount('/content/drive')

# Use gpu

# Anything else we can think of

"""# Dataset class
Where is the image
Robovis class to load the data
List of tupes
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd make sure you are in the path where labels file is present, dummy root folder is also present
# %cd "MyDrive"
# %cd "m2cai16-tool-locations"
os.listdir()

class roboDataset(Dataset):
  def __init__(self, labels_file, directory, transforms = None):
    self.labels_file = pd.read_csv(labels_file)
    self.directory = directory
    self.transforms = transforms

  def __len__(self):
    return len(self.labels_file)

  def __getitem__(self, idx):
    img_path = os.path.join(self.directory, self.labels_file.iloc[idx, 0])
    image = read_image(img_path)
    label = self.labels_file.iloc[idx, 1]

    #ToDO
    # Add code for transforms

    return image, label

# define the train_dataset
train_dataset = roboDataset(labels_file = "./labels_wider.csv", directory = "./dummy root/dummy class")

# Make the train dataloaders
train_dataloader = DataLoader(train_dataset, batch_size=1, shuffle=True)
train_features, train_labels = next(iter(train_dataloader))

from torchvision.transforms import ToPILImage
t = ToPILImage()
t(train_features[0])