import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.utils.data import Dataset,DataLoader
from PIL import Image
import os
import cv2
import numpy as np
import pandas as pd


class FashionDataset(Dataset):
    def __init__(self,df,images_path='./classification-assignment/images/'):
        super().__init__()
        self.images_path = images_path
        self.df =df
    
    def __getitem__(self,index):
        path = os.path.join(self.images_path,self.df.loc[index,"filename"])
        img = FashionDataset.augment(Image.open(path))
        img = torchvision.transforms.ToTensor()(img)
        img = torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(img)
        y = torch.tensor(self.df.loc[index,["neck","sleeve_length","pattern"]].values.astype('int64'))
        return img,y
    
    def __len__(self):
        return len(self.df)
        
    @staticmethod
    def augment(img):
        img = torchvision.transforms.Resize(size=(310,310))(img)
        img =torchvision.transforms.RandomCrop(size=(299,299))(img)
        img = torchvision.transforms.ColorJitter(brightness=0.5,contrast=0.5,saturation=0.5,hue=0.5)(img)

        img = np.array(img)
        # Rotation...
        angle = (50*np.random.normal())
        image_center = tuple(np.array(img.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        img = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

        img = Image.fromarray(img) 
        return img