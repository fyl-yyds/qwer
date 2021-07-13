import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-3,3.1,0.1)
y=np.power(2,x)
x1=np.arange(-3,3.1,0.1)
y1=np.power(0.5,x)
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()