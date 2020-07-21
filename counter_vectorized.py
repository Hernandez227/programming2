# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:46:49 2020

@author: erick
"""


import numpy as np

animals = np.array(['Cow', 'Elephant', 'Snake', 'Camel', 'Praying Mantis'])
print(animals)

vlen = np.vectorize(len)
print(vlen(animals))