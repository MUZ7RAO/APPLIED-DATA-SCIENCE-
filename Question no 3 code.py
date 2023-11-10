import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
df = pd.read_excel("C:\\Users\\Ahsan Ali\\Desktop\\muzz\\(Dataa).xlsx")

# Extract relevant data for plotting
years = df.columns[2:]
yellow_fever_data = df.loc[0, years]
total_tetanus_data = df.loc[1, years]
japanese_encephalitis_data = df.loc[2, years]
pertussis_data = df.loc[3, years]

# function is used for plotting figure 
plt.figure(figsize=(12, 8))

# Scatter plot for disease with different colors
plt.scatter(years, yellow_fever_data, label='Yellow Fever', marker='o', color='gold')
plt.scatter(years, total_tetanus_data, label='Total Tetanus', marker='o', color='blue')
plt.scatter(years, japanese_encephalitis_data, label='Japanese Encephalitis', marker='o', color='green')
plt.scatter(years, pertussis_data, label='Pertussis', marker='o', color='red')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Total Cases')
plt.title('Comparison of diseases')
plt.legend()

# Show plot
plt.show()

