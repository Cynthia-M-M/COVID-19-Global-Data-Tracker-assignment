import pandas as pd

# Read the downloaded CSV
df = pd.read_csv('owid-covid-data.csv')

# Print the first few rows to verify it's loaded correctly
print(df.head())
