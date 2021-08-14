# -*- coding: utf-8 -*-
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import cm#,colors
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

# %%
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
