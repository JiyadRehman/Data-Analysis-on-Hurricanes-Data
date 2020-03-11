import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Hurricane2.csv")

#data.head()

print(data.describe(include='all').transpose())

datab1 = data.dropna(subset=['Highest_Category', 'Max_Winds_kt'])

datab2 = data.dropna(subset=['Central_Pressure_mb', 'Max_Winds_kt'])

plt.plot(x='Months')


plt.plot(datab1.Highest_Category,datab1.Max_Winds_kt, 'ro')

#ax.yaxis.set_major_locator(plt.NullLocator())
#ax.xaxis.set_major_formatter(plt.NullFormatter())




plt.show()

plt.plot(datab2.Central_Pressure_mb,datab2.Max_Winds_kt, 'ro')