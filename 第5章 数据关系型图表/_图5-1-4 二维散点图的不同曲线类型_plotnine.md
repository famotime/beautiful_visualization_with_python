# _图5-1-4 二维散点图的不同曲线类型_plotnine

```python
import pandas as pd
import numpy as np
from plotnine import *
import skmisc  # 提供loess smoothing

df = pd.read_csv('Scatter_Data.csv')
df

```

```python
plot_loess = (ggplot(df, aes('x', 'y')) +
              geom_point(fill="black", colour="black", size=3, shape='o') +
              # (f)
              geom_smooth(method='loess', span=0.4, se=True, colour="# 00A5FF", fill="# 00A5FF", alpha=0.2) +
              scale_y_continuous(breaks=np.arange(0, 126, 25)) +
              theme(
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    legend_position="none",
    aspect_ratio=1,
    figure_size=(5, 5),
    dpi=100
)
)

print(plot_loess)

```

```python
plot_lm = (ggplot(df, aes('x', 'y')) +
           geom_point(fill="black", colour="black", size=3, shape='o') +
           geom_smooth(method="lm", se=True, colour="red") +  # (h)
           # geom_smooth(method = 'gam',formula='y ~s(x)')+   # (g)
           # geom_smooth(method = 'loess',span=0.4,se=True,colour="# 00A5FF",fill="# 00A5FF",alpha=0.2)+ # (f)
           scale_y_continuous(breaks=np.arange(0, 126, 25)) +
           theme(
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    legend_position="none",
    aspect_ratio=1,
    figure_size=(5, 5),
    dpi=100
)
)

print(plot_lm)

```

```python
plot_glm = (ggplot(df, aes('x', 'y')) +
            geom_point(fill="black", colour="black", size=3, shape='o') +
            geom_smooth(method="glm", se=True, colour="red") +  # (h)
            # geom_smooth(method = 'gam')+   # (g)
            # geom_smooth(method = 'loess',span=0.4,se=True,colour="# 00A5FF",fill="# 00A5FF",alpha=0.2)+ # (f)
            scale_y_continuous(breaks=np.arange(0, 126, 25)) +
            theme(
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    legend_position="none",
    aspect_ratio=1,
    figure_size=(5, 5),
    dpi=100
)
)

print(plot_glm)

```
