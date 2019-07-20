import pandas as pd
import numpy as np
from sklearn import preprocessing

import matplotlib
from matplotlib import pyplot as plt

df_sales = pd.read_csv('../datasets/sales.csv', delimiter=',')
df_comp_prices = pd.read_csv('../datasets/comp_prices.csv', delimiter=',')


def find_nan_values(df_name, df):
    print(df_name)
    for column in df.columns:
        nan_instances = df[df[column].isnull()]
        size = len(nan_instances)
        print("nones instances in column "+str(column)+":  "+str(size))
        if size:
            print(nan_instances)
    print('-------------------\n')


def normalize_price(df_name, column):
    print(df_name)
    min_max_scaler = preprocessing.MinMaxScaler()
    column_normalized = min_max_scaler.fit_transform(column)
    print(column_normalized)
    print('-------------------\n')

print('Find by nones values')
find_nan_values('COMP_PRICES', df_comp_prices)
find_nan_values('SALES', df_sales)

print('Normilze numeric values')
normalize_price('COMP_PRICES', np.asarray(
    df_comp_prices.COMPETITOR_PRICE).reshape(-1, 1))
normalize_price('SALES', np.asarray(df_sales.REVENUE).reshape(-1, 1))
