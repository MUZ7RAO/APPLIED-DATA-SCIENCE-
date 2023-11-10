import pandas as pd
import matplotlib.pyplot as plt

# extract Excel file
df = pd.read_excel("C:\\Users\\Ahsan Ali\\Desktop\\muzz\\(Dataa).xlsx")

# Extract relevant data for plotting the functions
disease_labels = df['Disease']
data_2022 = df[2022]

# Plotting the functions 
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(data_2022, labels=disease_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

#titles and show function
plt.title('Distribution of Diseases in 2022')
plt.show()

