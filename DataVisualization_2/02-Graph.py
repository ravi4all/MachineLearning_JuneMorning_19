import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('appl_1980_2014.csv')
print(df.head())
df['Date'] = pd.to_datetime(df['Date'])

x = df['Date']
y = df['Adj Close']
plt.plot(x,y)
plt.show()
