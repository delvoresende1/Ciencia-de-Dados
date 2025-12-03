import pandas as pd

df = pd.read_csv('/home/delvo/dados/arquivos/gapminder.tsv', sep='\t')

#print(df.head(n=10))
print(df.groupby('year')['lifeExp'].mean())

multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var)

flat = multi_group_var.reset_index()
print(flat.head(15))

print(df.groupby('continent')['country'].nunique())

print(df.groupby('continent')['country'].value_counts())

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

import matplotlib.pyplot as plt

(df
     .groupby(['year'])
     [['lifeExp']]
     .mean()
     .plot()
)
plt.show()

