import pandas as pd

import users_redeemables_redemptions

cleaning transactions table
transactions = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\transactions.csv')
transactions.drop("created_at", inplace=True, axis=1)
transactions.drop("updated_at", inplace=True, axis=1)

transactions.columns = transactions.columns.str.title()
transactions = transactions.rename(columns=lambda x: x.replace("_", " "))
transactions = transactions.rename(columns=lambda x: x.replace("Id", "ID"))

Progress Checker
print(transactions.columns)