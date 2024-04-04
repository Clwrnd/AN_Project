# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:47:58 2024

@author: sarchis01
"""

from math import exp
import numpy as np
import matplotlib.pyplot as plt
import random as rand


def BA (a, b ,N) :
    liste = [] 
    for i in range (N) :
        liste.append(f(rand.uniform(a, b))) ;  
    print(liste)
    z = min(liste) ;
    
    return z ;

def f(x) :
    f = x**3 - 3 * x**2 + 2 * x + 5 ;
    return f ;

##plot de l'erreur

N = 100
min = 4.6150998205402494903272341463320283629015988324865820826542651156
erreur = []
print(erreur)

for i in range(2,N) :
    erreur.append(abs(BA(0,3,i) - min)) ;
x=[i+1 for i in range(N)]    
plt.plot(N, erreur)
