# -*- coding: utf-8 -*-
# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image


def getImage(path, zoom=0.07):
    img = Image.open(path)
    img.thumbnail((512, 512), Image.ANTIALIAS)  # resizes image in-place
    return OffsetImage(img, zoom=zoom)


paths = np.arange(1, 11, 1)

N = 10
x = np.sort(np.random.randn(N))+5
y = np.sort(np.random.randn(N))+5

fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
ax.scatter(x, y)

plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)
plt.yticks(ticks=np.arange(5, 8, 1))

artists = []
for x0, y0, path in zip(x, y, paths):
    ab = AnnotationBbox(getImage('图片散点图数据集/'+str(path) +
                                 '.jpg'), (x0, y0), frameon=True)
    artists.append(ax.add_artist(ab))

# fig.savefig("图片散点图.pdf")
