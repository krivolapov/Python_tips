# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:32:17 2020

@author: makkri01
"""

class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __repr__(self):
        return("Simple calculator")
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    
