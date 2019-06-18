import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('SaratogaHouses.csv')

x = df['rooms']
plt.hist(x,rwidth=0.8, color='red')
plt.title('Number of rooms')
plt.xlabel('No. of room')
plt.ylabel('Count')
plt.show()
