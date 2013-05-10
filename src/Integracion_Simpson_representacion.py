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

if __name__ == '__main__':
  
  expr_f = '1/(1+exp(x))'
  expr_p = '0.01686*x**2-0.1714*x+0.42344'
  
  x = linspace(1,6,20)
  
  y_f = zeros(len(x))
  j=0
  for i in x:
     y_f[j] = ev_funcion(i)
     j+=1
  
  y_p = zeros(len(x))
  j=0
  for i in x:
     y_p[j] = ev_parabola(i)
     j+=1

  print '\n    X:          Y(funcion):          Y(parabola):'
  for i in range(len(x)):
    print (" %5f %15f %20f" % (x[i], y_f[i], y_p[i]))

  plot(x, y_f, 'b', x, y_p, 'r--')
  xlim(0, 7)
  ylim(-0.1, 0.5)
  xlabel('Valores de x en [1,6].')
  ylabel('Imagenes de la funcion y la parabola.')
  title('Representacion de f(x) y su parabola')
  legend([expr_f, expr_p])
  
  savefig('rep_funcion.eps')
  
  show()
  