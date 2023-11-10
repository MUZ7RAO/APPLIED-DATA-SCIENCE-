import pandas as pd
import matplotlib.pyplot as plt

# importing data from excel file 
# importing the excel data into Python for basic analysis
df = pd.read_excel("C:\\Users\\Ahsan Ali\\Desktop\\muzz\\Q#1 (Dataa).xlsx")

# Melt function in pandas is used to transform a DataFrame from wide format to long format
#essentially reshaping the data
df_melted = pd.melt(df, id_vars=['Country / Region', 'Disease'], var_name='Year', value_name='Cases')

# Filtering the data 
diseases = ['Yellow fever', 'Total tetanus', 'Japanese encephalitis', 'Pertussis']
df_filtered = df_melted[df_melted['Disease'].isin(diseases)]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Defining different line styles for the plot
# Solid, Dahed, dash-dot, dotted
line_styles = ['-', '--', '-.', ':']
#different colors for plot
colors = ['g', 'b', 'r', 'k']

# Creating a multiple line plot 
for idx, disease in enumerate(diseases):
    df_temp = df_filtered[df_filtered['Disease'] == disease]
    ax.plot(df_temp['Year'], df_temp['Cases'], linestyle=line_styles[idx % len(line_styles)], color=colors[idx % len(colors)], label=disease)

# giving a title and labels
ax.set_title(' Disease in last many years ')
ax.set_xlabel('years')
ax.set_ylabel('Total amount of Cases')
ax.legend()
ax.grid(True)
plt.show()
