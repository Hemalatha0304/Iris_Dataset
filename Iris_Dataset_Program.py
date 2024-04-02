# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Reading the CSV file
df = pd.read_csv("iris.csv")

# Correcting column names
df.columns = [
    "Sepal_Length",
    "Sepal_Width",
    "Petal_Length",
    "Petal_Width",
    "Species"
]

data = df.drop_duplicates(subset="Species")
print(data)
print(df["Species"].value_counts())

# Scatterplot comparing Sepal Length and Sepal Width
sns.scatterplot(x='Sepal_Length', y='Sepal_Width', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Scatterplot comparing Petal Length and Petal Width
sns.scatterplot(x='Petal_Length', y='Petal_Width', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Pair-Plot
sns.pairplot(df,hue="Species")
plt.show()

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

# Handling Outliers
sns.boxplot(x='Sepal_Width', data=df)
plt.show()

Q1 = np.percentile(df['Sepal_Width'], 25, interpolation='midpoint')
Q3 = np.percentile(df['Sepal_Width'], 75, interpolation='midpoint')
IQR = Q3 - Q1
print("Old Shape: ", df.shape)
upper = np.where(df['Sepal_Width'] >= (Q3 + 1.5 * IQR))
lower = np.where(df['Sepal_Width'] <= (Q1 - 1.5 * IQR))
df.drop(upper[0], inplace=True)
df.drop(lower[0], inplace=True)
print("New Shape: ", df.shape)
sns.boxplot(x='Sepal_Width', data=df)
plt.show()