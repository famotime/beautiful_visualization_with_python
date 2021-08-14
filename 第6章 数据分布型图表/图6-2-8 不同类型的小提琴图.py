# -*- coding: utf-8 -*-
# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *


df = pd.read_csv('Distribution_Data.csv')
df['class'] = pd.Categorical(df['class'], categories=[
                             "n", "s", "k", "mm"], ordered=True)
df

# %%
# -------------------------------------------(a)小提琴图-------------------------------------------
violin_plot = (ggplot(df, aes(x='class', y="value", fill="class"))
               + geom_violin(show_legend=False)
               + geom_boxplot(fill="white", width=0.1, show_legend=False)
               + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
               + theme_matplotlib()
               + theme(  # legend_position='none',
    aspect_ratio=1.05,
    dpi=100,
    figure_size=(4, 4)))
print(violin_plot)
# violin_plot.save("violin_plot.pdf")

# %%
# -------------------------------------------(b)小提琴图-------------------------------------------

violin_plot = (ggplot(df, aes(x='class', y="value", fill="class"))
               + geom_violin(show_legend=False)
               + geom_jitter(fill="black", width=0.3, size=1,
                             stroke=0.1, show_legend=False)
               + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
               + theme_matplotlib()
               + theme(  # legend_position='none',
    aspect_ratio=1.05,
    dpi=100,
    figure_size=(4, 4)))
print(violin_plot)
# violin_plot.save("violin_plot2.pdf")
