# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:55:44 2020

@author: EVer
"""

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    exp_sum_a = np.sum(exp_a)
    y = exp_a / exp_sum_a
    
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))
