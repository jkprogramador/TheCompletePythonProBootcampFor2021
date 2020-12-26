import pandas as pd

# Series are array-like objects. They can be combined to form a tabular object
# (DataFrame), with rows an columns being the series
# Series can have an index, where all values must be unique
# If we do not assign an index, then a numeric sequence starting from 0 will be used
# Series can have a name, so that, if we were to create a DataFrame using this
# series, a column/row name would be automatically assigned
ser1 = pd.Series([1, 2, 3, 4])
# print(ser1)
ser2 = pd.Series(["a", "b", "c"])
# print(ser2)
# Create an index consisting of names of cities
idx = pd.Index(
    ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", \
     "Phoenix", "San Antonio", "San Diego", "Dallas"])
# print(idx)

# Create a series with index and name
populations = pd.Series([1245.0, 4587.0, 9654.0, 7415.0, 5214.0, 6532.0, \
                         58551.0, 6321.0, 745.0], index=idx, name="Population")
# print(populations)

# Create a series from a dictionary, where each key will be the index
states = pd.Series({"New York": "New York", "Los Angeles": "Los Angeles"}, \
                   name="State")
# print(states)

area = pd.Series({"New York": 302.6, "Los Angeles": 468.7}, name="Area")
# print(area)

# Create DataFrame from list of tuples
# print(pd.DataFrame([(1, "a"), (2, "b"), (3, "c")], columns=["Numbers", "Letters"]))

# Create DataFrame from dictionary
# print(pd.DataFrame({"Numbers": [1, 2, 3], "Letters": ["a", "b", "c"]}))

# If the lists are not of the same length, an error will be thrown
# because pandas does not know how to assign an index to missing info
# print(pd.DataFrame({"Numbers": [1, 2, 3, 4], "Letters": ["a"]}))

# However, if we use series, even if they are not of same length,
# pandas knows how to line up the elements in different series,
# filling any spot where info is missing with NaN
# print(pd.DataFrame({"Numbers": ser1, "Letters": ser2}))

# print(pd.DataFrame({"State": states, "Population": populations, "Area": area}))

# Read CSV file
# df = pd.read_csv("salaries_by_college_major.csv")

# print(df.head()) # View first 5 rows
# print(df.tail()) # View last 5 rows

# print(df.shape) # Display number of rows and columns as tuple

# print(df.columns) # Display column names

# print(df.isna()) # View blank cells or cells that contain strings instead of numbers

# clean_df = df.dropna()  # Remove rows that contain NaN cells
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
