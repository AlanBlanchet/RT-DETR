import torch.nn as nn
from detrcore import register

CrossEntropyLoss = register(nn.CrossEntropyLoss)
