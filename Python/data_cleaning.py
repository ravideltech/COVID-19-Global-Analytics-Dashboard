import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/owid-covid-data.csv")

# Keep required columns
covid = df[[
    "location",
    "date",
    "total_cases"
]]

# Latest record for each country
latest = covid.groupby("location")["total_cases"].max()

# Top 10 countries
top10 = latest.sort_values(ascending=False).head(10)

print(top10)

# Plot
plt.figure(figsize=(10,6))

sns.barplot(
    x=top10.values,
    y=top10.index
)

plt.title("Top 10 Countries by Total COVID Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("images/top10_cases.png")

plt.show()