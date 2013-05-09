#####################################################################
#
# Titulo: Representacion de una funcion y la parabola formada para el metodo de Simpson
#
# Autores: Ivan Trujillo Trujillo
#          Samuel Santos Lucas Castilla
#
# Grupo:  2J
#
######################################################################

#!/usr/bin/python

from matplotlib.pylab import *
from Integracion_Simpson import *
import numpy

#def representa(x, y1, y2):
  

if __name__ == '__main__':
  funcion='1/(1+exp(x))'
  funcion_int='log(exp(x))-log(exp(x)+1)'
  a=1.0
  b=6.0
  x = numpy.linspace(1,6,20)
  y_f = ev_funcion(x)
  y_p = ev_parabola(x)
  print 'X:'
  for i in range(x):
    print (" %f" % i)
  print 'Y(funcion):'
  for i in range(y_f):
    print (" %f" % i)
  print 'Y(parabola):'
  for i in range(y_p):
    print (" %f" % i)
#  representa(x, y_f, y_p)
  