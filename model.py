import torch
import torch.nn as nn

# Define a simple neural network class
class ArtificialNeuralNetwork(nn.Module):
    def __init__(self, weights=None, num_classes=10):
        super(ArtificialNeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(128, 64)
        self.relu2 = nn.ReLU()
        self.fc = nn.Linear(64, num_classes)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.fc(x)
        return x