import pandas as pd

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
df = df.dropna()
# print(df.shape)
# print(df.head())
# print(df.tail())
# print(df.count())
# by_tag = df.groupby("TAG")
# Get sum of all posts by tag
# sum_by_tag = by_tag.sum()
# print(sum_by_tag)
# Display number of months of posts by tag
# print(by_tag.count())

# Display second date entry
# print(df["DATE"][1])
# Same as above
# print(df.DATE[1])

# print(type(df.DATE[1]))
# Convert string to timestamp with pandas to_datetime
# print(type(pd.to_datetime(df.DATE[1])))

# Convert entire DATE column from string to timestamp
df.DATE = pd.to_datetime(df.DATE)
# print(df.head())

# test_df = pd.DataFrame({
#     "Age": ["Young", "Young", "Young", "Young", "Old", "Old", "Old", "Old"],
#     "Actor": ["Jack", "Arnold", "Keanu", "Sylvester", "Jack", "Arnold", "Keanu", "Sylvester"],
#     "Power": [100, 80, 25, 50, 99, 75, 5, 30]
# })
# print(test_df)

# Convert DataFrame so each category has its own column
# Ex.: create separate column for each actor (columns parameter)
# where each row category is the age (index parameter)
# and each value in the new cell is the power (values parameter)
# pivoted_df = test_df.pivot(index="Age", columns="Actor", values="Power")
# print(pivoted_df)

# Pivot the DataFrame so that each column is a programming language
# and each row category is a date and each value is the number of posts
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
# print(reshaped_df.shape)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# print(reshaped_df.columns)

# count() excludes NaN values
# print(reshaped_df.count())

# Substitute the number 0 for any NaN cell
reshaped_df.fillna(0, inplace=True)
# print(reshaped_df.head())
# Check if there are any NaN cells
print(reshaped_df.isna().values.any())