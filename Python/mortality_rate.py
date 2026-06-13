import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/owid-covid-data.csv")

# Latest data per country
latest = df.groupby("location").agg({
    "total_cases":"max",
    "total_deaths":"max"
})

# Remove missing values
latest = latest.dropna()

# Filter countries with sufficient cases
latest = latest[latest["total_cases"] > 100000]

# Calculate mortality rate
latest["mortality_rate"] = (
    latest["total_deaths"] /
    latest["total_cases"]
) * 100

# Top 10 mortality rates
top10 = latest.sort_values(
    by="mortality_rate",
    ascending=False
).head(10)

print(top10[["mortality_rate"]])

# Plot
plt.figure(figsize=(10,6))

sns.barplot(
    x=top10["mortality_rate"],
    y=top10.index
)

plt.title("Top 10 Countries by Mortality Rate")
plt.xlabel("Mortality Rate (%)")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("images/mortality_rate.png")

plt.show()