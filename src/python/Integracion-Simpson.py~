#####################################################################
#
# Titulo: Integracion numerica por Simpson
#
# Autores: Ivan Trujillo Trujillo
#          Samuel Santos Lucas Castilla
#
# Grupo:  2J
#
######################################################################

#!/usr/bin/python

from math import *

def evalua_expresion(x):
  return 1/(1+exp(x))

def simpson(a,b):
  return ((b-a)/6)*(evalua_expresion(a)+4*evalua_expresion((a+b)/2)+evalua_expresion(b))

if __name__ == '__main__':
  expr='1/(1+exp(x))'
  a=1.0
  b=6.0
  print ("La integral definida entre %.1f y %.1f de %s es aproximadamente %.10f." % (a,b,expr,simpson(a,b)))
