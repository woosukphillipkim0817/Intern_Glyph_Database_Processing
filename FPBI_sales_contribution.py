import os
import pandas as pd

import brands_stores_branches #will only use new_stores_table

import entry_items
# new_entry_items columns: ['Entry Item ID', 'Entry ID', 'Product ID', 'Quantity', 'Item Price',
# 'Brand ID', 'Brand Name', 'Product Name', 'Product Code', 'Disabled']

import entries_valid_misc_transactions
# new_entries columns: ['Entry ID', 'Transaction ID', 'User ID', 'Brand ID', 'Store ID', 'Payment Method', 'Total', 'Paid Amount', 'Change',
#   'Remarks', 'List of Misc Items']

#creating a temporary table that contains the store details of each valid transaction
temp_entries = entries_valid_misc_transactions.new_entries[["Entry ID", "User ID", "Store ID"]]
temp_entry_items = entry_items.new_entry_items[["Entry ID", "Product ID", "Quantity", "Item Price"]]
temp_stores_details = brands_stores_branches.new_stores_table[["Store ID", "Store Name"]]

temp_valid_transactions = pd.merge(temp_entries, temp_entry_items, on="Entry ID")
temp_valid_transactions_with_store_details = pd.merge(temp_valid_transactions, temp_stores_details, on="Store ID")

#adding a column for the revenue of each valid transaction
temp_valid_transactions_with_store_details["Sales"] = temp_valid_transactions_with_store_details["Quantity"] * temp_valid_transactions_with_store_details["Item Price"]

#creating a results table with the sales, unique customers, transaction count, and average customer spend per store
total_sales = temp_valid_transactions_with_store_details['Sales'].sum()
total_unique_customers = temp_valid_transactions_with_store_details['User ID'].nunique()
sales_contribution_by_store = temp_valid_transactions_with_store_details.groupby('Store Name')['Sales'].sum().reset_index()
sales_contribution_by_store["Sales Percentage"] = (sales_contribution_by_store["Sales"] / total_sales * 100).round().astype(int)

unique_customers_per_store_table = temp_valid_transactions_with_store_details.groupby("Store Name")["User ID"].nunique().reset_index()
sales_contribution_by_store["Unique Customers"] = unique_customers_per_store_table["User ID"]
sales_contribution_by_store["Unique Customers Percentage"] = (sales_contribution_by_store["Unique Customers"] / total_unique_customers * 100).round().astype(int)

transactions_per_store = temp_valid_transactions_with_store_details.groupby('Store Name').size().reset_index(name='Number of Transactions')
sales_contribution_by_store["Transaction Count"] = transactions_per_store["Number of Transactions"]

sales_contribution_by_store["Average Customer Spend"] = sales_contribution_by_store["Sales"] // sales_contribution_by_store["Transaction Count"]

sales_contribution_by_store.sort_values('Sales Percentage', ascending=False, inplace=True)

#using Python's built-in OS library download data to local downloads folder
# desired_file_name = "sales_contribution_by_store_test.csv"
# desired_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', desired_file_name)
# sales_contribution_by_store.to_csv(desired_file_path, index=False)

#Progress Checker
# print(sales_contribution_by_store)