# 图3-2-2 seaborn带标记的曲线图分面案例

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import cm# ,colors
import seaborn as sns


import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

sns.set_palette("Set1")
sns.set_style("ticks")
sns.set_context(rc={'axes.labelsize': 15, 'legend.fontsize': 13,
                    'xtick.labelsize': 13, 'ytick.labelsize': 13})


df = pd.read_csv("MappingAnalysis_Data.csv")
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
# -------------------------------------------------------------------------------------
sns.set_context("notebook", font_scale=1.5,
                rc={'font.size': 12,
                    'axes.labelsize': 13, 'legend.fontsize': 13,
                    'xtick.labelsize': 12, 'ytick.labelsize': 12})

g = sns.FacetGrid(df, col="variable", hue="variable", height=3,
                  aspect=0.9, gridspec_kws={"wspace": 0.1})
g.map(sns.lineplot, "Time", "value", marker='o', dashes=False,
      markersize=8, markeredgewidth=0.5, markeredgecolor="k",
      linewidth=1)
g.set_xlabels("Time(d)")
g.set_ylabels("value")
plt.xticks(np.linspace(0, 20, 5, endpoint=True))
# 设置纵轴的上下限
plt.yticks(np.linspace(0, 80, 5, endpoint=True))

g.set_titles(row_template='{row_name}', col_template='{col_name}')

# g.savefig("seaborn5.pdf")

```
```
C:\QMDownload\anaconda\lib\site-packages\seaborn\axisgrid.py:382: UserWarning: This figure includes Axes that are not compatible with tight_layout, so results might be incorrect.
  fig.tight_layout()
C:\QMDownload\anaconda\lib\site-packages\seaborn\axisgrid.py:856: UserWarning: This figure includes Axes that are not compatible with tight_layout, so results might be incorrect.
  self.fig.tight_layout()

```
