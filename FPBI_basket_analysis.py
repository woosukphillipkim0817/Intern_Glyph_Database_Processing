import os
import pandas as pd

import entry_items
import entries_valid_misc_transactions

#Description: a table which shows which misc items were most commonly purchased along with the products of each brand

#creating table valid_transactions which has all the details for every entry
valid_transactions = pd.merge(entry_items.new_entry_items, entries_valid_misc_transactions.new_entries, on="Entry ID")
valid_transactions.drop("Brand ID_y", inplace=True, axis=1)
valid_transactions.rename(columns={"Brand ID_x": "Brand ID"}, inplace=True)

#finding the most common misc items transacted BY EACH BRAND
valid_transactions_temp = valid_transactions[["Brand ID", "List of Misc Items"]]
misc_items = valid_transactions_temp.explode("List of Misc Items")
misc_items_grouped_by_brand = misc_items.groupby(['Brand ID', 'List of Misc Items']).size().reset_index(name='Count')
misc_items_grouped_by_brand_sorted = misc_items_grouped_by_brand.sort_values(by='Count', ascending=False)

#constructing a basket analysis result table where it displays the top 10 most common misc items for each brand
basket_analysis_result = pd.DataFrame()
for brand_num in range(1, misc_items_grouped_by_brand_sorted["Brand ID"].max() + 1):
    top_10_items_list = misc_items_grouped_by_brand_sorted[misc_items_grouped_by_brand_sorted["Brand ID"] == brand_num].nlargest(10, "Count")["List of Misc Items"].tolist()

    if len(top_10_items_list) < 10: #some brands might not have enough misc items
        # Fill up the list with "NA" if the length of commonly transacted misc items less than 10
        top_10_items_list.extend(["No Significant Data"] * (10 - len(top_10_items_list)))

    basket_analysis_result["Brand " + str(brand_num)] = top_10_items_list

#clean up the syntax of the data
basket_analysis_result = basket_analysis_result.applymap(lambda x: x.title() if isinstance(x, str) else x)

#using Python's built-in OS library download data to local downloads folder
# desired_file_name = "basket_analysis_test.csv"
# desired_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', desired_file_name)
# basket_analysis_result.to_csv(desired_file_path, index=False)


#Progress Checker
# print(misc_items_grouped_by_brand_sorted)
print(basket_analysis_result)