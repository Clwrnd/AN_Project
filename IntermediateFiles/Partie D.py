# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:30:51 2024

@author: sarchis01
"""

from math import *
from matplotlib.pyplot import *
from numpy import *

def rhok(y,A) : 
    if (G(y) == 0) :
        rhok = 0 
        return rhok
    else : ##trouver la fonctio pour faire la transposée
        rhok = absolute(G(y)**2)/(2 * T G(y) * A *G(y))
        return rhok
    

def gradPO(eps, MaxIter, rho, yk, phi): 
    
    while (N>MaxIter or absolute(ykplus1-yk)<eps) :
        yplus1 = yk - rhok