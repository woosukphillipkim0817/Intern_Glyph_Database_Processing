import pandas as pd

import products
#contains new_products table that has details of products

#cleaning entry_items table ()
entry_items = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\entry_items.csv')
entry_items.drop("created_at", inplace=True, axis=1)
entry_items.drop("updated_at", inplace=True, axis=1)

entry_items.columns = entry_items.columns.str.title()
entry_items = entry_items.rename(columns=lambda x: x.replace("_", " "))
entry_items = entry_items.rename(columns=lambda x: x.replace("Id", "ID"))
entry_items.rename(columns={"ID": "Entry Item ID"}, inplace=True)

#making a new entry_items table with products
entry_items_for_merge = entry_items[["Entry Item ID", "Entry ID", "Product ID", "Quantity", "Item Price"]]
new_entry_items = pd.merge(entry_items_for_merge, products.new_products, on="Product ID")


#Progress Checker
# print(new_entry_items.columns)