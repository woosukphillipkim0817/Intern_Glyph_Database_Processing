import pandas as pd

#cleaning entries table (table of completed valid transactions)
entries = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\entries.csv')
entries.drop("created_at", inplace=True, axis=1)
entries.drop("updated_at", inplace=True, axis=1)

entries.columns = entries.columns.str.title()
entries = entries.rename(columns=lambda x: x.replace("_", " "))
entries = entries.rename(columns=lambda x: x.replace("Id", "ID"))
entries = entries.rename(columns=lambda x: x.replace("Hp", "HP"))
entries.rename(columns={"ID": "Entry ID"}, inplace=True)

#cleaning misc_entry_items table (table of items that are not a part of the brands bought in the transaction)
misc_entry_items = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\misc_entry_items.csv')
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

#Progress Checker
print(new_entries)