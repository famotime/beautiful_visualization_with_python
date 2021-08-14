# -*- coding: utf-8 -*-
# %%
from scipy import interpolate
import math
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *


df = pd.read_csv('Facting_Data.csv')
df

# %%
# ------------------------------------------(a)-----------------------------------------------
df_melt = pd.melt(df, id_vars='X_Axis', var_name='var', value_name='value')
df_melt['var'] = pd.Categorical(df_melt['var'], categories=np.unique(df_melt['var'])[::-1], ordered=True)

base_plot = (ggplot(df_melt, aes('X_Axis', 'value', fill='var')) +
             geom_area(color="black", size=0.25) +
             facet_grid('var~.') +
             scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl') +
             theme(aspect_ratio=0.1,
                   dpi=100,
                   figure_size=(5, 0.5)))
print(base_plot)

# %%
# ------------------------------------------(b)--------------------------------

mydata = pd.DataFrame(columns=['x', 'y', 'var'])

list_var = np.unique(df_melt['var'])
N = 300
for i in list_var:
    x = df.loc[:, 'X_Axis']
    y = df.loc[:, i]
    f = interpolate.interp1d(x, y)  # , kind='slinear')#kind='linear',

    x_new = np.linspace(np.min(x), np.max(x), N)
    y_new = f(x_new)
    mydata = mydata.append(pd.DataFrame(
        {'x': x_new, 'y': y_new, 'var': np.repeat(i, N)}))

mydata['var'] = pd.Categorical(mydata['var'], categories=np.unique(df_melt['var'])[::-1], ordered=True)

base_plot = (ggplot(mydata, aes('x', 'y', group='var')) +
             geom_bar(aes(fill='y'), color='none', size=0.5, stat="identity") +
             geom_line(color="black", size=0.5) +
             scale_fill_cmap(name='Spectral_r') +
             facet_grid('var~.') +
             theme(aspect_ratio=0.1,
                   dpi=100,
                   figure_size=(5, 0.5)))
print(base_plot)
