# -*- coding: utf-8 -*-
# %%
import pandas as pd
from plotnine import *


df = pd.read_csv('MultiSeries_Scatter_Data.csv')
df

# %%
base_plot = (ggplot(df, aes('x', 'y', shape='factor(label_pred)', fill='factor(label_pred)')) +
             geom_point(size=4, colour="black", alpha=0.7) +
             scale_shape_manual(values=('s', 'o')) +
             scale_fill_manual(values=("#00AFBB",  "#FC4E07")) +
             labs(x="Axis X", y="Axis Y") +
             scale_y_continuous(limits=(-5, 10)) +
             scale_x_continuous(limits=(-5, 10)) +
             theme(
    # text=element_text(size=15,face="plain",color="black"),
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    aspect_ratio=1,
    figure_size=(5, 5),
    dpi=100
)
)
print(base_plot)
