import pandas as pd

df = pd.read_csv("data/owid-covid-data.csv")

covid = df[[
    "location",
    "date",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "population"
]]

covid = covid.dropna(subset=["location"])

covid.to_csv("covid_cleaned.csv", index=False)

print("File exported successfully!")