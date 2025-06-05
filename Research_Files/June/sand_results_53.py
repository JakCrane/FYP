# import matplotlib.pyplot as plt
# import pandas as pd

# # Read the CSV files
# input_file_1 = 'Research_Files/June/5_bar_sand/3_kermit106.csv'  # 0 2 7
# input_file_2 = 'Research_Files/June/5_bar_sand/3_kermit108.csv'  # 0 1 7

# # Load the data into a DataFrame
# df_1 = pd.read_csv(input_file_1)
# df_2 = pd.read_csv(input_file_2)

# # Keep only the specified columns
# df_1 = df_1[['BackendTime', 'ch0sens', 'ch2sens', 'ch7sens']]
# df_2 = df_2[['BackendTime', 'ch0sens', 'ch1sens', 'ch7sens']]

# # Rescale BackendTime to seconds and set the first value to 0
# df_1['BackendTime'] = (df_1['BackendTime'] - 1748811694990) / 1e3
# df_2['BackendTime'] = (df_2['BackendTime'] - 1748811694990) / 1e3

# # Replace any values in 'ch1sens' column of df_2 above 3 with 0
# # df_2['ch1sens'] = df_2['ch1sens'].apply(lambda x: None if x > 3 else x)
# # df_2['ch7sens'] = df_2['ch7sens'].apply(lambda x: None if x > 3 else x)

# df_1 = df_1[(df_1['BackendTime'] >= 29) & (df_1['BackendTime'] <= 75)]
# df_2 = df_2[(df_2['BackendTime'] >= 29) & (df_2['BackendTime'] <= 75)]
# # df_2['ch7sens'] = df_2['ch7sens'].apply(lambda x: None if x is not None and x < 0 else x)


# plt.rc('legend', fontsize=24)   # Increase legend font size
# plt.rc('lines', linewidth=4)    # Further increase line width
# plt.rc('axes', labelsize=28)    # Increase axis label font size
# plt.figure(figsize=(12, 8))    # Increase figure size
# plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
# plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size
# # plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT (df_1)')
# plt.plot(df_1['BackendTime'], df_1['ch2sens'], label='Start of Tank', color='blue')
# plt.plot(df_1['BackendTime'], df_1['ch7sens'], label='End of Tank', color='red')
# plt.plot(df_2['BackendTime'], df_2['ch7sens'], label='Cyclone Seperator', color='orange')
# # Plot the sum of 'ch2sens' and 'ch7sens' from df_1
# # plt.plot(
# #     df_1['BackendTime'],
# #     df_1['ch2sens'] + df_1['ch7sens'],
# #     label='Combined Tank Load Cell',
# #     linestyle=':'
# # )
# # Plot the values from df_2 against BackendTime
# # plt.plot(df_2['BackendTime'], df_2['ch0sens'], label='Pre-choke PT', linestyle='--')
# # plt.plot(df_2['BackendTime'], df_2['ch1sens'], label='Post-choke PT', linestyle='--')
# plt.axvline(x=36.2, color='green', linestyle='--')
# plt.axvline(x=67.0, color='green', linestyle='--')
# # Remove all values before 8 seconds
# # Add labels and title
# plt.xlabel('Experiment Time (s)')
# plt.ylabel('Load Cell Values (kg)')
# plt.ylim(0.1, 2.1)
# plt.legend()
# # Show the plot
# plt.savefig('./latex/report_assets/53_raw_mass.png')
# df_1['ch2plus7'] = df_1['ch2sens'] + df_1['ch7sens']
# # Save cleaned DataFrames to new CSV files
# df_1.to_csv(input_file_1.replace('.csv', '_clean.csv'), index=False)
# df_2.to_csv(input_file_2.replace('.csv', '_clean.csv'), index=False)


# import matplotlib.pyplot as plt
# import pandas as pd

# # Read the CSV files
# input_file_1 = 'Research_Files/June/5_bar_sand/3_kermit106_clean.csv'  # 0 2 7
# input_file_2 = 'Research_Files/June/5_bar_sand/3_kermit108_clean.csv'  # 0 1 7

