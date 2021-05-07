import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('National_Daily_Deaths.csv')

# print(df.columns)

ndd=df['National_Daily_Deaths']
date=df['Date']

plt.plot(date,ndd, 'r-')
plt.ylabel('National daily deaths')
plt.xlabel('Date')
plt.show()