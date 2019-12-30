import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

import statsmodels.api as sm
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LassoCV, LinearRegression

import warnings
warnings.filterwarnings("ignore")

# Write a function, select_kbest_freg() that takes X_train, y_train and k as input and returns a list of the top k features.

def select_kbest_freg(X_train, y_train, k):
    f_selector = SelectKBest(f_regression, k=k).fit(X_train, y_train)
    f_support = f_selector.get_support()
    f_feature = X_train.loc[:,f_support].columns.tolist()
    return f_feature


# Write a function, ols_backware_elimination() that takes X_train and y_train (scaled) as input and returns selected features based on the ols backwards elimination method.
def ols_backware_elimination(X_train, y_train):
    ols_model = sm.OLS(y_train, X_train)
    fit = ols_model.fit()

    cols = list(X_train.columns)
    while (len(cols)>0):
        X_1 = X_train[cols]
        model = sm.OLS(y_train,X_1).fit()
        p = model.pvalues
        pmax = max(p)
        feature_with_p_max = p.idxmax()
        if(pmax>0.05):
            cols.remove(feature_with_p_max)
        else:
            break
    return cols

# Write a function, lasso_cv_coef() that takes X_train and y_train as input and returns the coefficients for each feature, along with a plot of the features and their weights.
def lasso_cv_coef(X_train, y_train):
    reg = LassoCV(cv=5)
    reg.fit(X_train, y_train)

    coef = pd.Series(reg.coef_, index = X_train.columns)
    imp_coef = coef.sort_values()

    # plot = imp_coef.plot(kind = "barh")
    plot = sns.barplot(x=X_train.columns, y=reg.coef_)

    return coef, plot

# Write 3 functions, the first computes the number of optimum features (n) using rfe, the second takes n as input and returns the top n features, and the third takes the list of the top n features as input and returns a new X_train and X_test dataframe with those top features , recursive_feature_elimination() that computes the optimum number of features (n) and returns the top n features.
def num_optimal_features(X_train, y_train):
    number_of_features_list = range(1,len(X_train.columns)+1)
    high_score=0
    number_of_features=0           
    # score_list =[]

    for n in number_of_features_list:
        model = LinearRegression()
        rfe = RFE(model,n)
        train_rfe = rfe.fit_transform(X_train,y_train)
        model.fit(train_rfe,y_train)
        score = model.score(train_rfe,y_train)
        # score_list.append(score)
        if(score>high_score):
            high_score = score
            number_of_features = n
    return number_of_features

def optimal_features(n, X_train, y_train):
    cols = list(X_train.columns)

    model = LinearRegression()
    rfe = RFE(model, n)

    train_rfe = rfe.fit_transform(X_train,y_train)  
    model.fit(train_rfe,y_train)

    temp = pd.Series(rfe.support_,index = cols)
    selected_features_rfe = temp[temp==True].index

    return selected_features_rfe

def df_with_optimal_features(df, features):
    optimal_features_df = df[features]
    return optimal_features_df

def recursive_feature_elimination(X_train, y_train):
    return optimal_features(num_optimal_features(X_train, y_train), X_train, y_train)
