import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('Iris.csv')
sb.heatmap(data.corr(numeric_only=True),annot=True,cmap="summer")
plt.show()