# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:31:08 2023

@author: amar
"""

from functools import reduce

num = [3,5,7,5,3,56,7,3,7,4,7]

sum = reduce(lambda a, b : a+b, num)

print(sum)