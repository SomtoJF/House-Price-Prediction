#STEP 1: IMPORT NECESSARY LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
boston_dataset = load_boston()
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target
'''
corr_matrix = boston.corr().round(2)
corr_heatmap = sns.heatmap(corr_matrix,cmap='YlGnBu')
plt.show()
'''
from sklearn.linear_model import LinearRegression
model = LinearRegression()
from sklearn.model_selection import train_test_split
X = boston[['RM','LSTAT','CRIM']]
Y = boston['MEDV']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, random_state=1)
model.fit(X_train,Y_train)
Y_test_predicted = model.predict(X_test)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(Y_test, Y_test_predicted))
print(boston['MEDV'].describe())