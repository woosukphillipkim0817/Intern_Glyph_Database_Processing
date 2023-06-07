import pandas as pd

#Description: creates new_branches_table which shows the details of each branch (the branch's parent store and brand)

#cleaning Brands table
brands = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\brands.csv')
brands.drop("created_at", inplace=True, axis=1)
brands.drop("updated_at", inplace=True, axis=1)
brands.rename(columns={"name": "Brand Name"}, inplace=True)
brands.rename(columns={"id": "Brand ID"}, inplace=True)

#putting brand names into stores table and cleaning
stores = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\stores.csv')
stores.columns = stores.columns.str.title()
stores.rename(columns={"Brand_Id": "Brand ID"}, inplace=True)
new_stores_table = pd.merge(brands, stores, on="Brand ID") #NOTE: this table is in order of brand ID
new_stores_table.rename(columns={"Id": "Store ID"}, inplace=True)
new_stores_table.rename(columns={"Name": "Store Name"}, inplace=True)
new_stores_table.rename(columns={"Altername": "Alternate Store Name"}, inplace=True)
new_stores_table.drop("Created_At", inplace=True, axis=1)
new_stores_table.drop("Updated_At", inplace=True, axis=1)
new_stores_table.drop("Region", inplace=True, axis=1)
new_stores_table.drop("Province", inplace=True, axis=1)
new_stores_table.drop("Address", inplace=True, axis=1)
new_stores_table.drop("Altername2", inplace=True, axis=1)
new_stores_table.drop("Altername3", inplace=True, axis=1)
new_stores_table.drop("Disabled", inplace=True, axis=1)
new_stores_table = new_stores_table.rename(columns=lambda x: x.replace("_", " "))

#cleaning branches table
branches = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\branches.csv')
branches.drop("brand_id", inplace=True, axis=1)
branches.drop("store_group", inplace=True, axis=1)
branches.drop("created_at", inplace=True, axis=1)
branches.drop("updated_at", inplace=True, axis=1)
branches.columns = branches.columns.str.title()
branches.rename(columns={"Id": "Branch ID"}, inplace=True)
branches.rename(columns={"Name": "Branch Name"}, inplace=True)
branches.rename(columns={"Store_Id": "Store ID"}, inplace=True)

#merging branches tables with the updated stores table
new_branches_table = pd.merge(new_stores_table, branches, on="Store ID")
for col in new_branches_table.columns:
    if new_branches_table[col].dtype == "object":
        new_branches_table[col] = new_branches_table[col].str.title().str.replace("Sm", "SM") #change title to upper for all caps

#Progress Checker
# print(new_branches_table)