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

def ev_funcion(x):
  return 1/(1+exp(x))
  
def ev_funcion_int(x):
  return log(exp(x))-log(exp(x)+1)
  
def int_real(a,b):
  return ev_funcion_int(b)-ev_funcion_int(a)

def int_simpson(a,b):
  return ((b-a)/6)*(ev_funcion(a)+4*ev_funcion((a+b)/2)+ev_funcion(b))

if __name__ == '__main__':
  funcion='1/(1+exp(x))'
  funcion_int='log(exp(x))-log(exp(x)+1)'
  a=1.0
  b=6.0
  error=abs(int_real(a,b)-int_simpson(a,b))
  print ("La integral definida entre %.1f y %.1f de %s es realmente %.7f unidades cuadradas." % (a,b,funcion,int_real(a,b)))
  print ("La integral definida entre %.1f y %.1f de %s es aproximadamente %.7f unidades cuadradas." % (a,b,funcion,int_simpson(a,b)))
  print ("El error absoluto entre los dos calculos es %.10f." % error)

