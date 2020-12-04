# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:50:59 2020

@author: EVer
"""

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    def forword(self, x, y):
        self.x = x
        self.y = y
        out = x * y
       
        return out
        
    def backword(self, dout):
        dx = dout * self.y
        dy = dout * self.x
    
        return dx, dy
    
class AddLayer:
    def __init__(self):
        self.x = None
        self.y = None
        
    def forword(self, x, y):
        self.x = x
        self.y = y
        out = x + y
        
        return out
    
    def backword(self, dout):
        dx = dout * 1
        dy = dout * 1
        
        return dx, dy
    
apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

# forword propagation
apple_price = mul_apple_layer.forword(apple, apple_num)
orange_price = mul_orange_layer.forword(orange, orange_num)
all_price = add_apple_orange_layer.forword(apple_price, orange_price)
price = mul_tax_layer.forword(all_price, tax)


#backpropagation 
dprice = 1
dall_price, dtax = mul_tax_layer.backword(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backword(dall_price)
dorange, dorange_num = mul_orange_layer.backword(dorange_price)
dapple, dapple_num = mul_apple_layer.backword(dapple_price)

