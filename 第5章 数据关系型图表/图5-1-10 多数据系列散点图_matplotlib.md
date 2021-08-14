# 图5-1-10 多数据系列散点图_matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('MultiSeries_Scatter_Data.csv')
df

```
```
            x         y  label_pred
0   -0.095714 -0.406647           0
1    3.730082  1.836354           1
2    5.760651  2.223426           1
3    0.806121  0.000757           0
4    3.044205  1.601044           1
..        ...       ...         ...
295  0.516852 -0.536252           0
296  2.501448  3.941616           1
297 -0.098418 -0.321477           0
298 -0.359185 -0.716439           0
299 -0.188894 -0.033229           0

[300 rows x 3 columns]
```

```python
group = np.unique(df.label_pred)
markers = ['o', 's']
colors = ["# 00AFBB",  "# FC4E07"]
fig = plt.figure(figsize=(4, 4), dpi=100)
for i in range(0, len(group)):
    temp_df = df[df.label_pred == group[i]]
    plt.scatter(temp_df.x, temp_df.y,
                s=40, linewidths=0.5, edgecolors="k", alpha=0.8,
                marker=markers[i], c=colors[i], label=group[i])
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.legend(title='group', loc='lower right',
           edgecolor='none', facecolor='none')
plt.show()

```
```
<Figure size 400x400 with 1 Axes>
```
