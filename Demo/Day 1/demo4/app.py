import pandas as pd
import pandasql as ps
path="products.csv"
df = pd.read_csv(path)
print(df.head())
query="""
SELECT Category, AVG(Price) as Average_Price from data group by Category"""
result=ps.sqldf(query, {'data':df})
print(result)