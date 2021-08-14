# 图7-1-1 多数据系列图_matplotlib

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_csv('Line_Data.csv', index_col=0)
df.index = [datetime.strptime(d, '%Y/%m/%d').date() for d in df.index]
df

```
```
              AMZN    AAPL
2000-01-01   69.00   25.94
2000-02-01   67.00   28.66
2000-03-01   55.00   33.95
2000-04-01   48.00   31.01
2000-05-01   36.00   21.00
...            ...     ...
2009-10-01  136.00  188.50
2009-11-01  134.52  199.91
2009-12-01  125.00  210.73
2010-01-01  118.00  192.06
2010-02-01  129.00  204.62

[122 rows x 2 columns]
```
## 图611 多数据系列图. (a)折线图

```python
fig = plt.figure(figsize=(5, 4), dpi=100)
plt.plot(df.index, df.AMZN, color='# F94306', label='AMZN')
plt.plot(df.index, df.AAPL, color='# 06BCF9', label='AAPL')
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left', edgecolor='none', facecolor='none')
plt.show()

```
```
<Figure size 500x400 with 1 Axes>
```
## 图611 多数据系列图.(b)面积图.

```python
columns = df.columns
colors = ["# F94306", "# 06BCF9"]
fig = plt.figure(figsize=(5, 4), dpi=100)
plt.fill_between(df.index.values, y1=df.AMZN.values, y2=0,
                 label=columns[1], alpha=0.75, facecolor=colors[0], linewidth=1, edgecolor='k')
plt.fill_between(df.index.values, y1=df.AAPL.values, y2=0,
                 label=columns[0], alpha=0.75, facecolor=colors[1], linewidth=1, edgecolor='k')
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left', edgecolor='none', facecolor='none')
plt.show()

```
```
<Figure size 500x400 with 1 Axes>
```
## 图613 夹层填充面积图. (a)单色

```python
df = pd.read_csv('Line_Data.csv')

# df['date'].map(lambda x:datetime.datetime.strptime(x, '%Y/%m/%d').date())
df['date'] = [datetime.strptime(d, '%Y/%m/%d').date() for d in df['date']]

df['ymin'] = df[['AMZN', 'AAPL']].apply(lambda x: x.min(), axis=1)
df['ymax'] = df[['AMZN', 'AAPL']].apply(lambda x: x.max(), axis=1)

fig = plt.figure(figsize=(5, 4), dpi=100)
plt.fill_between(df.date.values, y1=df.ymax.values, y2=df.ymin.values,
                 alpha=0.15, facecolor='black', linewidth=1, edgecolor='k')
plt.plot(df.date, df.AMZN, color='# F94306', label='AMZN')
plt.plot(df.date, df.AAPL, color='# 06BCF9', label='AAPL')
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left', edgecolor='none', facecolor='none')
plt.show()

```
```
<Figure size 500x400 with 1 Axes>
```
