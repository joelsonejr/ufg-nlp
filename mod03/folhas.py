import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Trazendo o dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

# gráfico de violino
plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='petal_length', palette='husl', data=iris)
plt.title('Distribuição do Comprimento das Pétalas por Espécie')
plt.xlabel('Espécie')
plt.ylabel('Comprimento das Pétalas')
plt.show()

# gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal_length', palette='husl', data=iris, estimator=np.mean)
plt.title('Média do Comprimento das Pétalas por Espécie')
plt.xlabel('Espécie')
plt.ylabel('Comprimento Médio das Pétalas')
plt.show()

# calculando valores médios
mean_petal_length = iris.groupby('species')['petal_length'].mean()
max_species = mean_petal_length.idxmax()
print(f"A espécie com maior valor médio de comprimento da pétala é: {max_species}")

# encontrando outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='petal_length', palette='husl', data=iris)
plt.title('Distribuição do Comprimento das Pétalas por Espécie')
plt.xlabel('Espécie')
plt.ylabel('Comprimento das Pétalas')
plt.show()

# Estatísticas descritivas para identificar outliers
desc_stats = iris.groupby('species')['petal_length'].describe()
print(desc_stats)

# As espécies com mais outliers são as Setosa e Versicolor.