import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/owid-covid-data.csv")

# Maximum deaths per country
deaths = df.groupby("location")["total_deaths"].max()

# Top 10 countries
top10 = deaths.sort_values(ascending=False).head(10)

print(top10)

# Plot
plt.figure(figsize=(10,6))

sns.barplot(
    x=top10.values,
    y=top10.index
)

plt.title("Top 10 Countries by COVID Deaths")
plt.xlabel("Total Deaths")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("images/top10_deaths.png")

plt.show()