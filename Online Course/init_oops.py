# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:41:37 2023

@author: amar
"""

class computer:
    
    def __init__(self,cpu,ram):
        print("In init")
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("config is", self.cpu, self.ram)
        
com1 = computer('i5',16)
com2 = computer('Ryzen',8)


com1.config()
com2.config()