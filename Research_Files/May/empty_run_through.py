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


# Rescale BackendTime to seconds and set the first value to 0
df_1['BackendTime'] = (df_1['BackendTime'] - df_1['BackendTime'].iloc[0]) / 1e3
df_2['BackendTime'] = (df_2['BackendTime'] - df_2['BackendTime'].iloc[0] + 750) / 1e3

# df_1 = df_1[(df_1['BackendTime'] >= 322) & (df_1['BackendTime'] <= 341)] # 3bar
# df_2 = df_2[(df_2['BackendTime'] >= 322) & (df_2['BackendTime'] <= 341)] # 3bar
# df_1 = df_1[(df_1['BackendTime'] >= 165) & (df_1['BackendTime'] <= 193)] # 4bar
# df_2 = df_2[(df_2['BackendTime'] >= 165) & (df_2['BackendTime'] <= 193)] # 4bar
# df_1 = df_1[(df_1['BackendTime'] >= 145) & (df_1['BackendTime'] <= 180)] # 5bar
# df_2 = df_2[(df_2['BackendTime'] >= 145) & (df_2['BackendTime'] <= 180)] # 5bar
plt.rc('legend', fontsize=24)   # Increase legend font size
plt.rc('lines', linewidth=4)    # Further increase line width
plt.rc('axes', labelsize=28)    # Increase axis label font size
plt.figure(figsize=(12, 8))    # Increase figure size
plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size
plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT')
plt.plot(df_2['BackendTime'], df_2['ch1sens'], label='Outlet PT')
# Add horizontal lines at y=1.303 and y=1.625 with labels
# plt.axhline(y=1.195, color='red', linestyle='--', linewidth=3, label='y=1.195') # 3bar
# plt.axhline(y=1.405, color='green', linestyle='--', linewidth=3, label='y=1.405') # 3bar
# plt.axhline(y=1.303, color='red', linestyle='--', linewidth=3, label='y=1.303') # 4bar
# plt.axhline(y=1.625, color='green', linestyle='--', linewidth=3, label='y=1.625') # 4bar
# plt.axhline(y=1.432, color='red', linestyle='--', linewidth=3, label='y=1.432') # 5bar
# plt.axhline(y=1.852, color='green', linestyle='--', linewidth=3, label='y=1.852') # 5bar
# for line in plt.gca().lines[-2:]:
#     line.set_alpha(0.6)
# Add labels and title
plt.xlabel('Experiment Time (s)')
plt.ylabel('Absolute Pressure (bar)')
# plt.xlim(322, 341) # 3bar
# plt.xlim(165, 193) # 4bar
# plt.xlim(145, 177) # 5bar
plt.legend()

# Show the plot
plt.show()



# 1 was first test
# 2 - 4 were static pressure loss tests with clean tank
# 5 - 6 were static pressure loss tests with old piston design (handle)
# 7 was static pressure loss test with new piston design (no handle)
# 8 was new piston design with sand