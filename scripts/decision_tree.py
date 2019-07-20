import pandas as pd
from sklearn import tree
import pydotplus

from IPython.display import Image

df_sales = pd.read_csv('../datasets/sales.csv', delimiter=',')
df_comp_prices = pd.read_csv('../datasets/comp_prices.csv', delimiter=',')


clf = tree.DecisionTreeClassifier(max_leaf_nodes=10)
df_comp_prices['DATE_EXTRACTION'] = pd.to_datetime(df_comp_prices['DATE_EXTRACTION']).astype(int) / 10 ** 9
df_comp_prices['PROD_ID'] = df_comp_prices['PROD_ID'].astype('category').cat.codes
df_comp_prices=df_comp_prices[df_comp_prices.PROD_ID==1]

class_names = df_comp_prices.COMPETITOR.unique()
feature_names = ['PROD_ID', 'DATE_EXTRACTION', 'COMPETITOR_PRICE', 'PAY_TYPE']

df_comp_prices['COMPETITOR'] = df_comp_prices['COMPETITOR'].astype('category').cat.codes

clf = clf.fit(df_comp_prices[['PROD_ID', 'DATE_EXTRACTION', 'COMPETITOR_PRICE', 'PAY_TYPE']],
              df_comp_prices['COMPETITOR'])


dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_names, class_names=class_names,
                                filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
graph.write_png("../analysis/decision_tree.png")
