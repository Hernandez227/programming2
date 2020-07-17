# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:53:07 2020

@author: erick


Programa que reciba una matriz cuadradra e intercambie las filas desde arriba
hacia abajo de tal manera que el elemento de mayor magnitud de cada columna 
se ubique en diagonal y se sustituya con ceros el resto de la fila hacia la derecha
"""


import  numpy as np

n = int(input('Ingrese numero de n para matriz nxn: '))

print('')

matriz = np.zeros([n,n],int)

for i in range(n):

    for j in range(n):
        print('Ingrese el dato',(i,j))

        matriz[i][j] = int(input(''))
print('')

print('Matriz original \n',matriz,'\n')

matrizfinal = np.zeros([n,n],int)

for i in range(n-1):

    vector = matriz[i:,i:].tolist()

    vector.sort(reverse=-1)

    matriz = np.array(vector)

    matrizfinal[i:,i:] = matriz

    matriz[0,1:] = 0

    matrizfinal[i,i+1:] = 0

    if i>= 1 and matrizfinal[i,i-1] > matrizfinal[i+1,i-1]:

        matrizfinal[i,i-1],matrizfinal[i+1,i-1]=matrizfinal[i+1,i-1],matrizfinal[i,i-1]

print("matriz final \n",matrizfinal)