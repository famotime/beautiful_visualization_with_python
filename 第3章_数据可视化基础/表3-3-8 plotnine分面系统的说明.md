# 表3-3-8 plotnine分面系统的说明

```python
from plotnine import *
from plotnine.data import mpg


mpg
```
```
    manufacturer   model  displ  year  cyl       trans drv  cty  hwy fl  \
0           audi      a4    1.8  1999    4    auto(l5)   f   18   29  p   
1           audi      a4    1.8  1999    4  manual(m5)   f   21   29  p   
2           audi      a4    2.0  2008    4  manual(m6)   f   20   31  p   
3           audi      a4    2.0  2008    4    auto(av)   f   21   30  p   
4           audi      a4    2.8  1999    6    auto(l5)   f   16   26  p   
..           ...     ...    ...   ...  ...         ...  ..  ...  ... ..   
229   volkswagen  passat    2.0  2008    4    auto(s6)   f   19   28  p   
230   volkswagen  passat    2.0  2008    4  manual(m6)   f   21   29  p   
231   volkswagen  passat    2.8  1999    6    auto(l5)   f   16   26  p   
232   volkswagen  passat    2.8  1999    6  manual(m5)   f   18   26  p   
233   volkswagen  passat    3.6  2008    6    auto(s6)   f   17   26  p   

       class  
0    compact  
1    compact  
2    compact  
3    compact  
4    compact  
..       ...  
229  midsize  
230  midsize  
231  midsize  
232  midsize  
233  midsize  

[234 rows x 11 columns]
```

```python
t = (ggplot(mpg, aes('cty', 'hwy', fill='fl'))
     + geom_point(size=3, stroke=0.3, alpha=0.8, show_legend=False)
     + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
     )

t1 = (t + facet_grid('.~ fl')
      + theme_matplotlib()
      + theme(text=element_text(size=12, colour="black"),
              strip_text=element_text(size=15, colour="black"),
              strip_background=element_rect(color='k'),
              aspect_ratio=1.3,
              dpi=100,
              figure_size=(10, 10)))
print(t1)
# t1.save('分面1.pdf')

```
```
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:136: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:137: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead

```

```python
t2 = (t + facet_grid('year ~ .')
      + theme_matplotlib()
      + theme(text=element_text(size=12, colour="black"),
              strip_text=element_text(size=15, colour="black"),
              strip_background=element_rect(color='k'),
              aspect_ratio=0.5,
              dpi=100,
              figure_size=(4, 4)))
print(t2)
# t2.save('分面2.pdf')

```
```
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:136: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:137: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead

```

```python
t3 = (t + facet_grid('year ~ fl')
      + theme_matplotlib()
      + theme(text=element_text(size=12, colour="black"),
              strip_text=element_text(size=15, colour="black"),
              strip_background=element_rect(color='k'),
              aspect_ratio=1,
              dpi=100,
              figure_size=(9, 9)))
print(t3)
# t3.save('分面3.pdf')

```
```
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:136: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:137: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead

```

```python
t4 = (t + facet_wrap('~ fl')
      + theme_matplotlib()
      + theme(text=element_text(size=14, colour="black"),
              strip_text=element_text(size=20, colour="black"),
              strip_background=element_rect(color='k'),
              aspect_ratio=1,
              dpi=100,
              figure_size=(9, 9)))
print(t4)
# t4.save('分面4.pdf')

```
```
<Figure size 900x659.308 with 5 Axes>
```

```python
t5 = (t + facet_grid('drv ~ fl', scales="free")
      + theme_matplotlib()
      + theme(text=element_text(size=12, colour="black"),
              strip_text=element_text(size=15, colour="black"),
              strip_background=element_rect(color='k'),
              aspect_ratio=1,
              dpi=100,
              figure_size=(9, 9)))
print(t5)
# t5.save('分面5.pdf')

```
```
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:136: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead
C:\QMDownload\anaconda\lib\site-packages\plotnine\facets\facet_grid.py:137: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead

```

```python

```
