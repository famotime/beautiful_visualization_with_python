# 图4-1-2 排序调整后的柱形图系列_plotnine

```python
import pandas as pd
import numpy as np
from plotnine import *
# from plotnine.data import *
# import matplotlib.pyplot as plt

```
## a)单数剧系列柱形图

```python
mydata = pd.DataFrame({'Cut': ["Fair", "Good", "Very Good", "Premium", "Ideal"],
                       'Price': [4300, 3800, 3950, 4700, 3500]})

Sort_data = mydata.sort_values(by='Price', ascending=False)

# Sort_data['Cut']=Sort_data['Cut'].astype("category",categories=Sort_data['Cut'],ordered=True)

Sort_data['Cut'] = pd.Categorical(
    Sort_data['Cut'], ordered=True, categories=Sort_data['Cut'])

base_plot = (ggplot(Sort_data, aes('Cut', 'Price'))
             + geom_bar(stat="identity", width=0.8, colour="black",
                        size=0.25, fill="# FC4E07", alpha=1)
             + ylim(0, 6000)
             + theme(
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    aspect_ratio=1.15,
    figure_size=(6.5, 6.5),
    dpi=50
)
)
print(base_plot)
# base_plot.save('Bar_Plot.pdf')

```
```
<Figure size 325x376.177 with 1 Axes>
```
## b)双数剧系列柱形图

```python
df = pd.read_csv('MultiColumn_Data.csv')
df = df.sort_values(by='1996', ascending=False)

mydata = pd.melt(df, id_vars='Catergory')

display(df, mydata)

```
```
           Catergory  1996  1997
0  Temporary\nStream  7.67  5.84
1  Permanent\nStream  4.02  6.45
2               Lake  3.95  6.76
```

```python
mydata['Catergory'] = pd.Categorical(
    mydata['Catergory'], ordered=True, categories=df['Catergory'])


base_plot = (ggplot(mydata, aes(x='Catergory', y='value', fill='variable'))
             + geom_bar(stat="identity", color="black",
                        position='dodge', width=0.7, size=0.25)
             + scale_fill_manual(values=["# 00AFBB", "# FC4E07", "# E7B800"])
             + ylim(0, 10)
             + theme(legend_title=element_text(size=18, face="plain", color="black"),
                     legend_text=element_text(
                         size=16, face="plain", color="black"),
                     axis_title=element_text(
                         size=18, face="plain", color="black"),
                     axis_text=element_text(
                         size=16, face="plain", color="black"),
                     legend_background=element_blank(),
                     legend_position=(0.75, 0.80),
                     aspect_ratio=1.15,
                     figure_size=(6.5, 6.5),
                     dpi=50
                     )
             )
print(base_plot)
# base_plot.save('Bar_Plot2.pdf')

```
```
<Figure size 325x376.177 with 1 Axes>
```
## c)堆积柱形图

```python
df = pd.read_csv('StackedColumn_Data.csv')
df

```
```
     Clarity    I1   SI2   SI1   VS2   VS1    S2    S1    IF
0       Fair   150   400   390   300   130   100   100   150
1       Good  1200  1100  1700   900   790  1300  1200  1100
2  Very_Good  1300  2300  3300  1900  1800  1900  1700  1300
3    Premium  2800  2900  3500  2800  3000  1800  1600  1280
4      Ideal  2000  2700  4200  3300  4200  2700  2100  1300
```

```python
Sum_df = df.iloc[:, 1:].apply(
    lambda x: x.sum(), axis=0).sort_values(ascending=False)

meanRow_df = df.iloc[:, 1:].apply(lambda x: x.mean(), axis=1)

Sing_df = df['Clarity'][meanRow_df.sort_values(ascending=True).index]

mydata = pd.melt(df, id_vars='Clarity')

mydata['variable'] = pd.Categorical(mydata['variable'], categories=Sum_df.index, ordered=True)
mydata['Clarity'] = pd.Categorical(mydata['Clarity'], categories=Sing_df, ordered=True)

base_plot = (ggplot(mydata, aes(x='variable', y='value', fill='Clarity'))
             + geom_bar(stat="identity", color="black",
                        position='stack', width=0.7, size=0.25)
             + scale_fill_brewer(palette="YlOrRd")
             + ylim(0, 15000)
             + theme(
    legend_title=element_text(size=18, face="plain", color="black"),
    legend_text=element_text(size=16, face="plain", color="black"),
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    legend_background=element_blank(),
    legend_position=(0.75, 0.75),
    aspect_ratio=1.15,
    figure_size=(6.5, 6.5),
    dpi=50
)
)
print(base_plot)
# base_plot.save('Bar_Plot3.pdf')

```
```
<Figure size 325x376.177 with 1 Axes>
```
## d)百分比堆积柱形图

```python
df = pd.read_csv('StackedColumn_Data.csv')

SumCol_df = df.iloc[:, 1:].apply(lambda x: x.sum(), axis=0)

df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x/SumCol_df, axis=1)

meanRow_df = df.iloc[:, 1:].apply(lambda x: x.mean(), axis=1)

Per_df = df.iloc[meanRow_df.idxmax(), 1:].sort_values(ascending=False)

Sing_df = df['Clarity'][meanRow_df.sort_values(ascending=True).index]

mydata = pd.melt(df, id_vars='Clarity')
mydata['Clarity'] = pd.Categorical(mydata['Clarity'], categories=Sing_df, ordered=True)
mydata['variable'] = pd.Categorical(mydata['variable'], categories=Per_df.index, ordered=True)

base_plot = (ggplot(mydata, aes(x='variable', y='value', fill='Clarity'))
             + geom_bar(stat="identity", color="black",
                        position='fill', width=0.7, size=0.25)
             + scale_fill_brewer(palette="GnBu")
             # +ylim(0, 10)
             + theme(
    # text=element_text(size=15,face="plain",color="black"),
    legend_title=element_text(size=18, face="plain", color="black"),
    legend_text=element_text(size=16, face="plain", color="black"),
    axis_title=element_text(size=18, face="plain", color="black"),
    axis_text=element_text(size=16, face="plain", color="black"),
    aspect_ratio=1.15,
    figure_size=(6.5, 6.5),
    dpi=50
)
)
print(base_plot)
# base_plot.save('Bar_Plot4.pdf')

```
```
<Figure size 325x376.177 with 1 Axes>
```
