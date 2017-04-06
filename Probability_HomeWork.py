# -*- coding: utf-8 -*-
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from scipy.stats import norm

fig = plt.gcf()
fig.set_size_inches(8,5)

var('x')
f = lambda x: exp(-x**2/2)

x = np.linspace(-4,4,100)
y = np.array([f(v) for v in x],dtype='float')

plt.grid(True)
plt.title('Gaussian Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y,color='red')
plt.fill_between(x,y,0,color='#123456')
plt.show()


fig, ax = plt.subplots(1, 1)
x = np.linspace(norm.ppf(0.01),norm.ppf(0.99), 100)
ax.plot(x, norm.pdf(x),'r-', lw=5, alpha=0.6, label='norm pdf')
ax.plot(x, norm.pdf(x), 'k-', lw=2, label='frozen pdf')
# r = norm.rvs(size=1000)
# ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
plt.show()