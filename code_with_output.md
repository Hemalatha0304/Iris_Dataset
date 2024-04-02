```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
```

```
df = pd.read_csv("iris.csv")

df.columns = [
    "Sepal_Length",
    "Sepal_Width",
    "Petal_Length",
    "Petal_Width",
    "Species"
]
print(df)
```

```
     Sepal_Length  Sepal_Width  Petal_Length  Petal_Width         Species                                                                                            
0             4.9          3.0           1.4          0.2     Iris-setosa                                                                                            
1             4.7          3.2           1.3          0.2     Iris-setosa                                                                                            
2             4.6          3.1           1.5          0.2     Iris-setosa                                                                                            
3             5.0          3.6           1.4          0.2     Iris-setosa                                                                                            
4             5.4          3.9           1.7          0.4     Iris-setosa                                                                                            
..            ...          ...           ...          ...             ...                                                                                            
144           6.7          3.0           5.2          2.3  Iris-virginica                                                                                            
145           6.3          2.5           5.0          1.9  Iris-virginica                                                                                            
146           6.5          3.0           5.2          2.0  Iris-virginica                                                                                            
147           6.2          3.4           5.4          2.3  Iris-virginica                                                                                            
148           5.9          3.0           5.1          1.8  Iris-virginica
```

```
data = df.drop_duplicates(subset="Species")
print(data)
print(df["Species"].value_counts())
```

```
[149 rows x 5 columns]                                                                                                                                               
    Sepal_Length  Sepal_Width  Petal_Length  Petal_Width          Species                                                                                            
0            4.9          3.0           1.4          0.2      Iris-setosa                                                                                            
49           7.0          3.2           4.7          1.4  Iris-versicolor                                                                                            
99           6.3          3.3           6.0          2.5   Iris-virginica                                                                                            
Species                                                                                                                                                              
Iris-versicolor    50                                                                                                                                                
Iris-virginica     50                                                                                                                                                
Iris-setosa        49                                                                                                                                                
Name: count, dtype: int64   
```

```
sns.scatterplot(x='Sepal_Length', y='Sepal_Width', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()
```
![scatter plot1](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/1.SepalLength_SepalWidth_scatterplot.jpeg)

```
sns.scatterplot(x='Petal_Length', y='Petal_Width', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()
```
![scatter plot2](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/2.PetalLength_PetalWidth_scatterplot.jpeg)

```
# Pair-Plot
sns.pairplot(df,hue="Species")
plt.show()
```
![pair plot](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/3.PairPlot_Species.jpeg)

```
# Histograms
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].set_title("Sepal Length")
axes[0, 0].hist(df['Sepal_Length'], bins=7)

axes[0, 1].set_title("Sepal Width")
axes[0, 1].hist(df['Sepal_Width'], bins=5)

axes[1, 0].set_title("Petal Length")
axes[1, 0].hist(df['Petal_Length'], bins=6)

axes[1, 1].set_title("Petal Width")
axes[1, 1].hist(df['Petal_Width'], bins=6)

plt.show()
```
![Histograms](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/4.Histogram.jpeg)

```
# Histograms with Distplot Plot
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "Sepal_Length").add_legend()

plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "Sepal_Width").add_legend()

plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "Petal_Length").add_legend()

plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.distplot, "Petal_Width").add_legend()

plt.show()
```
![hist with dist1](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/5.Histogram_with_distplot1.jpeg)

![hist with dist2](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/6.Histogram_with_distplot2.jpeg)

![hist with dist3](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/7.Histogram_with_distplot3.jpeg)

![hist with dist4](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/8.Histogram_with_distplot4.jpeg)

```
# Box Plots
def graph(y):
    sns.boxplot(x="Species", y=y, data=df)

plt.figure(figsize=(10, 10))

plt.subplot(221)
graph('Sepal_Length')

plt.subplot(222)
graph('Sepal_Width')

plt.subplot(223)
graph('Petal_Length')

plt.subplot(224)
graph('Petal_Width')

plt.show()
```
![boxplot](https://github.com/Hemalatha0304/Iris_Dataset/blob/main/Outputs/9.BoxPlot.jpeg)