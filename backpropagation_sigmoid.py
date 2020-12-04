# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:57:34 2020

@author: EVer
"""

import numpy as np

class Sigmoid:
    def __init__(self):
        self.out = None
    
    def forword(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        
        return out
    
    def backword(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        
        return dx