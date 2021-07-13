import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-5,5.1,0.1)
y=1/(1+np.exp(-x))
y1=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
plt.plot(x,y)
plt.plot(x,y1)
plt.show()