import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv("C:\\Users\\Konny\\Downloads\\archive (5)\\SHIPPING_PERFORMANCE.csv")

print(f'first five rows : {data.head()}')

# Create a copy of the data
copy_data = data.copy()

print(f'information about the dataframe : {copy_data.info()}')

# Remove rows with all null values
copy_data = copy_data.dropna(how='all')

print(f'Number of duplicate rows: {copy_data.duplicated().sum()}')

# Convert "Date" column to datetime format
copy_data['Date'] = pd.to_datetime(copy_data['Date'], format='%d-%m-%Y')
print(f'data type of the "Date" column : {copy_data['Date'].dtype}')

copy_data[['Engine_Type', 'Ship_Type', 'Route_Type']] = copy_data[['Engine_Type', 'Ship_Type', 'Route_Type']].fillna('No Information')

for column in ['Engine_Type', 'Ship_Type', 'Route_Type']:
    print(f"{column}: {copy_data[column].unique()}")

# Compute the average efficiency per engine type
efficiency_per_engine = copy_data.groupby('Engine_Type')['Efficiency_nm_per_kWh'].mean()
efficiency_per_engine = efficiency_per_engine.sort_values()
print(efficiency_per_engine)

print(f'standard deviation : {np.std(efficiency_per_engine)}')

# Visualization of performance by engine type
plt.figure(figsize=(8, 4))
efficiency_per_engine.plot(kind='bar', color='lightsteelblue')
plt.title('Performance by Engine Type')
plt.xlabel('Engine Type')
plt.ylabel('Average Performance (nm per kWh)')
plt.xticks(rotation=10, size=8)
plt.grid(True, color='lightcoral', linestyle='--', linewidth=0.6)
plt.show()

# Compute the average efficiency per ship type and route type
efficiency_per_combination = copy_data.groupby(['Ship_Type', 'Route_Type'])['Efficiency_nm_per_kWh'].mean()

efficiency_per_combination = efficiency_per_combination.sort_values()
print(efficiency_per_combination)
print(f'standard deviation : {np.std(efficiency_per_combination)}')

# Visualization of efficiency by ship type and route type
plt.figure(figsize=(8, 4))
efficiency_per_combination.plot(kind='bar', color='blue')
plt.title('Efficiency by Ship Type and Route Type')
plt.xlabel('Ship Type and Route Type')
plt.ylabel('Average Efficiency (nm per kWh)')
plt.xticks(rotation=45, ha='right', size=7)
plt.tight_layout()
plt.grid(True, color='red', linestyle=':', linewidth=0.3)
plt.show()

