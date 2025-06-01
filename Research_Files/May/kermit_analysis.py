import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV files
input_file_1 = 'Research_Files/June/5_bar_sand/3_kermit106.csv'  # 0 2 7
input_file_2 = 'Research_Files/June/5_bar_sand/3_kermit108.csv'  # 0 1 7

# Load the data into a DataFrame
df_1 = pd.read_csv(input_file_1)
df_2 = pd.read_csv(input_file_2)

# Keep only the specified columns
df_1 = df_1[['BackendTime', 'ch0sens', 'ch2sens', 'ch7sens']]
df_2 = df_2[['BackendTime', 'ch0sens', 'ch1sens', 'ch7sens']]

# Replace any values in 'ch1sens' column of df_2 above 3 with 0
df_2['ch1sens'] = df_2['ch1sens'].apply(lambda x: None if x > 3 else x)
df_2['ch7sens'] = df_2['ch7sens'].apply(lambda x: None if x > 3 else x)
# Rescale BackendTime to seconds and set the first value to 0
df_1['BackendTime'] = (df_1['BackendTime'] - df_1['BackendTime'].iloc[0]) / 1e3
df_2['BackendTime'] = (df_2['BackendTime'] - df_2['BackendTime'].iloc[0]) / 1e3
# Plot the values from df_1 against BackendTime
plt.figure(figsize=(12, 8))
plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT (df_1)')
plt.plot(df_1['BackendTime'], df_1['ch2sens'], label='Load Cell start (df_1)')
plt.plot(df_1['BackendTime'], df_1['ch7sens'], label='Load Cell end (df_1)')

# Plot the values from df_2 against BackendTime
plt.plot(df_2['BackendTime'], df_2['ch0sens'], label='Pre-choke PT', linestyle='--')
plt.plot(df_2['BackendTime'], df_2['ch1sens'], label='Post-choke PT', linestyle='--')
plt.plot(df_2['BackendTime'], df_2['ch7sens'], label='Load Cell cyclone', linestyle='--')

# Add labels and title
plt.xlabel('BackendTime')
plt.ylabel('Sensor Values')
plt.title('Sensor Values vs BackendTime (df_1 and df_2)')
plt.legend()

# Show the plot
plt.show()



# 1 was first test
# 2 - 4 were static pressure loss tests with clean tank
# 5 - 6 were static pressure loss tests with old piston design (handle)
# 7 was static pressure loss test with new piston design (no handle)
# 8 was new piston design with sand