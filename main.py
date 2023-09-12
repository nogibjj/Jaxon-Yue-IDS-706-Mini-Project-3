import polars as pl
import numpy as np
import matplotlib.pyplot as plt

# Read the uploaded csv file
df = pl.read_csv("Development of average annual wages.csv")

# Get the # of rows and columns of the dataframe
rows = df.shape[0]
columns = df.shape[1]

# Convert columns to float
df = df.with_column(
    pl.col("2000").str.replace(",", "").cast(pl.Float64)
).with_column(
    pl.col("2010").str.replace(",", "").cast(pl.Float64)
).with_column(
    pl.col("2020").str.replace(",", "").cast(pl.Float64)
).with_column(
    pl.col("2022").str.replace(",", "").cast(pl.Float64)
)

# Top 3 countries with 2022 average annual wages
top_3_countries = df.sort("2022", reverse=True).head(3)

# Calculate the numerical change between 2000 to 2022
df = df.with_column(
    pl.col("2022") - pl.col("2000")
).rename_at_idx(-1, "Change")

# Calculate the median for the 2022 numbers
median = df["2022"].filter(lambda x: x.is_not_null()).median().get(0)

# Find the mean for every year's data
mean_2000 = df["2000"].mean().get(0)
mean_2010 = df["2010"].mean().get(0)
mean_2020 = df["2020"].mean().get(0)
mean_2022 = df["2022"].mean().get(0)
means = [mean_2000, mean_2010, mean_2020, mean_2022]

# Plot the growth of the average number
years = [2000, 2010, 2020, 2022]
plt.plot(years, means)

# Add labels and title
plt.xlabel("Year")
plt.xticks(ticks=years, labels=["2000", "2010", "2020", "2022"])
plt.ylabel("Average Annual Wages")
plt.title("Growth of Average Annual Wages")
plt.show()
