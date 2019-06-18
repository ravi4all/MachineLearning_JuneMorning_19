import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('SaratogaHouses.csv')

x = df['rooms']
y = df['price']
plt.bar(x,y)
plt.title('Price w.r.t no of rooms')
plt.xlabel('No. of room')
plt.ylabel('Price')
plt.show()
