# -*- coding: utf-8 -*-
# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from matplotlib.pyplot import figure, show, rc
plt.rcParams["patch.force_edgecolor"] = True


df = pd.DataFrame(dict(categories=['var1', 'var2', 'var3', 'var4', 'var5'], group_A=[
                  38.0, 29, 8, 7, 28], group_B=[1.5, 10, 39, 31, 15]))
N = df.shape[0]
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

fig = figure(figsize=(4, 4), dpi=90)
ax = fig.add_axes([0.1, 0.1, 0.6, 0.6], polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)
plt.xticks(angles[:-1], df['categories'], color="black", size=12)
plt.ylim(0, 45)
plt.yticks(np.arange(10, 50, 10), color="black", size=12,
           verticalalignment='center', horizontalalignment='right')
plt.grid(which='major', axis="x", linestyle='-',
         linewidth='0.5', color='gray', alpha=0.5)
plt.grid(which='major', axis="y", linestyle='-',
         linewidth='0.5', color='gray', alpha=0.5)

values = df['group_A'].values.flatten().tolist()
values += values[:1]
ax.fill(angles, values, '#7FBC41', alpha=0.3)
ax.plot(angles, values, marker='o', markerfacecolor='#7FBC41',
        markersize=8, color='k', linewidth=0.25, label="group A")

values = df['group_B'].values.flatten().tolist()
values += values[:1]
ax.fill(angles, values, '#C51B7D', alpha=0.3)
ax.plot(angles, values, marker='o', markerfacecolor='#C51B7D',
        markersize=8, color='k', linewidth=0.25, label="group B")
plt.legend(loc="center", bbox_to_anchor=(1.25, 0, 0, 1))
