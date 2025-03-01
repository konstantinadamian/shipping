import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv("C:\\Users\\Konny\\Downloads\\archive (5)\\SHIPPING_PERFORMANCE.csv")

print(f'first five rows : {data.head()}')

# Create a copy of the data
copy_data = data.copy()

print(copy_data.info())
# Remove rows with all null values
copy_data = copy_data.dropna(how='all')

print(f'Number of duplicate rows: {copy_data.duplicated().sum()}')

copy_data[['Engine_Type', 'Ship_Type', 'Route_Type','Maintenance_Status','Weather_Condition']] = copy_data[['Engine_Type', 'Ship_Type', 'Route_Type','Maintenance_Status','Weather_Condition']].fillna('No Information')

for column in ['Engine_Type', 'Ship_Type', 'Route_Type','Maintenance_Status','Weather_Condition']:
    print(f"{column}: {copy_data[column].unique()}")

# Compute the average efficiency per engine type
efficiency_per_engine = copy_data.groupby('Engine_Type')['Efficiency_nm_per_kWh'].mean()
efficiency_per_engine = efficiency_per_engine.sort_values()
print(efficiency_per_engine)

print(f'standard deviation : {np.std(efficiency_per_engine)}')

# Visualization of performance by engine type
def graph_(data,title,x_label,y_label,color_bar,color_grid,rotation,size):
    plt.figure(figsize=(8, 4))
    data.plot(kind='bar', color = color_bar )
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=rotation, size= size)
    plt.grid(True, color= color_grid, linestyle='--', linewidth=0.6)
    plt.show()

result_graph = graph_(data= efficiency_per_engine,
                      title = 'Performance by Engine Type',
                      x_label ='Engine Type',
                      y_label = 'Average Performance (nm per kWh)',
                      color_bar = 'lightsteelblue',
                      color_grid = 'lightcoral',
                      rotation= 45,
                      size= 8)

# Compute the average efficiency per ship type and route type
efficiency_per_combination = copy_data.groupby(['Ship_Type', 'Route_Type'])['Efficiency_nm_per_kWh'].mean()

efficiency_per_combination = efficiency_per_combination.sort_values()
print(efficiency_per_combination)
print(f'standard deviation : {np.std(efficiency_per_combination)}')

# Visualization of efficiency by ship type and route type
result_graph = graph_(data=efficiency_per_combination,
                     title='Efficiency by Ship Type and Route Type',
                     x_label='Ship Type and Route Type',
                     y_label='Average Performance (nm per kWh)',
                     color_bar = 'lightsteelblue',
                     color_grid ='coral',
                     rotation=70,
                     size=8)

#conversion to dates and check if it has been done correctly
copy_data['Date'] = pd.to_datetime(copy_data['Date'] ,dayfirst=True, errors='coerce')
print(copy_data['Date'].dtype)
print(copy_data['Date'].isna().sum())

copy_data['month and year'] = copy_data['Date'].dt.strftime('%b %Y')
print(copy_data['month and year'])


groupby_columns = copy_data.groupby('month and year')[[
  'Revenue_per_Voyage_USD','Operational_Cost_USD'
]].mean()
print(groupby_columns)

groupby_columns.plot(kind='bar', figsize=(8,5) ,color=['sandybrown','lightsteelblue'])
plt.xlabel('Month and Year')
plt.ylabel('USD')
plt.title('Revenue vs Operational Cost Per Month')
plt.xticks(rotation=45)
plt.legend()
plt.show()

sum_Revenue_per_Voyage_USD = groupby_columns['Revenue_per_Voyage_USD'].sum()
sum_Operational_Cost_USD = groupby_columns['Operational_Cost_USD'].sum()
result = sum_Revenue_per_Voyage_USD - sum_Operational_Cost_USD
print(int(result))

print(f'Cost to Revenue Ratio : {(sum_Operational_Cost_USD) / (sum_Revenue_per_Voyage_USD) * 100} %')

num_columns = data[['Speed_Over_Ground_knots', 'Engine_Power_kW', 'Distance_Traveled_nm','Draft_meters',
'Cargo_Weight_tons','Operational_Cost_USD','Revenue_per_Voyage_USD','Turnaround_Time_hours',
'Efficiency_nm_per_kWh','Seasonal_Impact_Score']]
print(num_columns.corr())

print(num_columns.describe())