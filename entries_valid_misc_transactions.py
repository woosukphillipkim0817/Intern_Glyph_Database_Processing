import pandas as pd

#creates new_entries table which shows the details of each valid transaction including other items bought with the brand's items (so same number of rows as entry_items)


#cleaning entries table (table of completed valid transactions)
entries = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\entries.csv') #initial database snapshot data
# entries = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\cognitive_ai_2022_data\entries.csv') #2022 data
entries.drop("created_at", inplace=True, axis=1)
entries.drop("updated_at", inplace=True, axis=1)

entries.columns = entries.columns.str.title()
entries = entries.rename(columns=lambda x: x.replace("_", " "))
entries = entries.rename(columns=lambda x: x.replace("Id", "ID"))
entries = entries.rename(columns=lambda x: x.replace("Hp", "HP"))
entries.rename(columns={"ID": "Entry ID"}, inplace=True)

#cleaning misc_entry_items table (table of items that are not a part of the brands bought in the transaction)
misc_entry_items = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\misc_entry_items.csv') #initial database snapshot data
# misc_entry_items = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\cognitive_ai_2022_data\misc_entry_items.csv') #2022 data
misc_entry_items.drop("created_at", inplace=True, axis=1)
misc_entry_items.drop("updated_at", inplace=True, axis=1)

misc_entry_items.columns = misc_entry_items.columns.str.title()
misc_entry_items = misc_entry_items.rename(columns=lambda x: x.replace("_", " "))
misc_entry_items = misc_entry_items.rename(columns=lambda x: x.replace("Id", "ID"))

#new table grouping the misc_entry_items by transaction and including a column with a list of strings of the misc_items names
unique_ids = misc_entry_items["Transaction ID"].unique()
grouped_items = misc_entry_items.groupby("Transaction ID")["Item Name"].apply(list).reset_index()
temp_table_of_grouped_misc_entry_items = pd.DataFrame({"Transaction ID": grouped_items["Transaction ID"], "List of Misc Items": grouped_items["Item Name"]})

#adding this list of misc_items into the entries table
new_entries = pd.merge(entries, temp_table_of_grouped_misc_entry_items, on="Transaction ID")
new_entries.drop("HP Card Number", inplace=True, axis=1) #columns regarding HP are just remnants from previous data management systems
new_entries.drop("HP Points Earned", inplace=True, axis=1)
new_entries.drop("HP Load Balance", inplace=True, axis=1)
new_entries.drop("HP Points Balance", inplace=True, axis=1)

#Progress Checker
# print(new_entries.columns)
# Expected Outcome: ['Entry ID', 'Transaction ID', 'User ID', 'Brand ID', 'Store ID',
#        'Payment Method', 'Total', 'Paid Amount', 'Change', 'Remarks',
#        'List of Misc Items']