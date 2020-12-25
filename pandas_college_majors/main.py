import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

# print(df.head()) # View first 5 rows
# print(df.tail()) # View last 5 rows

# print(df.shape) # Display number of rows and columns as tuple

# print(df.columns) # Display column names

# print(df.isna()) # View blank cells or cells that contain strings instead of numbers

clean_df = df.dropna()  # Remove rows that contain NaN cells
# print(clean_df.tail())

# print(clean_df["Starting Median Salary"]) # Get all rows from given column

# print(clean_df["Starting Median Salary"].max()) # Get the highest value from all rows

# Get index of row with greatest value
# max_starting_salary_index = clean_df["Starting Median Salary"].idxmax()

# Get row with loc property and display value at given column
# print(clean_df["Undergraduate Major"].loc[max_starting_salary_index])
# Equivalent to above is
# print(clean_df["Undergraduate Major"][max_starting_salary_index])
# Same as above, but retrieve entire row instead of just a cell
# print(clean_df.loc[max_starting_salary_index])

# College major and highest mid career salary
# highest_median_salary_idx = clean_df["Mid-Career Median Salary"].idxmax()
# highest_median_salary_row = clean_df.loc[highest_median_salary_idx]
# print(highest_median_salary_row["Undergraduate Major"])
# print(highest_median_salary_row["Mid-Career Median Salary"])
#
# lowest_starting_salary_idx = clean_df["Starting Median Salary"].idxmin()
# lowest_starting_salary_row = clean_df.loc[lowest_starting_salary_idx]
# print(lowest_starting_salary_row["Undergraduate Major"])
# print(lowest_starting_salary_row["Starting Median Salary"])
#
# lowest_mid_career_salary_idx = clean_df["Mid-Career Median Salary"].idxmin()
# lowest_mid_career_salary_row = clean_df.loc[lowest_mid_career_salary_idx]
# print(lowest_mid_career_salary_row["Undergraduate Major"])
# print(lowest_mid_career_salary_row["Mid-Career Median Salary"])

# Get difference between earnings of 10th and 90th percentile
# diff_10th_90th_earnings = clean_df["Mid-Career 90th Percentile Salary"] - \
#                           clean_df["Mid-Career 10th Percentile Salary"]
# Result will be new column that can be added to DataFrame
# clean_df.insert(1, "Spread", diff_10th_90th_earnings)
# print(clean_df.head())
# low_risk = clean_df.sort_values("Spread")
# Pass list to DataFrame with names of desired columns
# print(low_risk[["Undergraduate Major", "Spread"]].head())

# Sort by 90th percentile in descending order
# high_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
# print(high_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())

# clean_df.insert(1, "Spread", diff_10th_90th_earnings)
# greatest_spread = clean_df.sort_values("Spread", ascending=False)
# print(greatest_spread[["Undergraduate Major", "Spread"]].head())

# Count how many majors we have in each "Group" category
# print(clean_df.groupby("Group").count())

# Print float numbers to look like 1,012.45
# pd.options.display.float_format = "{:,.2f}".format

# print(clean_df.groupby("Group").mean())
