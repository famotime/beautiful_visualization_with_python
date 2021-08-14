# -*- coding: utf-8 -*-
# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *


df = pd.read_csv('Boxplot_Sort_Data.csv')
df

# %%
box_plot = (ggplot(df, aes(x='class', y="value", fill="class"))
            + geom_boxplot(show_legend=False)
            + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
            + theme_matplotlib()
            + theme(  # legend_position='none',
    text=element_text(size=12, colour="black"),
    aspect_ratio=1.05,
    dpi=100,
    figure_size=(4, 4)))
print(box_plot)
# box_plot.save("box_plot_sort1.pdf")

# %%
df_group = df.groupby(df['class'], as_index=False).median()
df_group = df_group.sort_values(by="value", ascending=False)

df['class'] = pd.Categorical(df['class'], categories=df_group['class'].astype(str), ordered=True)

box_plot = (ggplot(df, aes(x='class', y="value", fill="class"))
            + geom_boxplot(show_legend=False)
            + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
            + theme_matplotlib()
            + theme(  # legend_position='none',
    text=element_text(size=12, colour="black"),
    aspect_ratio=1.05,
    dpi=100,
    figure_size=(4, 4)))
print(box_plot)
# box_plot.save("box_plot_sort2.pdf")
