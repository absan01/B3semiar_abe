import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./iris.csv')

plt.figure()
plt.title("all_data")
plt.xlabel("petal_length")
plt.ylabel("freq")
plt.grid(True)
plt.hist(df["petal_length"], bins=40, range=(0, 8))
plt.savefig('./kadai2_1.jpg')
plt.close('all')