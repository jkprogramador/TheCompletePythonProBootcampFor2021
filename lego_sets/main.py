import pandas as pd
import matplotlib.pyplot as plt

# colors_df = pd.read_csv("data/colors.csv")
# How many unique different colors LEGO bricks are there?
# print(colors_df["name"].nunique())

# How many LEGO colors are transparent compared to how many are opaque.
# print(colors_df.groupby("is_trans").count())
# value_counts method is a very quick way of finding the number of members of
# each category.
# print(colors_df.is_trans.value_counts())

sets_df = pd.read_csv("data/sets.csv")

# In which year were the first LEGO sets released and what were they called?
sets_df.sort_values(by="year", ascending=True, inplace=True)
# print(sets_df.head())

# How many different products did LEGO sell in their first year?
# print(sets_df.groupby("year").nunique())
# print(sets_df[sets_df["year"] == 1949])

# Top 5 LEGO sets with the largest number of parts
# print(sets_df.sort_values(by="num_parts", ascending=False).head())

# Create series which has years as index an number of sets as value.
# sets_by_year = sets_df.groupby("year").count()["set_num"]
sets_by_year_df = sets_df.groupby("year").count()
# plt.figure(figsize=(16, 10))
# plt.xlabel("Year", fontsize=8)
# plt.ylabel("Number of sets", fontsize=8)
# plt.plot(sets_by_year_df.index[:-2], sets_by_year_df["set_num"][:-2])
# plt.show()

# Get number of different themes shipped by year.
# agg() accepts a dictionary specifying which operation to apply to each column.
# Ex.: calculate the number of unique entries in theme_id column
# themes_by_year = sets_df.groupby("year").agg({"theme_id": pd.Series.nunique})
# Rename some columns
# themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)

# ax1 = plt.gca() # Get current axis
# ax2 = ax1.twinx() # By using twinx() ax1 and ax2 share the same x-axis

# plt.figure(figsize=(16, 10))
# ax1.plot(sets_by_year_df.index[:-2], sets_by_year_df.set_num[:-2], color="g")
# ax2.plot(themes_by_year.index[:-2], themes_by_year["nr_themes"][:-2], color="b")
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Number of Sets", color="green")
# ax2.set_ylabel("Number of Themes", color="blue")
# plt.show()

# Calculate the average of number of parts per set grouped by year.
# parts_per_set = sets_df.groupby("year").agg({"num_parts": pd.Series.mean})
# parts_per_set.rename(columns={"num_parts": "average num_parts"}, inplace=True)
# plt.figure(figsize=(16, 10))
# plt.xlabel("Year", fontsize=8)
# plt.ylabel("Average number of parts", fontsize=8)
# plt.scatter(parts_per_set.index[:-2], parts_per_set["average num_parts"][:-2])
# plt.show()

# Count the number of sets per theme
set_theme_count = sets_df["theme_id"].value_counts()
# print(set_theme_count.head())
set_theme_count = pd.DataFrame({
    "id": set_theme_count.index,
    "set_count": set_theme_count.values
})

# Get themes whose name is Star Wars
themes_df = pd.read_csv("data/themes.csv")
star_wars_df = themes_df[themes_df.name == "Star Wars"]
# print(star_wars_df)

# Which products correspond to Star Wars themes in sets.csv
# print(sets_df[sets_df.theme_id == 209])

# Use merge() to combine two separate DataFrames.
# Works on columns with the same name in both DataFrames.
# Provide the two DataFrames and the column name on which to merge.
merged_df = pd.merge(set_theme_count, themes_df, on="id")
# print(merged_df.head())
plt.figure(figsize=(14, 8))
plt.xticks(fontsize=5, rotation=45)
plt.yticks(fontsize=10)
plt.xlabel("Theme Name", fontsize=8)
plt.ylabel("Nr of Sets", fontsize=10)
# Top 10 themes on bar chart
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()