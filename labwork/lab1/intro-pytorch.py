# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wo1_lJd1GQgB9GxtrJOorrIcvJd73NB5
"""

import torch
torch.__version__

x = torch.tensor([1,2,3], dtype=torch.float32)
y = torch.tensor([4,5,6], dtype=torch.float32)

z = torch.tensor([1,2,3,6], dtype=torch.float32)
z.std()

"""The standard deviation is the sample mean: s.d = [(sum (xi-mu)^2)/(N-1)]^(1/2)

---
"""

x = torch.randn((2, 3, 1, 10, 10))
x

print(x.shape)
print(x.squeeze().shape)

x = torch.arange(0,100)
x.reshape(10,10)

