import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/home/delvo/dados/arquivos/anscombes.csv")
#print(df)
#a biblioteca seaborn carrega o arquivo nativamente
anscombe = sns.load_dataset("anscombe")
#print(anscombe)

dataset_1 = anscombe[anscombe['dataset']=='I']
dataset_2 = anscombe[anscombe['dataset']=='II']
dataset_3 = anscombe[anscombe['dataset']=='III']
dataset_4 = anscombe[anscombe['dataset']=='IV']
""" plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.plot(dataset_2['x'], dataset_2['y'], 'o')
plt.plot(dataset_3['x'], dataset_3['y'], 'o')
plt.plot(dataset_4['x'], dataset_4['y'], 'o') """
#cria toda a figura na qual nossas subplotagens serão inseridas
fig = plt.figure()
#diz à figura como as subplotagens deverão ser dispostas no exemplo
#teremos 2 linhas de plotagens, e cada linha terá 2 plotagens
#a subplotagem tem 2 linhas e 2 colunas, local 1 da plotagem
axes1 = fig.add_subplot(2, 2, 1)
#a subplotagem tem 2 linhas e 2 colunas, local 2 da plotagem
axes2 = fig.add_subplot(2, 2, 2)
#a subplotagem tem 2 linhas e 2 colunas, local 3 da plotagem
axes3 = fig.add_subplot(2, 2, 3)
#a subplotagem tem 2 linhas e 2 colunas, local 4 da plotagem
axes4 = fig.add_subplot(2, 2, 4)

#adiciona uma plotagem em cada um dos eixos criados anteriormente
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

#acrescenta um título para cada plotagem
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

axes1.set_xlabel('x')
axes1.set_ylabel('y')

axes2.set_xlabel('x')
axes2.set_ylabel('y')

axes3.set_xlabel('x')
axes3.set_ylabel('y')

axes4.set_xlabel('x')
axes4.set_ylabel('y')

#adiciona um título para toda a figura
fig.suptitle("Anscombe data")

#usa um layout organizado
fig.tight_layout()
plt.show()