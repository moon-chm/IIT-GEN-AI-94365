import pandas as pd
#print read csv file
df=pd.read_csv('products.csv')
#Print each row in a clean format
print(df)
#Total number of rows
print("Total number of rows: ",len(df))
#Total number of products priced above 500
count=0
for price in df['price']:
    if price>500:
        count+=1
print("Number of products priced above 500: ",count)
#Average price of all products
average_price=df['price'].mean()
print("Average price of all products: ",average_price)
#List all products belonging to a specific category (user input)
category=input("Enter a category to filter products: ")
filtered_products=df[df['category'].str.lower()==category.lower()]  
print("Products in category",category,":")
print(filtered_products)
#Total quantity of all items in stock
total_quantity=df['quantity'].sum()
print("Total quantity of all items in stock: ",total_quantity)
