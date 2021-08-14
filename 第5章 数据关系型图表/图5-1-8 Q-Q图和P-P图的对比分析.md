# 图5-1-8 Q-Q图和P-P图的对比分析

```python
import numpy as np
import pandas as pd
from plotnine import *


df=pd.DataFrame(dict(x=np.random.normal(loc=10,scale=1,size=250)))

base_plot=(ggplot(df, aes(sample = 'x'))+
  geom_qq(shape='o',fill="none")+
  geom_qq_line()+
   theme(
       # text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       aspect_ratio =1.05,
       figure_size = (5,5),
       dpi = 100
       )
  )
print(base_plot)

```
```
<Figure size 500x528.409 with 1 Axes>
```

```python

```
