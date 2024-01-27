# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:34:09 2023

@author: amar
"""

def div(a,b):
    print(a/b)
    
def smart_div(func):
    
    def inner(a,b):
        if(a<b):
            a,b = b,a
        return func(a,b)
    
    return inner

div = (smart_div(div))

div(2,4)
