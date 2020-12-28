import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

tesla_df = pd.read_csv("TESLA Search Trend vs Price.csv")
unemployment_df = pd.read_csv("UE Benefits Search vs UE Rate 2004-19.csv")
daily_bitcoin_df = pd.read_csv("Daily Bitcoin Price.csv")
bitcoin_search_df = pd.read_csv("Bitcoin Search Trend.csv")

# print(bitcoin_search_df.shape)
# print(tesla_df.columns)
# print(f"Largest value for Tesla in Web Search: {tesla_df.TSLA_WEB_SEARCH.max()}")
# print(f"Smallest value for Tesla in Web Search: {tesla_df.TSLA_WEB_SEARCH.min()}")
# print(tesla_df.describe())

# print(unemployment_df.shape)
# print(unemployment_df.describe())

# print(tesla_df.isna().values.any())
# print(daily_bitcoin_df.isna().values.sum())
# print(daily_bitcoin_df[daily_bitcoin_df.CLOSE.isna()])
# daily_bitcoin_df.fillna(0, inplace=True)
daily_bitcoin_df.dropna(inplace=True)

tesla_df.MONTH= pd.to_datetime(tesla_df.MONTH)
unemployment_df.MONTH = pd.to_datetime(unemployment_df.MONTH)
daily_bitcoin_df.DATE = pd.to_datetime(daily_bitcoin_df.DATE)
bitcoin_search_df.MONTH = pd.to_datetime(bitcoin_search_df.MONTH)

# resample() to make time-series data comparable to another by changing periodicity.
# Convert daily data to monthly data.
# rule parameter specifies sample frequency (monthly in this case).
# on parameter specifies which column to use.
# After resampling(), we want the last available price of the month.
# If we wanted the average price over the month:
# daily_bitcoin_df.resample(rule="M", on="DATE").mean()
monthly_bitcoin_df = daily_bitcoin_df.resample(rule="M", on="DATE").last()

plt.figure(figsize=(16, 10), dpi=120)
plt.title("Tesla Web Search vs Price", fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx() # By using twinx() ax1 and ax2 share the same x-axis
ax1.set_xlabel("Year", fontsize=8)
ax1.set_ylabel("TSLA Stock Price", fontsize=8)
ax2.set_ylabel("Search Trend", fontsize=8)
ax1.set_xlim([tesla_df.MONTH.min(), tesla_df.MONTH.max()])
ax1.set_ylim([0, 600])

# Create locators for ticks on the time axis.
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.grid(color="grey", linestyle="--")
ax1.plot(tesla_df.MONTH, tesla_df.TSLA_USD_CLOSE, color="#E6232E", linestyle="--", linewidth=3)
ax2.plot(tesla_df.MONTH, tesla_df.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)
plt.show()