import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.utils.data import Dataset,DataLoader


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = torchvision.models.inception_v3(pretrained=True)
        for param in list(self.model.parameters())[:100]:
            param.requires_grad=False
        self.neck = nn.Linear(1000,7)
        self.sleeve = nn.Linear(1000,4)
        self.pattern = nn.Linear(1000,10)
    
    def forward(self,x,eval_=False):
        if eval_ : 
            x = self.model(x)
        else :
            x = self.model(x)[0]
        x1,x2,x3 = [self.neck(x),self.sleeve(x),self.pattern(x)]
        return x1,x2,x3