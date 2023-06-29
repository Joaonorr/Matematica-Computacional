import numpy as np
import scipy.integrate as spi

def f(x):
    return x**2

def df(x):
    return 2*x

def comprimento_arco(f, a, b):
    integrando = lambda x: np.sqrt(1 + (df(x))**2)
    return spi.quad(integrando, a, b)

a = 1
b = 3
L = comprimento_arco(f, a, b)[0]

print("%.5f" % L)