import pandas as pd


df_sales = pd.read_csv('../datasets/sales.csv', delimiter=',')
df_comp_prices = pd.read_csv('../datasets/comp_prices.csv', delimiter=',')

df_comp_prices['COMPETITOR']=df_comp_prices['COMPETITOR'].astype('category').cat.codes
df_comp_prices['PROD_ID']=df_comp_prices['PROD_ID'].astype('category').cat.codes
df_comp_prices['DATE_EXTRACTION'] = pd.to_datetime(df_comp_prices['DATE_EXTRACTION']).astype(int)/ 10**9

print(df_comp_prices.corr())