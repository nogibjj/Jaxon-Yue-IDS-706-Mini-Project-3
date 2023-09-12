import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the uploaded csv file
df = pd.read_csv("Development of average annual wages.csv")

# Get the # of rows and columns of the dataframe
rows = df.shape[0]
columns = df.shape[1]

# Convert columns to float
df["2000"] = df["2000"].str.replace(",", "").astype(float)
df["2010"] = df["2010"].str.replace(",", "").astype(float)
df["2020"] = df["2020"].str.replace(",", "").astype(float)
df["2022"] = df["2022"].str.replace(",", "").astype(float)

# Top 3 countries with 2022 average annual wages
top_3_countries = df.sort_values("2022", ascending=False)[:3]

# Calculate the numerial change between 2000 to 2022
df["Change"] = df["2022"] - df["2000"]

# Calculate the median for the 2022 numbers
median = np.median(df["2022"].dropna())

# Find the mean for every year's data
mean_2000 = np.mean(df["2000"])
mean_2010 = np.mean(df["2010"])
mean_2020 = np.mean(df["2020"])
mean_2022 = np.mean(df["2022"])
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
