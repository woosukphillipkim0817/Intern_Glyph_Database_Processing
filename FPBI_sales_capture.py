import os
import pandas as pd

import entry_items
#new_entry_items columns: ['Entry Item ID', 'Entry ID', 'Product ID', 'Quantity', 'Item Price', 'Brand ID', 'Brand Name', 'Product Name', 'Product Code', 'Disabled']

#creating a copy of new_entry_items with selected columns in order to complete calculations of sales
temp_new_entry_items = entry_items.new_entry_items[["Product ID", "Brand ID", "Quantity", "Item Price"]]

#creating a table with the total sales capture for each brand
num_months_covered_by_data = 3 #the snapshot only covers Oct-Dec of 2022 (change this number to match how many months the analyzed dataset covers)
temp_sales_capture = temp_new_entry_items[['Brand ID', 'Quantity', 'Item Price']]
temp_sales_capture["Revenue"] = temp_sales_capture["Quantity"] * temp_sales_capture["Item Price"]

sales_capture_per_brand = temp_sales_capture.groupby("Brand ID")["Revenue"].sum()
sales_capture_table = sales_capture_per_brand.reset_index() #a table where each row has the Brand ID and then the total revenue for that brand's items
total_sales_capture_across_brands = int(sales_capture_table["Revenue"].sum().round())
average_sales_capture_per_month_across_brands = total_sales_capture_across_brands // num_months_covered_by_data
sales_capture_table["Percent of Total Sales"] = (sales_capture_table["Revenue"] / total_sales_capture_across_brands * 100).round().astype(int)

#using Python's built-in OS library download data to local downloads folder
# desired_file_name = "sales_capture_table_test.csv"
# desired_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', desired_file_name)
# sales_capture_table.to_csv(desired_file_path, index=False)

#Progress Checker
print(sales_capture_table)