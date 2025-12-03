import pandas as pd

df = pd.read_csv('/home/delvo/dados/arquivos/gapminder.tsv', sep='\t')
#saida 5 linhas inicias (começa em 0)
print(df.head(5))

#<class 'pandas.core.frame.DataFrame'>
print(type(df))

#número de linhas e colunas do dataframe shape é um atributo, não é função logo não tem ()
print(df.shape)

#mostra as colunas e o tipo do objeto dataframe dtype=object
print(df.columns)

#obtem o dtype de cada coluna
print(df.dtypes)

#mais informações sobre os dados
print(df.info())

country_df = df['country']
#mostra as 5 primeiras linhas da coluna country
print(country_df.head())

print(country_df.tail())

#especificando várias colunas pelo nome
subset = df[['country', 'continent', 'year']]
print(subset.head())
print(subset.tail())
print(subset)

print(df.loc[1703])

print(df.loc[0])

#print(df.loc[-1])

number_of_rows = df.shape[0]
last_row_index = number_of_rows -1
print(df.loc[last_row_index])

print(df.tail(n=1))

#varias linhas
print(df.loc[[0, 99, 999]])
print(df.iloc[[0, 99, 999]])

small_range = list(range(5))
print(small_range)

subset = df.iloc[:, small_range]
print(subset.head())