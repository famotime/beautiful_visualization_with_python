# 图9-6-1  RadViz图

```python
from pandas.plotting import radviz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('iris.csv')
df

```
```
     sepal.length  sepal.width  petal.length  petal.width    variety
0             5.1          3.5           1.4          0.2     Setosa
1             4.9          3.0           1.4          0.2     Setosa
2             4.7          3.2           1.3          0.2     Setosa
3             4.6          3.1           1.5          0.2     Setosa
4             5.0          3.6           1.4          0.2     Setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  Virginica
146           6.3          2.5           5.0          1.9  Virginica
147           6.5          3.0           5.2          2.0  Virginica
148           6.2          3.4           5.4          2.3  Virginica
149           5.9          3.0           5.1          1.8  Virginica

[150 rows x 5 columns]
```

```python
angle = np.arange(360)/180*3.14159
x = np.cos(angle)
y = np.sin(angle)

fig = plt.figure(figsize=(3.5, 3.5), dpi=100)
ax = radviz(df, 'variety', color=['# FC0000', '# F0AC02', '# 009E88'],
            edgecolors='k', marker='o', s=34, linewidths=1)
plt.plot(x, y, color='gray')
plt.axis('off')
plt.legend(loc="center", bbox_to_anchor=(1.1, 0, 0, 0.4),
           edgecolor='none', facecolor='none', title='Group')

```
```
<matplotlib.legend.Legend at 0x1a4cb4fcfd0>
```
