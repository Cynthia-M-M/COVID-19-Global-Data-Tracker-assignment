# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Download and Load the Dataset
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Optional: Save it locally
df.to_csv("owid-covid-data.csv", index=False)

# Step 2: Data Cleaning
# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Drop rows where important columns are missing
df = df.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])

# Alternatively, you could fill missing values (e.g., with zeros)
# df.fillna(0, inplace=True)

# Step 3: Data Exploration (Basic Analysis)
# Get summary statistics and check the info
print("\nSummary Statistics:")
print(df.describe())

print("\nData Info:")
print(df.info())

# Step 4: Data Visualization - Total COVID-19 Cases Worldwide Over Time
# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum total cases
df_grouped = df.groupby('date')['total_cases'].sum().reset_index()

# Plotting the total cases over time
plt.figure(figsize=(10,6))
plt.plot(df_grouped['date'], df_grouped['total_cases'], color='blue')
plt.title('Total COVID-19 Cases Worldwide Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 5: Data Visualization - Total Deaths by Continent
# Group by continent and sum total deaths
continent_deaths = df.groupby('continent')['total_deaths'].sum().reset_index()

# Plotting the total deaths by continent
plt.figure(figsize=(10,6))
sns.barplot(x='continent', y='total_deaths', data=continent_deaths, palette='viridis')
plt.title('Total COVID-19 Deaths by Continent')
plt.xlabel('Continent')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45)
plt.show()

# Step 6: Data Visualization - Vaccination Progress Over Time
# Group by date and sum total vaccinations
df_vaccinated = df.groupby('date')['total_vaccinations'].sum().reset_index()

# Drop rows where continent is missing to avoid errors in grouping
df = df.dropna(subset=['continent'])

# Plotting the vaccination progress over time
plt.figure(figsize=(10,6))
plt.plot(df_vaccinated['date'], df_vaccinated['total_vaccinations'], color='green')
plt.title('Total COVID-19 Vaccinations Worldwide Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 7: Advanced Analysis - Correlation Between Cases and Deaths
# Calculate correlation between total cases and total deaths
correlation = df[['total_cases', 'total_deaths']].corr()
print("\nCorrelation between Total Cases and Total Deaths:")
print(correlation)

# Plot the correlation matrix
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Between Total Cases and Total Deaths')
plt.show()

# Step 8: Save the Cleaned Data (Optional)
df.to_csv('cleaned_covid_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_covid_data.csv'")

# Step 9: Summary and Report (This can be done manually in a report or notebook)
