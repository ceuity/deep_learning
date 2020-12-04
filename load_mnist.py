# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 06:00:12 2020

@author: EVer
"""

import sys, os
sys.path.append(os.pardir)
from database.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)