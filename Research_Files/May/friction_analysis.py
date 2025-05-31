import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV files
input_file_1 = 'Research_Files/May/kermit106_10.csv'  # 0 2 7

# Load the data into a DataFrame
df_1 = pd.read_csv(input_file_1)

# Keep only the specified columns
df_1 = df_1[['BackendTime', 'ch0sens', 'ch2sens', 'ch7sens']]

# Overwrite the original files with the filtered data
df_1.to_csv(input_file_1, index=False)

# Rescale BackendTime to seconds and set the first value to 0
df_1['BackendTime'] = (df_1['BackendTime'] - df_1['BackendTime'].iloc[0]) / 1e3
# Plot the values from df_1 against BackendTime
plt.figure(figsize=(12, 8))
plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT (df_1)')
plt.plot(df_1['BackendTime'], df_1['ch2sens'], label='Load Cell start (df_1)')
plt.plot(df_1['BackendTime'], df_1['ch7sens'], label='Load Cell end (df_1)')

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

# 36.5g