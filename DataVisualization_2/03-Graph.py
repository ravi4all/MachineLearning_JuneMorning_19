import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('SaratogaHouses.csv')
print(df.head())

x = df['livingArea']
y = df['price']

x1 = np.array([i for i in range(len(df['price']))])
y1 = np.linspace(100000,1000000,len(df['price']))

plt.scatter(x,y)
#plt.plot(x1,y1, color='black')
plt.show()
