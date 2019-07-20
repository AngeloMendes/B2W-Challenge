from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df_sales = pd.read_csv('../datasets/sales.csv', delimiter=',')
df_comp_prices = pd.read_csv('../datasets/comp_prices.csv', delimiter=',')


def chart_sales_prod(prod_id):
    total_sales = df_sales.PROD_ID.value_counts()[prod_id]
    df = df_sales.groupby(['PROD_ID', 'DATE_ORDER'])['PROD_ID'].count()
    df[prod_id].plot(title='Sales ' + str(prod_id) +
                     ' \n  Total sales = '+str(total_sales))

    plt.ylabel('num sales')
    plt.xlabel('date')
    plt.show()


# for prod_id in df_sales.PROD_ID.unique():
#    chart_sales_prod(prod_id)



def find_competitor_prices(competitor, pay_type, prod_id, date_min='2015-01-31 20:10:14', date_max='2015-10-14 20:11:30'):
    """
    Plot a figure with all prices in a date interval, group by prod_id and competitor
    
    Parameters/exmples:
        competitor (str): 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'...
        date_min (timestamp): '2015-01-31 20:10:14' (default values)
        date_max (timestamp): '2015-10-14 20:11:30' (default values)
        pay_type (int): 1 or 2
        prod_id (str): 'P1', 'P2', 'P3', 'P4', 'P5', 'P6'...
    """

    df = df_comp_prices.groupby(['DATE_EXTRACTION', 'PROD_ID', 'COMPETITOR', 'COMPETITOR_PRICE', 'PAY_TYPE']).filter(
        lambda x: (x['COMPETITOR'] == competitor).any())

    # df=df[df.PROD_ID=='P6'].sort('DATE_EXTRACTION')
    df = df[df.PROD_ID == prod_id]
    df = df[df.PAY_TYPE == pay_type]
    df = df[(df['DATE_EXTRACTION'] > date_min) &
            (df['DATE_EXTRACTION'] < date_max)]

    # print(df)
    if df.empty:
        print("No register in this condictions, change the parameters")
        return None

    df.plot(x='DATE_EXTRACTION', y='COMPETITOR_PRICE', title='PRICE VARIATION \n PROD_ID: '+str(prod_id)+' COMPETITOR: '+str(competitor))    
    plt.ylabel('competitor price')
    plt.xlabel('date')
    plt.show()

#find_competitor_prices(competitor='C4',pay_type=1,prod_id='P4')

def find_outliers(competitor, prod_id):
    print('Max values\n')
    max = df_comp_prices.groupby(['PROD_ID', 'COMPETITOR', 'COMPETITOR_PRICE']).filter(
            lambda x: (x['COMPETITOR'] == competitor).max())
    max = max[max.PROD_ID == prod_id]
    max = max.sort_values('COMPETITOR_PRICE', ascending=False)
    print(max.COMPETITOR_PRICE.head(5))
    
    print('Min values\n')
    min = df_comp_prices.groupby(['PROD_ID', 'COMPETITOR', 'COMPETITOR_PRICE', 'PAY_TYPE']).filter(
            lambda x: (x['COMPETITOR'] == competitor).min())
    min = min[min.PROD_ID == prod_id]
    min = min.sort_values('COMPETITOR_PRICE', ascending=True)
    print(min.COMPETITOR_PRICE.head(5))
    print('------------------------------------------------------\n\n')


#for prod_id in df_sales.PROD_ID.unique():
#    find_outliers('C6',prod_id)
