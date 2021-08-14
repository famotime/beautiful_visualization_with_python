# 表3-3-7 ggplot与geom对象之间的关系情况

```python
import pandas as pd
import numpy as np
from plotnine import *
# from plotnine.data import *
import matplotlib.pyplot as plt
import matplotlib
# plt.rc('font',family='Times New Roman')
matplotlib.rcParams['font.family'] = 'Times New Roman'

N = 20
df1 = pd.DataFrame(dict(x=np.sort(np.random.randn(N)),
                        y=np.sort(np.random.randn(N))))
df2 = pd.DataFrame(dict(x=df1.x+0.3*np.sort(np.random.randn(N)),
                        y=df1.y+0.1*np.sort(np.random.randn(N))))

df1, df2

```
```
(           x         y
 0  -1.507629 -1.442141
 1  -1.334182 -1.280366
 2  -1.238369 -1.258982
 3  -1.180590 -1.074935
 4  -0.623618 -0.970617
 5  -0.388316 -0.730772
 6  -0.373213 -0.570436
 7  -0.287661 -0.254354
 8  -0.241706 -0.252112
 9  -0.152707 -0.230556
 10 -0.100028 -0.113224
 11  0.232475 -0.057443
 12  0.234262  0.018978
 13  0.311307  0.228950
 14  0.362275  0.236029
 15  0.463545  0.312297
 16  0.534884  1.023454
 17  0.627090  1.446735
 18  0.710476  1.476893
 19  2.324395  1.976391,
            x         y
 0  -2.124176 -1.682503
 1  -1.822366 -1.422829
 2  -1.700088 -1.392324
 3  -1.632982 -1.190879
 4  -0.928308 -1.072175
 5  -0.598115 -0.804867
 6  -0.559025 -0.630186
 7  -0.450137 -0.313356
 8  -0.346547 -0.308328
 9  -0.237417 -0.283477
 10 -0.181115 -0.132636
 11  0.248017 -0.031356
 12  0.268724  0.048986
 13  0.357269  0.273250
 14  0.532967  0.300663
 15  0.792510  0.379348
 16  0.876319  1.127240
 17  0.983745  1.568149
 18  1.137485  1.636700
 19  2.910300  2.138322)
```

```python
p1 = (ggplot(df1, aes('x', 'y', colour='x+y')) +
      geom_line(size=1) +
      geom_point(shape='o', size=5) +
      scale_color_distiller(name="Line", palette="Blues") +
      guides(color=guide_colorbar(title="Point\nLine")) +
      theme(text=element_text(size=12, colour="black"),
            aspect_ratio=1.25,
            dpi=100,
            figure_size=(4, 4)))  # shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)

# p1.save("plotnine_Advance1.pdf")

```
```
<Figure size 400x503.247 with 1 Axes>
```

```python
p1 = (ggplot(df1, aes('x', 'y')) +
      geom_line(aes(colour='x+y'), size=1) +
      geom_point(aes(fill='x+y'), color="black", shape='o', size=5) +
      scale_fill_distiller(name="Point", palette="YlOrRd") +
      scale_color_distiller(name="Line", palette="Blues") +
      theme(text=element_text(size=12, colour="black"),
            aspect_ratio=1.25,
            dpi=100,
            figure_size=(4, 4)))  # shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
# p1.save("plotnine_Advance2.pdf")

```
```
<Figure size 400x503.247 with 1 Axes>
```

```python
p1 = (ggplot() +
      geom_line(aes('x', 'y', colour='x+y'), df1, size=1) +
      geom_point(aes('x', 'y', fill='x+y'), df2, color="black", shape='o', size=5) +
      scale_fill_distiller(name="Point", palette="YlOrRd") +
      scale_color_distiller(name="Line", palette="Blues") +
      theme(text=element_text(size=12, colour="black"),
            aspect_ratio=1.25,
            dpi=100,
            figure_size=(4, 4)))  # shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
# p1.save("plotnine_Advance3.pdf")

```
```
<Figure size 400x503.247 with 1 Axes>
```
