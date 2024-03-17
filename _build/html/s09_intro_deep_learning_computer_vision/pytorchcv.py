# Script file to hide implementation details for PyTorch computer vision module

import builtins
import torch
import torch.nn as nn
from torch.utils import data
import torchvision
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import glob
import os
import zipfile


def plot_convolution(t, title="", data_train=None):
    with torch.no_grad():
        c = nn.Conv2d(kernel_size=(3, 3), out_channels=1, in_channels=1)
        c.weight.copy_(t)
        fig, ax = plt.subplots(2, 6, figsize=(8, 3))
        fig.suptitle(title, fontsize=16)
        for i in range(5):
            im = data_train[i][0]
            ax[0][i].imshow(im[0])
            ax[1][i].imshow(c(im.unsqueeze(0))[0][0])
            ax[0][i].axis("off")
            ax[1][i].axis("off")
        ax[0, 5].imshow(t)
        ax[0, 5].axis("off")
        ax[1, 5].axis("off")
        # plt.tight_layout()
        plt.show()
