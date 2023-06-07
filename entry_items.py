import pandas as pd

#creates new_entry_items which has the details of the valid products that have been transacted (taken from the parent transactions table)

import products

#cleaning entry_items table (a semi-processed table that shows the details of the products that have been transacted)
entry_items = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\entry_items.csv') #initial database snapshot data
# entry_items = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\cognitive_ai_2022_data\entry_items.csv') #2022 data
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
#Expected Result: ['Entry Item ID', 'Entry ID', 'Product ID', 'Quantity', 'Item Price', 'Brand ID', 'Brand Name', 'Product Name', 'Product Code', 'Disabled']