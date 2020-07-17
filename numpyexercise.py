# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:29:31 2020

@author: erick
"""

import numpy as np


A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)

# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)
print('Dot A:')
print(A.dot(A))
print('Dot B:')
print(B.dot(B))
print("\n")
print(A)
print('\n')
print(B)
print('\n')
print('The less is:')
print(A-B)
print('\n')
print('The sum is')
print(A+B)
