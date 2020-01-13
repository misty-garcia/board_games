import numpy as np
import pandas as pd

from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


def linear_model_and_eval(X_train, y_train):
    # extract numeric values
    X_train_num = X_train.select_dtypes(np.number)

    # create object and fit
    lm = LinearRegression()
    lm.fit(X_train_num, y_train)

    # transform object
    train_predict = lm.predict(X_train_num)

    # evaluating the model on train
    rmse_train = sqrt(mean_squared_error(y_train, train_predict))
    r2_train = r2_score(y_train, train_predict)

    print("Train set model performance")
    print("RMSE:", rmse_train)
    print("  R2:", r2_train)
    print("")

    return lm

def test_model_and_eval(lm, X_test, y_test):
    # extract numeric values
    X_test_num = X_test.select_dtypes(np.number)

    # transform object
    test_predict = lm.predict(X_test_num)

    # evaluating the model on test
    rmse_test = sqrt(mean_squared_error(y_test, test_predict))
    r2_test = r2_score(y_test, test_predict)

    print("Test set model performance")
    print("RMSE:", rmse_test)
    print("  R2:", r2_test)
    print("")
