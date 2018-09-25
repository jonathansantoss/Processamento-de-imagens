'''
Created on 25 de set de 2018

@author: Jonathan
'''

import random
from PIL import Image
from builtins import range


imagemLenna = Image.open('Lenna.tif')
imagemLenna.show()

imagemTonsCinza = imagemLenna.convert('L')
imagemTonsCinza.show()


T = 127 #Threshold

h = imagemTonsCinza.size[0]
w = imagemTonsCinza.size[1]

hAl = random.randrange(int(h))
wAl = random.randrange(int(w)) 


def cinza(tupla):
    ass = tupla
    #m = int( (r+g+b) /3) 
    return ass

#def marca(n1 , n2):
#    lista = [n1,n2,True]
#    return lista

def recurse(x, y):
    m1 = cinza(imagemTonsCinza.getpixel( (x, y) ) )
    m2 = cinza(imagemTonsCinza.getpixel( (x, y + 1) ) )
    subM = m1 - m2
    
    if subM == 0:
        recurse(x, y + 1)
    if subM != 0:
        recurse(x, y + 1)


a = recurse(hAl, wAl)
b = recurse(hAl, wAl)