import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV files
input_file_1 = 'Research_Files/May/kermit106_9.csv'  # 0 2 7
input_file_2 = 'Research_Files/May/kermit108_9.csv'  # 0 1 7

# Load the data into a DataFrame
df_1 = pd.read_csv(input_file_1)
df_2 = pd.read_csv(input_file_2)

# Keep only the specified columns
df_1 = df_1[['BackendTime', 'ch0sens']]
df_2 = df_2[['BackendTime', 'ch1sens']]

# Plot the values from df_1 against BackendTime
plt.figure(figsize=(12, 8))
plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT (df_1)')

# Plot the values from df_2 against BackendTime
plt.plot(df_2['BackendTime'], df_2['ch1sens'], label='Post-choke PT', linestyle='--')

# Plot a horizontal line at y = 1.2
# plt.axhline(y=1.431, color='red', linestyle='-.', label='y = 1.431')
# plt.axhline(y=1.832, color='green', linestyle='-.', label='y = 1.832')
# Add labels and title
plt.xlabel('BackendTime')
plt.ylabel('Sensor Values')
plt.title('Sensor Values vs BackendTime (df_1 and df_2)')
plt.legend()

# Show the plot
plt.show()



# 1 was first test
# 2 - 4 were static pressure loss tests with clean tank

