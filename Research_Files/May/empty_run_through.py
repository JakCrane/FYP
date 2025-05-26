import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV files
input_file_1 = 'Research_Files/May/kermit106_2.csv'  # 0 2 7
input_file_2 = 'Research_Files/May/kermit108_2.csv'  # 0 1 7

# Load the data into a DataFrame
df_1 = pd.read_csv(input_file_1)
df_2 = pd.read_csv(input_file_2)

# Keep only the specified columns
df_1 = df_1[['BackendTime', 'ch0sens']]
df_2 = df_2[['BackendTime', 'ch1sens']]

# Plot the values from df_1 against BackendTime

# Plot a horizontal line at y = 1.2

# Rescale BackendTime to seconds and set the first value to 0
df_1['BackendTime'] = (df_1['BackendTime'] - df_1['BackendTime'].iloc[0]) / 1e3
df_2['BackendTime'] = (df_2['BackendTime'] - df_2['BackendTime'].iloc[0] + 750) / 1e3
plt.rc('legend', fontsize=18)  # Further increase legend font size
plt.rc('lines', linewidth=3)   # Further increase line width
plt.rc('axes', labelsize=20)   # Further increase axis label font size
plt.figure(figsize=(12, 8))   # Increase figure size
plt.rc('xtick', labelsize=20)  # Increase x-axis tick font size
plt.rc('ytick', labelsize=20)  # Increase y-axis tick font size
plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT')
plt.plot(df_2['BackendTime'], df_2['ch1sens'], label='Post-choke PT', linestyle='--')

# Add labels and title
plt.xlabel('Experiment Time (s)')
plt.ylabel('Absolute Pressure (bar)')
plt.legend()

# Show the plot
plt.show()



# 1 was first test
# 2 - 4 were static pressure loss tests with clean tank
# 5 - 6 were static pressure loss tests with old piston design (handle)
# 7 was static pressure loss test with new piston design (no handle)
# 8 was new piston design with sand