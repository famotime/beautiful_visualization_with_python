# -*- coding: utf-8 -*-
# %%
from plotnine.data import mtcars
import matplotlib.pyplot as plt

mtcars

# %%
x = mtcars['wt']
y = mtcars['mpg']
size = mtcars['disp']
fill = mtcars['disp']

fig, ax = plt.subplots(figsize=(5, 4))
scatter = ax.scatter(x, y, c=fill, s=size, linewidths=0.5,
                     edgecolors="k", cmap='RdYlBu_r')


cbar = plt.colorbar(scatter)
cbar.set_label('disp')

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=5)
ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
