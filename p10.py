from math import *
import numpy as np
from scipy import linalg
import pylab as pl
def lowess(x, y, f, iter=3):
    n = len(x)
    r = int(f*n)
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]
    w = np.clip(np.abs((x[:,None] - x[None,:]) / h), 0, 1)
    w = (1 - w**3)**3
    est = np.zeros(n)
    delta = np.ones(n)
    for it in range(iter):
        for i in range(n):
            weights = delta * w[:,i]
            b = np.array([np.sum(weights*y), np.sum(weights*y*x)])
            A = np.array([[np.sum(weights), np.sum(weights*x)], [np.sum(weights*x), np.sum(weights*x*x)]])
            b = linalg.solve(A, b)
            est[i] = b[0] + b[1] * x[i]
        res = y - est
        s = np.median(np.abs(res))
        delta = np.clip(res / (6 * s), -1, 1)
        delta = (1 - delta**2)**2
    return est
x = np.linspace(0, 2 * 3.14, 100)
print("==========================values of x=====================\n",x)
y = np.sin(x) + 0.3 * np.random.randn(100)
print("================================Values of y===================\n",y)
est = lowess(x, y, .25, 3)
pl.clf()
pl.plot(x, y)
pl.plot(x, est)
pl.show()