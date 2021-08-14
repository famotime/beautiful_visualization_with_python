# -*- coding: utf-8 -*-
# %%
from pandas.plotting import radviz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('iris.csv')
df

# %%
angle = np.arange(360)/180*3.14159
x = np.cos(angle)
y = np.sin(angle)

fig = plt.figure(figsize=(3.5, 3.5), dpi=100)
ax = radviz(df, 'variety', color=['#FC0000', '#F0AC02', '#009E88'],
            edgecolors='k', marker='o', s=34, linewidths=1)
plt.plot(x, y, color='gray')
plt.axis('off')
plt.legend(loc="center", bbox_to_anchor=(1.1, 0, 0, 0.4),
           edgecolor='none', facecolor='none', title='Group')
