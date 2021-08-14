# 图5-1-11 气泡图系列_plotnine

```python
import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import mtcars


mtcars

```
```
                   name   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  \
0             Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1   
1         Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1   
2            Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1   
3        Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0   
4     Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0   
5               Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0   
6            Duster 360  14.3    8  360.0  245  3.21  3.570  15.84   0   0   
7             Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0   
8              Merc 230  22.8    4  140.8   95  3.92  3.150  22.90   1   0   
9              Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0   
10            Merc 280C  17.8    6  167.6  123  3.92  3.440  18.90   1   0   
11           Merc 450SE  16.4    8  275.8  180  3.07  4.070  17.40   0   0   
12           Merc 450SL  17.3    8  275.8  180  3.07  3.730  17.60   0   0   
13          Merc 450SLC  15.2    8  275.8  180  3.07  3.780  18.00   0   0   
14   Cadillac Fleetwood  10.4    8  472.0  205  2.93  5.250  17.98   0   0   
15  Lincoln Continental  10.4    8  460.0  215  3.00  5.424  17.82   0   0   
16    Chrysler Imperial  14.7    8  440.0  230  3.23  5.345  17.42   0   0   
17             Fiat 128  32.4    4   78.7   66  4.08  2.200  19.47   1   1   
18          Honda Civic  30.4    4   75.7   52  4.93  1.615  18.52   1   1   
19       Toyota Corolla  33.9    4   71.1   65  4.22  1.835  19.90   1   1   
20        Toyota Corona  21.5    4  120.1   97  3.70  2.465  20.01   1   0   
21     Dodge Challenger  15.5    8  318.0  150  2.76  3.520  16.87   0   0   
22          AMC Javelin  15.2    8  304.0  150  3.15  3.435  17.30   0   0   
23           Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0   
24     Pontiac Firebird  19.2    8  400.0  175  3.08  3.845  17.05   0   0   
25            Fiat X1-9  27.3    4   79.0   66  4.08  1.935  18.90   1   1   
26        Porsche 914-2  26.0    4  120.3   91  4.43  2.140  16.70   0   1   
27         Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1   
28       Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1   
29         Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1   
30        Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1   
31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1   

    gear  carb  
0      4     4  
1      4     4  
2      4     1  
3      3     1  
4      3     2  
5      3     1  
6      3     4  
7      4     2  
8      4     2  
9      4     4  
10     4     4  
11     3     3  
12     3     3  
13     3     3  
14     3     4  
15     3     4  
16     3     4  
17     4     1  
18     4     2  
19     4     1  
20     3     1  
21     3     2  
22     3     2  
23     3     4  
24     3     2  
25     4     1  
26     5     2  
27     5     2  
28     5     4  
29     5     6  
30     5     8  
31     4     2  
```
## (c) 带数据标签的气泡图

```python
base_plot = (ggplot(mtcars, aes(x='wt', y='mpg')) +
             geom_point(aes(size='disp', fill='disp'), shape='o', colour="black", alpha=0.8) +
             # 绘制气泡图，颜色填充和面积大小都映射到“disp”
             scale_fill_gradient2(low="# 377EB8", high="# E41A1C",
                                  limits=(0, np.max(mtcars.disp)),
                                  midpoint=np.mean(mtcars.disp)) +  # 设置填充颜色映射主题(Colormap)
             scale_size_area(max_size=12) +  # 设置显示的气泡图气泡最大面积
             # 添加数据标签disp”
             geom_text(label=mtcars.disp, nudge_x=0.3, nudge_y=0.3) +
             theme(
    # text=element_text(size=15,face="plain",color="black"),
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    aspect_ratio=1.2,
    figure_size=(5, 5),
    dpi=100
)
)
print(base_plot)

```
```
<Figure size 500x603.896 with 1 Axes>
```
##  (d) 方块状的气泡图

```python
base_plot = (ggplot(mtcars, aes(x='wt', y='mpg')) +
             geom_point(aes(size='disp', fill='disp'), shape='s', colour="black", alpha=0.8) +
             # 绘制气泡图，颜色填充和面积大小都映射到“disp”
             scale_fill_gradient2(low="# 377EB8", high="# E41A1C",
                                  limits=(0, np.max(mtcars.disp)),
                                  midpoint=np.mean(mtcars.disp)) +  # 设置填充颜色映射主题(Colormap)
             scale_size_area(max_size=12) +  # 设置显示的气泡图气泡最大面积
             # geom_text(label = mtcars.disp,nudge_x =0.3,nudge_y =0.3)+ # 添加数据标签disp”
             theme(
    # text=element_text(size=15,face="plain",color="black"),
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    aspect_ratio=1.2,
    figure_size=(5, 5),
    dpi=100
)
)
print(base_plot)

```
```
<Figure size 500x603.896 with 1 Axes>
```
