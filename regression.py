import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv
import coremltools

# Load the matchups dataset
#Using pandas
input_file = "matchupsDatabase.csv"
train_file = "trainDatabase.csv"

df = pd.read_csv(input_file,header=0)
train = pd.read_csv(train_file,header=0)

orignal_headers = list(df.columns.values)
df = df._get_numeric_data()
numeric_headers = list(df.columns.values)
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
lr = lin_regr.fit(df,train["WinPercentage"])

print("1714 - 2-0")
print(lr.predict([[1714,0]]))#Retorna a probabilidade deste resultado acontece
print("69 - 1-1")
print(lr.predict([[69,1]]))#Retorna a probabilidade deste resultado acontece
print("123 2-1")
print(lr.predict([[123,0.666666667]]))#Retorna a probabilidade deste resultado acontece
print("114 - 2-0")
print(lr.predict([[114,1]]))#Retorna a probabilidade deste resultado acontece

coreml_model = coremltools.converters.sklearn.convert(lr,["matchup","winPercentage"])

coreml_model.save("decksMatchup.mlmodel)
