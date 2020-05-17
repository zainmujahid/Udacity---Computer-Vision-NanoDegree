## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        # layer_1 -> [conv[kernel 5X5, padding = (5 - 1) / 2 = 2, stride = 1, depth = 32, input = (224 X 224 X 1)] X 1]
        #         ->  output 112 X 112 X 32
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=5, stride=1, padding=2),
            # nn.Conv2d(32, 32, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        
        # layer_2 -> [conv[kernel 3X3, padding = (3 - 1) / 2 = 1, stride = 1, depth = 64, input = (112 X 112 X 32)] X 1]
        #         ->  output 56 X 56 X 64
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            # nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))

        # layer_3 -> [conv[kernel 3X3, padding=(3 - 1) / 2=1, stride=1, depth=128, input=(56 X 56 X 64)] X 1]
        #         ->  output 28 X 28 X 128
        self.layer3 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            # nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))

        # layer_4 -> [conv[kernel 3X3, padding=(3 - 1) / 2 = 1, stride=1, depth=256, input=(28 X 28 X 256)] X 1]
        #         ->  output 14 X 14 X 256
        self.layer4 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            # nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))

        # layer_5 -> [conv[kernel 3X3, padding=(3 - 1) / 2 = 1, stride=1, depth=256, input=(14 X 14 X 256)] X 1]
        #         ->  output 7 X 7 X 256
        self.layer5 = nn.Sequential(
            nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            # nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        
         # =========================== Regression using fully connected layer ===========================================
        self.layer6 = nn.Linear(7*7*256, 136)
        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        x = self.layer5(self.layer4(self.layer3(self.layer2(self.layer1(x)))))    # using fully connected layer
        x = x.reshape(x.size(0), -1)
        x = self.layer6(x)        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
