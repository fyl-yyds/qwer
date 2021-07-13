import numpy as np
import matplotlib.pyplot as plt
import random

_x=[i/100 for i in range(100)]
_y=[3*e+4+random.random() for e in _x]

w=random.random()
b=random.random()
for i in range(20):
    for x, y in zip(_x, _y):
        loss = (w * x + b - y) ** 2
        dw = 2 * (w * x + b - y) * x
        db = 2 * (w * x + b - y)
        w = w - dw * 0.1
        b = b - db * 0.1
        print(w, b, loss)

m=[w*e+b for e in _x]
plt.plot(_x,_y,'.')
plt.plot(_x,m)
plt.show()
