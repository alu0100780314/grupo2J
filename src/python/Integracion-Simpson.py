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

def evalua_expresion(a,expr):
  return ---

def simpson(a,b,expr):
  return ((b-a)/6)*(evalua_expresion(a,expr)+4*evalua_expresion((a+b)/2,expr)+evalua_expresion(b,expr))

if __name__ == '__main__':
  expr='x**2+3*x'
  a=1.0
  b=3.0
  print ("La integral definida entre %f y %f de %s es %f." % (a,b,expr,simpson(a,b,expr)))
