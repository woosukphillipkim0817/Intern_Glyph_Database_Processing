import pandas as pd
import re

#Description: creates new_redemptions_table which shows every redeemable that has been transacted is detailed with the details of the redeemable and the user's information

import brands_stores_branches
#contains branches table merged with stores and brands (although each table exists on its own as well)

#cleaning Redeemables table (this details the types of products customers can redeem)
redeemables = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\redeemables.csv')
redeemables.drop("created_at", inplace=True, axis=1)
redeemables.drop("updated_at", inplace=True, axis=1)
redeemables.drop("image_url", inplace=True, axis=1)
redeemables.drop("brand_id", inplace=True, axis=1) #only null data
redeemables.drop("source_product_id", inplace=True, axis=1) #only null data

#cleaning syntax of data example (a version of this code block used quite often)
redeemables.columns = redeemables.columns.str.title()
redeemables = redeemables.rename(columns=lambda x: x.replace("_", " "))
redeemables = redeemables.rename(columns=lambda x: x.replace("Id", "ID"))
redeemables.rename(columns={"ID": "Redeemable ID"}, inplace=True)
redeemables.rename(columns={"Item Name": "Redeemable Name"}, inplace=True)

#creating new column in Redeemables table that has the PHP value of the redeemable
def extract_number_as_string(input_string):
    pattern = r'\d+'  # Regular expression pattern to match one or more digits
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, input_string)
    if matches:
        return matches[0]  # Return the first match as a string
    else:
        return None  # Return None if no match is found
redeemables["PHP Value of Redeemable"] = redeemables["Redeemable Name"].apply(lambda x: extract_number_as_string(x))

#cleaning Redemptions table (history of which redeemables customers used)
redemptions = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\redemptions.csv')
redemptions.drop("created_at", inplace=True, axis=1)
redemptions.drop("updated_at", inplace=True, axis=1)
redemptions.drop("extra_info", inplace=True, axis=1)
redemptions.columns = redemptions.columns.str.title()
redemptions = redemptions.rename(columns=lambda x: x.replace("_", " "))
redemptions = redemptions.rename(columns=lambda x: x.replace("Id", "ID"))
redemptions.rename(columns={"ID": "Redemption (Transaction) ID"}, inplace=True)

#putting brand names into redemptions table
new_redemptions = pd.merge(brands_stores_branches.brands, redemptions, on="Brand ID")

#adding data from a copy of Redeemables table onto new Redemptions table
redeemables_subtable_for_redemptions = redeemables[["Redeemable ID", "Redeemable Name", "Required Points", "Disabled", "PHP Value of Redeemable"]]
new_redemptions = pd.merge(redeemables_subtable_for_redemptions, new_redemptions, on="Redeemable ID") #automatically sorted by Redeemable ID

#add user details into redemptions table
users = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\users.csv')

users.columns = users.columns.str.title()
users = users.rename(columns=lambda x: x.replace("_", " "))
users = users.rename(columns=lambda x: x.replace("Id", "ID"))
for col_num in range(11): #range is how many columns (from the first one) to change the name of
    column_name = users.columns[col_num]
    new_column_name = "User " + column_name
    users = users.rename(columns={column_name: new_column_name})

selected_columns_from_users_table = ["User ID", "User Name", "User Mobile Number", "User Email"]
copy_of_users_table_with_select_columns_for_redemptions_merge = users[selected_columns_from_users_table]
new_redemptions = pd.merge(new_redemptions, copy_of_users_table_with_select_columns_for_redemptions_merge, on="User ID")

#Progress Checker
# print(new_redemptions.columns)
# Expected Outcome: ['Redeemable ID', 'Redeemable Name', 'Required Points', 'Disabled',
#        'PHP Value of Redeemable', 'Brand ID', 'Brand Name',
#        'Redemption (Transaction) ID', 'User ID', 'Coupon ID', 'User Name',
#        'User Mobile Number', 'User Email']

# print(len(new_redemptions))
# Expected Outcome: 158