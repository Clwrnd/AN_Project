# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:30:51 2024

@author: sarchis01
"""

from math import *
from matplotlib.pyplot import *
from numpy import *
A = 0

b = Ax

def G(y,A,b) :
    G = 2 * (A * y - b)
    return G

def rhok(y,A,b) : 
    if (G(y,A,b) == 0) :
        rhok = 0 
        return rhok
    else : 
        rhok = absolute(G(y,A,b)**2)/(2 * G(y,A,b) * np.transpose(A) * G(y,A,b))
        return rhok
    

def gradPO(eps, MaxIter, a, b): 
    yk = 
    while (N>MaxIter or absolute(ykplus1-yk)<eps) :
        ykplus1 = yk - rhok
        
