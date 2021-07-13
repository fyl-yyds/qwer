import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10,10.1,0.1)
y=np.power(x,2)
x1=np.arange(0,10,0.1)
y1=np.power(x1,0.5)
x2=np.arange(-10,10.1,0.1)
y2=np.power(x2,3)
x3=np.arange(0.1,10.1,0.1)
y3=np.power(x3,-1)
plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.show()