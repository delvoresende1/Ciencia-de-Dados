import pandas as pd
from collections import OrderedDict
df = pd.read_csv('/home/delvo/dados/arquivos/scientists.csv', sep=',')

cientistas = pd.DataFrame(df)
print(cientistas)
born = cientistas[['Name', 'Born']]
print(born)

scientists = pd.DataFrame(
    data = {'Occupation': ['Chemist', 'Statistician'],
            'Born': ['1920-07-25','1876-06-13' ],
            'Died': ['1958-04-16', '1937-10-16'],
            'Age': [37, 61]
            },
    index=['Rosaline Franklin','William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age'])

print(scientists)

gosset = scientists.loc['William Gosset']
print(gosset)

print(gosset.index)
print(gosset.keys())

ages = scientists['Age']
print(ages)

print('Media de idade', ages.mean())
print('Menor idade', ages.min())
print('Maior idade', ages.max())
print('Desvio padrao', ages.std())

metodos_series = cientistas['Age']

print('Media de idade todos', metodos_series.mean())
print('Menor idade todos', metodos_series.min())
print('Maior idade todos', metodos_series.max())
print('Desvio padrao todos', metodos_series.std())

print(metodos_series.describe())

print('Idade maior que a média:\n', metodos_series[metodos_series > metodos_series.mean()])
print(metodos_series + metodos_series)

print(cientistas[cientistas['Age'] > cientistas['Age'].mean()])