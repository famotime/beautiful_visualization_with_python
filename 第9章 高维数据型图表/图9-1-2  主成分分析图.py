# -*- coding: utf-8 -*-
# %%
import pandas as pd
import numpy as np
from plotnine import *
from sklearn.decomposition import PCA
from sklearn import datasets


# -----------------------------------(a) 四维数据的iris数据集-----------------------------------------------------
iris = datasets.load_iris()

X_reduced = PCA(n_components=2).fit_transform(iris.data)
target = pd.Categorical.from_codes(iris.target, iris.target_names)

df = pd.DataFrame(
    dict(pca1=X_reduced[:, 0], pca2=X_reduced[:, 1], target=target))
df

# %%
base_plot2 = (ggplot(df, aes('pca1', 'pca2', fill='factor(target)')) +
              geom_point(alpha=1, size=3, shape='o', colour='k') +
              # ç»å¶éæåº¦ä¸º0.2 çæ£ç¹å¾
              stat_ellipse(geom="polygon", level=0.95, alpha=0.2) +
              # ç»å¶æ¤­åæ å®ä¸åç±»å«
              scale_fill_manual(values=("#00AFBB", "#E7B800", "#FC4E07"), name='group') +
              theme(
    axis_title=element_text(size=15, face="plain", color="black"),
    axis_text=element_text(size=13, face="plain", color="black"),
    legend_text=element_text(size=11, face="plain", color="black"),
    aspect_ratio=1,
    figure_size=(5, 5),
    dpi=100
)
)
print(base_plot2)

# %%
# ---------------------------------  (b) 93维数据的train数据集------------------------------------------------------
df = pd.read_csv('Tsne_Data.csv')
df = df.set_index('id')

num_rows_sample = 5000

df = df.sample(n=num_rows_sample)

X_reduced = PCA(n_components=2).fit_transform(df.iloc[:, :-1])

df = pd.DataFrame(
    dict(pca1=X_reduced[:, 0], pca2=X_reduced[:, 1], target=df.iloc[:, -1]))
df

# %%
base_plot2 = (ggplot(df, aes('pca1', 'pca2', fill='target', color='target')) +
              geom_point(alpha=1, size=2, shape='o', colour='k', stroke=0.1) +
              stat_ellipse(geom="polygon", level=0.95, alpha=0.2) +
              xlim(-15, 25) +
              ylim(-15, 25) +
              scale_fill_hue(s=0.99, l=0.65, h=0.0417, color_space='husl') +
              scale_color_hue(s=0.99, l=0.65, h=0.0417, color_space='husl') +
              theme(
    # text=element_text(size=15,face="plain",color="black"),
    axis_title=element_text(size=15, face="plain", color="black"),
    axis_text=element_text(size=13, face="plain", color="black"),
    aspect_ratio=1,
    figure_size=(5, 5),
    dpi=100
)
)
print(base_plot2)
