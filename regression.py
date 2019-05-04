import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv

# Load the matchups dataset
#Using pandas
input_file = "matchupsDatabase.csv"

df = pd.read_csv(input_file,header=0)
orignal_headers = list(df.columns.values)
df = df._get_numeric_data()
numeric_headers = list(df.columns.values)
numpy_array = df.as_matrix()
df.pop('Deck')
df.pop('OpponentDeck')
df.pop('Games')
df.pop('Victories')
df.pop('Losses')
x = np.split(df,2)

# print("what")
# print(x[0])
# print(x[1])

# Create linear regression object
lin_regr = linear_model.LinearRegression()
y_train = lin_regr.fit(x[0],x[1])

print(y_train.predict([[1714,1]]))#Retorna a probabilidade deste resultado acontecer

# print(y_train.predict([[12,0.3333]]))
# ypred = lin_regr.predict(y)
# print(ypred)

# Plot outputs
# plt.scatter(testSet, diabetes_y_test,  color='black')
# plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

# plt.xticks(())
# plt.yticks(())

# plt.show()