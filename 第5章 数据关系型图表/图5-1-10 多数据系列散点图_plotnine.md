# 图5-1-10 多数据系列散点图_plotnine

```python
import pandas as pd
from plotnine import *


df = pd.read_csv('MultiSeries_Scatter_Data.csv')
df

```
```
            x         y  label_pred
0   -0.095714 -0.406647           0
1    3.730082  1.836354           1
2    5.760651  2.223426           1
3    0.806121  0.000757           0
4    3.044205  1.601044           1
..        ...       ...         ...
295  0.516852 -0.536252           0
296  2.501448  3.941616           1
297 -0.098418 -0.321477           0
298 -0.359185 -0.716439           0
299 -0.188894 -0.033229           0

[300 rows x 3 columns]
```

```python
base_plot = (ggplot(df, aes('x', 'y', shape='factor(label_pred)', fill='factor(label_pred)')) +
             geom_point(size=4, colour="black", alpha=0.7) +
             scale_shape_manual(values=('s', 'o')) +
             scale_fill_manual(values=("# 00AFBB",  "# FC4E07")) +
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

```
```
<Figure size 500x503.247 with 1 Axes>
```
