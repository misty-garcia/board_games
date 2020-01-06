import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


def linear_model_and_eval(X_train, X_test, y_train, y_test):
    # extract numeric values
    X_train_num = X_train.select_dtypes(np.number)

    # create object and fit
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    train_predict = lm.predict(X_train)
    test_predict = lm.predict(X_test)

    # evaluating the model on train
    rmse_train = sqrt(mean_squared_error(y_train, train_predict))
    r2_train = r2_score(y_train, train_predict)

    # evaluating the model on the test
    # rmse_test = sqrt(mean_squared_error(y_test, test_predict))
    # r2_test = r2_score(y_test, test_predict)

    print("Train set model performance")
    print("RMSE:", rmse_train)
    print("  R2:", r2_train)
    print("")
    # print("Test set model performance") 
    # print("RMSE:", rmse_test)
    # print("  R2:", r2_test)