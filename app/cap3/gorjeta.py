import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.describe())

fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips['total_bill'], bins=10)
axes1.set_title('Histogram of total bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total bill')
plt.show()