import matplotlib.pyplot as plt
import numpy as np

#x = np.array([2,4,6,8,10,12,14,16,18,20])
#y = np.array([100,110,130,150,200,260,280,300,310,380])

x = np.array([i for i in range(100)])
#y = np.linspace(200,100000,10000)
y = x**3

plt.plot(x,y)
#plt.plot(x,y,'ro')
plt.show()
