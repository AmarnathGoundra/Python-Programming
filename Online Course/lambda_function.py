# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:56:27 2023

@author: amar
"""


"""
def is_even(n):
    return n%2 == 0

num = [5,3,7,4,8,5,54,8,98,34,2,6,6]

even = list(filter(is_even,num))

print(even)
"""

num = [5,3,7,4,8,5,54,8,98,34,2,6,6]

even = list(filter(lambda n: n%2 == 0,num))

print(even)

"""
def is_double(n):
    return n*2

doubles = list(map(is_double,num))

print(doubles)
"""

doubles = list(map(lambda n : n*2,num))

print(doubles)