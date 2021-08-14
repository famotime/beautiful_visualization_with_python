# 表3-3-8 plotnine分面系统的说明

```python
from plotnine import *
from plotnine.data import mpg


t = (ggplot(mpg, aes('cty', 'hwy', fill='fl'))
        + geom_point(size=3, stroke=0.3, alpha=0.8, show_legend=False)
        + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
    )

t1=(t + facet_grid('.~ fl')
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1.3,
        dpi=100,
       figure_size=(10,10)))
print(t1)
# t1.save('分面1.pdf')


t2=(t + facet_grid('year ~ .')
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =0.5,
        dpi=100,
       figure_size=(4,4)))
print(t2)
# t2.save('分面2.pdf')

t3=(t + facet_grid('year ~ fl')
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1,
        dpi=100,
       figure_size=(9,9)))
print(t3)
# t3.save('分面3.pdf')

t4=(t + facet_wrap('~ fl')
+theme_matplotlib()
+ theme(text=element_text(size=14,colour = "black"),
        strip_text=element_text(size=20,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1,
        dpi=100,
       figure_size=(9,9)))
print(t4)
# t4.save('分面4.pdf')


t5=(t + facet_grid('drv ~ fl', scales = "free")
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1,
        dpi=100,
       figure_size=(9,9)))
print(t5)
# t5.save('分面5.pdf')
```
```
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:136: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:137: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead

```

```python

```
