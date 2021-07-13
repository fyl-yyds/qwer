import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10.1,10.1,0.1)
y=np.maximum(0,x)

plt.plot(x,y)

plt.show()

