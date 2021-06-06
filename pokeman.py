from numpy import column_stack
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pokeman_df = pd.read_csv("F:\VSC Works\Python\Brainery Code Intermediate\pokeman.csv")
# Read xlsx - requires pip install xlrd
# pokeman_df = pd.read_excel("pokeman.xlsx")

teamattack = pokeman_df.loc[0:20,['Name', 'Type 1', 'Attack']]

#renaming column
teamattack = pokeman_df.loc[:,['Name', 'Type 1', 'Attack']]
teamattack = teamattack.rename(columns={"Type 1": "Type_1"})

teamattackfire = teamattack[teamattack.Type_1 == "Fire"]
print(teamattackfire)
# print(pokeman_df)
