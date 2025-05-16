import pandas as pd

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Optional: Save it locally
df.to_csv("owid-covid-data.csv", index=False)

print("Dataset downloaded and saved as 'owid-covid-data.csv'.")