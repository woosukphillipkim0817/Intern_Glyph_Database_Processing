import pandas as pd

#cleaning user_rewards table
user_rewards = pd.read_csv(r'C:\Users\Woosuk Kim\Downloads\[Cognitive AI] Database Snapshot\user_rewards.csv')
user_rewards.drop("created_at", inplace=True, axis=1)
user_rewards.drop("updated_at", inplace=True, axis=1)

user_rewards.columns = user_rewards.columns.str.title()
user_rewards = user_rewards.rename(columns=lambda x: x.replace("_", " "))
user_rewards = user_rewards.rename(columns=lambda x: x.replace("Id", "ID"))
user_rewards.rename(columns={"ID": "User Reward ID"}, inplace=True)

#creating two versions of the user_rewards table (dividing by whether the status of the reward is sent or not) - while preserving original user_rewards table
user_rewards_SENT = user_rewards[user_rewards["Status"] == "SENT"].copy()
user_rewards_PENDING = user_rewards[user_rewards["Status"] == "PENDING"].copy()


#progress checker
# print(user_rewards_SENT.columns)