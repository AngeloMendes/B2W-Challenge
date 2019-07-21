import pandas as pd
from apyori import apriori

df_comp_prices = pd.read_csv('../datasets/comp_prices.csv', delimiter=',')
df_comp_prices = df_comp_prices[df_comp_prices.PROD_ID == 'P9']

records = []
for i in range(0, len(df_comp_prices)):
    records.append([str(df_comp_prices.values[i, j]) for j in range(0, 5)])

association_rules = apriori(records, min_support=0.035, min_confidence=0.6, min_lift=3, min_length=3)
association_results = list(association_rules)

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

print(len(association_results))
