import numpy as np
import random
import matplotlib.pyplot as plt
import time

_x=[i/100 for i in range(100)]
_y=[3*e+4+random.random() for e in _x]

w=random.random()
b=random.random()
for i in range(30):
    for x, y in zip(_x, _y):
        z = w * x + b
        loss = (z - y) ** 2
        dw = 2 * (z - y) * x
        db = 2 * (z - y)
        w = -dw * 0.01 + w
        b = -db * 0.01 + b
        print(w, b, loss)
        time.sleep(0.2)

v=[e*w+b for e in _x]
plt.plot(_x,_y,".")
plt.plot(_x,v)
plt.show()