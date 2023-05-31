import pandas as pd

#Description: creates new_products table which shows the details of every product per brand (primarily used this script to join into entry_items)


import brands_stores_branches
#contains branches table merged with stores and brands (although each table exists on its own as well)

#cleaning Products table (details of products across the 4 brands but no Brand ID)
products = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\products.csv')
products.drop("created_at", inplace=True, axis=1)
products.drop("updated_at", inplace=True, axis=1)

#cleaning syntax of data example (a version of this code block used quite often)
products.columns = products.columns.str.title()
for col_num in range(3):
    column_name = products.columns[col_num]
    new_column_name = "Product " + column_name
    products = products.rename(columns={column_name: new_column_name})
products = products.rename(columns=lambda x: x.replace("Id", "ID"))

#extracting brands names from the product names and getting it as a column
four_brand_names = ["PROMIL® FOUR", "PROMIL® ORGANIC", "PROMIL GOLD® FOUR", "BONAKID PRE-SCHOOL ® 3+", "PROMIL® GOLD FOUR"] #last element for bug where name was inconsistent
extracted_brand_names = []
for data_point in products["Product Name"]:
    result = next((s for s in four_brand_names if s in data_point), None)
    extracted_brand_names.append(result)
for index in range(len(extracted_brand_names)): #bug where last product was not named correctly (was named as "PROMIL® GOLD FOUR" when it should be "PROMIL GOLD® FOUR")
    if extracted_brand_names[index] == "PROMIL® GOLD FOUR":
        extracted_brand_names[index] = "PROMIL GOLD® FOUR"
products["Brand Name"] = extracted_brand_names

#putting Brand ID into a new products table
new_products = pd.merge(brands_stores_branches.brands, products, on="Brand Name") #automatically sorted by Brand ID



#Progress Checker
# print(new_products.columns)
# Expected Outcome: ['Brand ID', 'Brand Name', 'Product ID', 'Product Name', 'Product Code', 'Disabled']
# print(new_products)