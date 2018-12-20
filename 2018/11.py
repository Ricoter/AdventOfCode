import numpy as np

serial = 28
grid = np.zeros((300,300))

def power_level(x, y):
    rack_id = x + 10
    power = y * rack_id
    power += serial
    power *= rack_id
    power = int((power%1000)/100)
    power -= 5
    return power

for i in range(300):
    for j in range(300):
        grid[i][j] = power_level(i+1, j+1)

import torch
import torch.nn as nn
import torch.nn.functional as F

size = 3
tensor = torch.from_numpy(grid[None, None,:,:])
#pooled = (size**2) * F.avg_pool2d(tensor, size)
filters = torch.Tensor(torch.ones(1,1,3,3), dtype=torch.double)
pooled = F.conv2d(tensor, filters, stride=1)
pooled = pooled.squeeze().numpy()

value = np.max(pooled)
index = np.unravel_index(np.argmax(pooled, axis=None), pooled.shape)

print(value, index)
