import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv('bookdetails.csv')

print(type(dataSet))
print(dataSet)
print(dataSet.describe())
print(dataSet.columns)
print(sum(dataSet['Price']))
print(sum(dataSet['Rating']))
print(dataSet[['Price','Rating']])
print(dataSet['Price'])
print(dataSet[dataSet.Stock.str.contains(r'Out')]['Price'])
print(dataSet[dataSet['Rating']>=4.0][['Title','Price']])
print(dataSet[dataSet.Rating.between(3.5,4.5)]['Title'])


#Chart1
price_group = dataSet[['Price']]
print(price_group)
bar_plot = price_group.plot()
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

#Chart2
price_group = dataSet[['Price']]
bar_plot = price_group.plot(kind='bar')
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

#Chart3
price_group = dataSet[['Price','Rating']]
bar_plot = price_group.plot(kind='bar',title="Book Price and Rating")
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

#Chart4
labels = dataSet[['Stock']]
print(labels)
price_group = dataSet[['Price','Rating']]
bar_plot = price_group.plot(kind='bar',title="Book Price and Rating")
bar_plot.set_xlabel("No of Books")
bar_plot.set_xticklabels(labels)
bar_plot.set_ylabel("Price")
plt.show()

#Chart5 - PieChart
prices = dataSet['Price'][0:6] #Price from first 6 items
labels = dataSet['Title'][0:6] #Book Titles from first 6 items
legends,ax1 = plt.pie(prices, labels=labels, shadow=True, startangle=45)
plt.legend(legends, prices, loc="best")
plt.show()
