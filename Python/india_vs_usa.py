import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/owid-covid-data.csv")

# Select countries
countries = ["India", "United States"]

covid = df[df["location"].isin(countries)]

# Convert date column
covid["date"] = pd.to_datetime(covid["date"])

# Plot
plt.figure(figsize=(12,6))

for country in countries:
    temp = covid[covid["location"] == country]
    
    plt.plot(
        temp["date"],
        temp["total_cases"],
        label=country
    )

plt.title("India vs USA Total COVID Cases")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()

plt.tight_layout()

plt.savefig("images/india_vs_usa_cases.png")

plt.show()