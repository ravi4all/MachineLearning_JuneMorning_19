import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('SaratogaHouses.csv')

x = df['livingArea'].values
y = df['price'].values
z = df['landValue'].values

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z,'o')
plt.show()
