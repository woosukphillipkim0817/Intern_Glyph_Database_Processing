import pandas as pd

#cleaning transactions table
user_rewards = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\user_rewards.csv')
user_rewards.drop("created_at", inplace=True, axis=1)
user_rewards.drop("updated_at", inplace=True, axis=1)

user_rewards.columns = user_rewards.columns.str.title()
user_rewards = user_rewards.rename(columns=lambda x: x.replace("_", " "))
user_rewards = user_rewards.rename(columns=lambda x: x.replace("Id", "ID"))
user_rewards.rename(columns={"ID": "User Reward ID"}, inplace=True)

#progress checker
print(user_rewards.columns)