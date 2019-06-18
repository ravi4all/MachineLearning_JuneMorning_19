import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('SaratogaHouses.csv')

x = np.array([df['heating'].value_counts()[0], df['heating'].value_counts()[1], df['heating'].value_counts()[2]])
lab = ['electric','hot water/steam', 'hot air']
col = ['red','blue','yellow']

plt.pie(x,
        labels=lab,
        colors=col,
        startangle=90,
        explode = (0,0.2,0),
        autopct = '%1.1f%%',
        shadow=True)
plt.legend()
plt.show()
