import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x**2

pontos = []

def trapezoidal(g, a, b):
  h = b - a
  return ((g(a) + g(b))*h)/2

def trapezoidal_quad(g, a, b, eps):
  mid = (a+b)/2

  tot = trapezoidal(g, a, b)

  if abs( trapezoidal(g, a, mid) + trapezoidal(g, mid, b) - tot) > eps:
    return trapezoidal_quad(g, a, mid, eps ) + trapezoidal_quad(g, mid, b, eps )
  else:
    pontos.append(a)
    pontos.append(b) 
    return tot

print( trapezoidal_quad(f, 1, 3, 1e-5))
print( len(pontos))

figure, axis = plt.subplots(1, 2)
x = np.linspace(-10,10,100)
axis[0].plot(x, [f(z) for z in x], '-r')
axis[0].grid()

axis[1].plot(pontos, [f(z) for z in pontos], '-b')
axis[1].grid()

plt.show()