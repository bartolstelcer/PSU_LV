import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:\\Users\\Admin\\Desktop\\Bartol\\pythonProgrami\\LV5\\occupancy_processed.csv")

plt.figure(figsize = (10, 6))
for count in data['Room_Occupancy_Count'].unique():
    subset = data[data['Room_Occupancy_Count'] == count]
    plt.scatter(subset['S3_Temp'], subset['S5_CO2'], label = f'Occupancy Count {count}', alpha = 0.5)

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.legend()
plt.title('Scatter Plot of S3_Temp vs S5_CO2')
plt.show()

print(f'Broj podatkovnih primjera: {len(data)}')

print(data['Room_Occupancy_Count'].value_counts())