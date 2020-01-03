import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def linear_model(X_train, y_train):
    lm=LinearRegression()
    lm.fit(X_train,y_train)
    lm_predictions=lm.predict(X_train)
    return lm_predictions

def evaluate(actual, model):
    MSE = mean_squared_error(actual, model)
    SSE = MSE*len(actual)
    RMSE = sqrt(MSE)
    r2 = r2_score(actual, model)
    return MSE, SSE, RMSE, r2 

def linear_model_and_eval(X_train, y_train):
    # extract numeric values
    X_train_num = X_train.select_dtypes(np.number)

    # predicted values & add to y_train
    y_train["predict"] = linear_model(X_train_num, y_train)

    #evaluate 
    mse, sse, rmse, r2  = evaluate(y_train['geek_rating'], y_train.predict)
    return mse, sse, rmse, r2