import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv

# Load the matchups dataset
# reader = csv.reader(open("matchupsDatabase.csv", encoding="utf8"),delimiter=",")
# print(reader)
# reader.readline()
# x = list(reader)
# data = np.array(x).astype("float")
# print(data)

#Using pandas
input_file = "matchupsDatabase.csv"

df = pd.read_csv(input_file,header=0)
orignal_headers = list(df.columns.values)
df = df._get_numeric_data()
numeric_headers = list(df.columns.values)
numpy_array = df.as_matrix()
numeric_headers.reverse()
reverse_df = df[numeric_headers]
print(reverse_df)

# reverse_df.to_excel(maFile.xls")

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
print(diabetes)


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('Prediction: ', diabetes_y_pred)
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()