# # Load the data into a DataFrame
# df_1 = pd.read_csv(input_file_1)
# df_2 = pd.read_csv(input_file_2)

# # Keep only the specified columns
# df_1 = df_1[['BackendTime', 'ch0sens', 'ch2sens', 'ch2plus7']]
# df_2 = df_2[['BackendTime', 'ch0sens', 'ch1sens', 'ch7sens']]


# plt.rc('legend', fontsize=24)   # Increase legend font size
# plt.rc('lines', linewidth=4)    # Further increase line width
# plt.rc('axes', labelsize=28)    # Increase axis label font size
# plt.figure(figsize=(12, 8))    # Increase figure size
# plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
# plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size
# # plt.plot(df_1['BackendTime'], df_1['ch0sens'], label='Inlet PT (df_1)')
# # plt.plot(df_1['BackendTime'], df_1['ch2sens'], label='Start of Tank')
# # plt.plot(df_1['BackendTime'], df_1['ch7sens'], label='End of Tank')
# plt.plot(df_1['BackendTime'], df_1['ch2plus7'], label='Combined Tank', color='purple')
# plt.plot(df_2['BackendTime'], df_2['ch7sens'], label='Cyclone Seperator', color='orange')
# # Plot the sum of 'ch2sens' and 'ch7sens' from df_1
# # Plot the values from df_2 against BackendTime
# # plt.plot(df_2['BackendTime'], df_2['ch0sens'], label='Pre-choke PT', linestyle='--')
# # plt.plot(df_2['BackendTime'], df_2['ch1sens'], label='Post-choke PT', linestyle='--')
# plt.axvline(x=36.2, color='green', linestyle='--')
# plt.axvline(x=67.0, color='green', linestyle='--')
# # Remove all values before 8 seconds
# # Add labels and title
# plt.xlabel('Experiment Time (s)')
# plt.ylabel('Load Cell Values (kg)')
# plt.legend()

# # # Show the plot
# plt.savefig('./latex/report_assets/53_clean_mass.png')


import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV files
input_file_1 = 'Research_Files/June/5_bar_sand/3_kermit106_clean.csv'  # 0 2 7
input_file_2 = 'Research_Files/June/5_bar_sand/3_kermit108_clean.csv'  # 0 1 7

# Load the data into a DataFrame
df_1 = pd.read_csv(input_file_1)
df_2 = pd.read_csv(input_file_2)

df_1 = df_1[['BackendTime', 'ch0sens', 'ch2sens', 'ch2plus7']]
df_2 = df_2[['BackendTime', 'ch0sens', 'ch1sens', 'ch7sens']]

df_1['ch2plus7'] = -1*df_1['ch2plus7']
df_1['m_flow'] = df_1['ch2plus7'].diff()
df_2['m_flow'] = df_2['ch7sens'].diff()
# Apply a rolling mean to smooth the curves
window_size = 100  # Adjust as needed for smoothing
df_1['smooth_combined'] = df_1['ch2plus7'].rolling(window=window_size, center=True, min_periods=1).mean()
df_2['smooth_ch7sens'] = df_2['ch7sens'].rolling(window=window_size, center=True, min_periods=1).mean()

df_1['m_flow_smooth'] = df_1['smooth_combined'].diff()
df_2['m_flow_smooth'] = df_2['smooth_ch7sens'].diff()

plt.rc('legend', fontsize=24)   # Increase legend font size
plt.rc('lines', linewidth=4)    # Further increase line width
plt.rc('axes', labelsize=28)    # Increase axis label font size
plt.figure(figsize=(12, 8))    # Increase figure size
plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size

plt.plot(df_1['BackendTime'], df_1['m_flow_smooth'], label='Combined Tank', color='purple')
plt.plot(df_2['BackendTime'], df_2['m_flow_smooth'], label='Cyclone Seperator', color='orange')

plt.axvline(x=36.2, color='green', linestyle='--')
plt.axvline(x=67.0, color='green', linestyle='--')

plt.xlabel('Experiment Time (s)')
plt.ylabel('Load Cell Values (kg)')
plt.legend()

# # Show the plot
plt.savefig('./latex/report_assets/53_clean_flow_100.png')
