# 图3-1-3 matplotlib带标记的曲线图绘制案例

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.style.use('default')  # print(plt.style.available)


df = pd.read_csv("MappingAnalysis_Data.csv")

df1 = df[df.variable == '0%(Control)']
df2 = df[df.variable == '1%']
df3 = df[df.variable == '5%']
df4 = df[df.variable == '15%']

# =============================================================================
colors = ['# e41a1c', '# 377eb8', '# 4daf4a', '# 984ea3']
markers = ['o', 's', 'H', 'D']
labels = ["0%(Control)", "1%", "5%", "15%"]
group = ["0%(Control)", "1%", "5%", "15%"]  # np.unique(df.variable)

df

```
```
    Unnamed: 0       Time     variable      value
0            1  -0.049505  0%(Control)   0.000000
1            2   0.891089  0%(Control)   0.803213
2            3   1.881188  0%(Control)   0.803213
3            4   3.019802  0%(Control)   0.803213
4            5   4.108911  0%(Control)   0.401606
..         ...        ...          ...        ...
71          72  14.207921          15%  65.863454
72          73  14.752475          15%  65.461847
73          74  15.940594          15%  65.461847
74          75  17.079208          15%  64.257028
75          76  18.019802          15%  64.257028

[76 rows x 4 columns]
```

```python
# ----------------------------(a)-----------------------------------------------
fig = plt.figure(figsize=(4, 3), dpi=100)

for i in range(0, 4):
    temp_df = df[df.variable == group[i]]
    plt.plot(temp_df.Time, temp_df.value)
# plt.plot(df2.Time, df2.value)
# plt.plot(df3.Time, df3.value)
# plt.plot(df4.Time, df4.value)
plt.show()
# fig.savefig("matplotlib1.pdf")

```
```
<Figure size 400x300 with 1 Axes>
```

```python
# -------------------------------(b)--------------------------------------------
fig = plt.figure(figsize=(4, 3), dpi=100)

for i in range(0, 4):
    plt.plot(df[df.variable == group[i]].Time, df[df.variable == group[i]].value,
             marker=markers[i], markerfacecolor=colors[i], markersize=8, markeredgewidth=0.5,
             color="k", linewidth=0.5, linestyle="-", label=group[i])
# plt.legend(loc='upper left',edgecolor='none',facecolor='none')
plt.show()

# fig.savefig("matplotlib2.pdf")

```
```
<Figure size 400x300 with 1 Axes>
```

```python
# ---------------------------------(c)------------------------------------------
fig = plt.figure(figsize=(4, 3), dpi=100)

plt.plot(df1.Time, df1.value,
         marker=markers[0], markerfacecolor=colors[0], markersize=8, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[0])
plt.plot(df2.Time, df2.value,
         marker=markers[1], markerfacecolor=colors[1], markersize=7, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[1])
plt.plot(df3.Time, df3.value,
         marker=markers[2], markerfacecolor=colors[2], markersize=8, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[2])
plt.plot(df4.Time, df4.value,
         marker=markers[3], markerfacecolor=colors[3], markersize=7, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[3])

plt.xlabel("Time(d)", fontsize=14)
plt.ylabel("value", fontsize=14)

plt.xlim(-1, 20)
plt.ylim(-2, 90)
# 设置横轴记号
plt.xticks(np.linspace(0, 20, 11, endpoint=True), fontsize=10)
# 设置纵轴的上下限
plt.yticks(np.linspace(0, 90, 10, endpoint=True), fontsize=10)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()

# fig.savefig("matplotlib3.pdf")

```
```
<Figure size 400x300 with 1 Axes>
```

```python
# ------------------------------(d)---------------------------------------------
fig = plt.figure(figsize=(4, 3), dpi=100)


plt.plot(df1.Time, df1.value,
         marker=markers[0], markerfacecolor=colors[0], markersize=8, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[0])
plt.plot(df2.Time, df2.value,
         marker=markers[1], markerfacecolor=colors[1], markersize=7, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[1])
plt.plot(df3.Time, df3.value,
         marker=markers[2], markerfacecolor=colors[2], markersize=8, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[2])
plt.plot(df4.Time, df4.value,
         marker=markers[3], markerfacecolor=colors[3], markersize=7, markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-", label=labels[3])

plt.xlabel("Time(d)", fontsize=14)
plt.ylabel("value", fontsize=14)

plt.xlim(-1, 20)
plt.ylim(-2, 90)
# 设置横轴记号
plt.xticks(np.linspace(0, 20, 11, endpoint=True), fontsize=10)
# 设置纵轴的上下限
plt.yticks(np.linspace(0, 90, 10, endpoint=True), fontsize=10)

plt.legend(loc='upper left', edgecolor='none', facecolor='none')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()

# fig.savefig("matplotlib4.pdf")

```
```
<Figure size 400x300 with 1 Axes>
```
