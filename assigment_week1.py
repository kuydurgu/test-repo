import pandas as pd
import scipy.stats as stats

# Read the CSV file into a DataFrame
df = pd.read_csv("wetter.csv")
# Display the first few rows of the DataFrame
print(df.head())

# Calculate the overall average temperature
overall_avg_temp = df["Temperatur"].mean()
print(f"Overall average temperature: {overall_avg_temp:.2f}°C")

# Extract the month from the 'Datum' column
df["Monat"] = pd.to_datetime(df["Datum"]).dt.month

# Calculate the average temperature for the month of July
july_avg_temp = df[df["Monat"] == 7]["Temperatur"].mean()
print(f"Average temperature in July: {july_avg_temp:.2f}°C")

# Calculate the average temperature for May
may_avg_temp = df[df["Monat"] == 5]["Temperatur"].mean()
print(f"Average temperature in May: {may_avg_temp:.2f}°C")

# Compare whether July and May differ significantly in average temperature
# Extract temperature data for both months
july_temps = df[df["Monat"] == 7]["Temperatur"]
may_temps = df[df["Monat"] == 5]["Temperatur"]

# Perform a t-test to check for statistical significance
t_statistic, p_value = stats.ttest_ind(july_temps, may_temps, equal_var=False)
print("\nT-test comparing July and May temperatures:")
print(f"t-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.4f}")

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print(
        f"The difference in average temperatures between July ({july_avg_temp:.2f}°C) and May ({may_avg_temp:.2f}°C) is statistically significant (p < {alpha})."
    )
else:
    print(
        f"The difference in average temperatures between July ({july_avg_temp:.2f}°C) and May ({may_avg_temp:.2f}°C) is not statistically significant (p >= {alpha})."
    )

# Optional: Calculate the difference in means
temp_difference = july_avg_temp - may_avg_temp
print(f"Temperature difference (July - May): {temp_difference:.2f}°C")
