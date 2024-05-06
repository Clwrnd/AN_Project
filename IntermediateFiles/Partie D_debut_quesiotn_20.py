# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:30:51 2024

@author: sarchis01
"""

from math import *
from matplotlib.pyplot import *
import numpy as np

def G(y,A,b) :
    G = 2 * (A * y - b)
    return G

def rhok(y,A,b) : 
    if (np.array_equal(G(y,A,b),[0,0])) :
        rhok = 0 
        return rhok
    else : 
        rhok = np.linalg.norm(G(y,A,b)**2)/(2 * np.transpose(G(y,A,b)) * A * G(y,A,b))
        return rhok
    
# a correspond à la première valeur testée
# b et A correspondent bien aux valeurs de la fonction.

def gradPO(MaxIter, a, A, b): 
    N = 0
    yk = a
    ykplus1 = 0
    while (N<MaxIter or np.linalg.norm(ykplus1-yk)>10**(-5)) :
        ykplus1 = yk - rhok(yk,A,b) * G(yk,A,b)
        yk = ykplus1
        N = N + 1
        if (np.array_equal(G(yk,A,b),[0,0])):
            N = MaxIter+1
    return yk

#gradPO(100, 0, np.array([[2, 1, 1],[1, 2, 1],[1, 1, 2]]), np.array([[1, 2, 3],[4, 5, 6],[1, 1, 2]]))
#gradPO(100, 0, np.array([[2, 1],[1,2]]), np.array([1, 2]))