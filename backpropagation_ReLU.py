# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:18:45 2020

@author: EVer
"""
import numpy as np

class Relu:
    def __init__(self):
        self.mask = None
        
    def forword(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        
        return out
    
    def backword(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx
    
x = np.array([[1.0, -0.5], [-2.0, 3.0]])
a = Relu()
print(x)
print(a.forword(x))
print(a.mask)