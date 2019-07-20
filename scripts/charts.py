from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
"""
graficos interessantes:
    sales
        1- numero de vendas de cada produto
        2- venda por data
    comp_prices
        1- filtrar por competidor_produto
        2- filtrar por comp_prod_data
        3- variacao de preco de cada produto por fornecedor ordenado por data (variacao de preco no dia)
"""

df_sales = pd.read_csv('../datasets/sales.csv', delimiter=',')
df_comp_prices = pd.read_csv('../datasets/comp_prices.csv', delimiter=',')

def chart_sales_prod(prod_id):
    total_sales = df_sales.PROD_ID.value_counts()[prod_id]
    df = df_sales.groupby(['PROD_ID','DATE_ORDER'])['PROD_ID'].count()
    df[prod_id].plot(title='Sales '+ str(prod_id) +' \n  Total sales = '+str(total_sales))

    plt.ylabel('num sales')
    plt.xlabel('date')
    plt.show()

#for prod_id in df_sales.PROD_ID.unique():
#    chart_sales_prod(prod_id)
"""   comp_prices
        1- filtrar por competidor_produto
        2- filtrar por comp_prod_data
        3- variacao de preco de cada produto por fornecedor ordenado por data (variacao de preco no dia)
"""

df = df_comp_prices.groupby(['DATE_EXTRACTION','PROD_ID','COMPETITOR','COMPETITOR_PRICE']).filter(lambda x: (x['COMPETITOR'] == 'C2').any())

#df=df[df.PROD_ID=='P6'].sort('DATE_EXTRACTION')
df=df[df.PROD_ID=='P6']
df=df[(df['DATE_EXTRACTION'] > '2015-01-30 08:11:38') & (df['DATE_EXTRACTION'] < '2015-01-31 08:11:38')]

#print(df)

df.plot(x='DATE_EXTRACTION', y='COMPETITOR_PRICE')  
plt.show()












