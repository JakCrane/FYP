import pandas as pd
import matplotlib.pyplot as plt

# # Paths to your two Fluent output files
# input_file1 = 'Research_Files/June/90mm_wide_wide.out'
# input_file2 = 'Research_Files/June/60mm_wide_wide.out'
# input_file3 = 'Research_Files/June/30mm_wide_wide.out'

input_file1 = 'Research_Files/June/30mm_grav.out'
input_file2 = 'Research_Files/June/60mm_grav_initial.out'
input_file3 = 'Research_Files/June/90mm_grav.out'
def read_fluent_out(path):
    data = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or not line[0].isdigit():
                continue
            parts = line.split()
            if len(parts) == 3:
                data.append(parts)
    return pd.DataFrame(data, columns=['Time Step', 'report_def_0', 'flow_time'], dtype=float)

# Load datasets
df1 = read_fluent_out(input_file1)
df2 = read_fluent_out(input_file2)
df3 = read_fluent_out(input_file3)

# Compute differences (mass change) between consecutive report_def_0 values
df1_diff = df1['report_def_0'].diff()/-0.0001
df2_diff = df2['report_def_0'].diff()/-0.0001
df3_diff = df3['report_def_0'].diff()/-0.0001

# Plot original comparison
plt.figure()
plt.rc('legend', fontsize=24)   # Increase legend font size
plt.rc('lines', linewidth=4)    # Further increase line width
plt.rc('axes', labelsize=28)    # Increase axis label font size
plt.figure(figsize=(12, 8))    # Increase figure size
plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size

plt.plot(df1['flow_time'], df1['report_def_0'], label='90mm')
plt.plot(df2['flow_time'], df2['report_def_0'], label='60mm')
plt.plot(df3['flow_time'], df3['report_def_0'], label='30mm')
plt.xlabel('Simulation Time')
plt.ylabel('Amount of Powder in System')
plt.legend()
plt.tight_layout()
plt.savefig('latex/report_assets/sim_grav_amount.png')
# plt.show()

# Plot mass change (difference) vs flow_time
plt.figure()
plt.rc('legend', fontsize=24)   # Increase legend font size
plt.rc('lines', linewidth=4)    # Further increase line width
plt.rc('axes', labelsize=28)    # Increase axis label font size
plt.figure(figsize=(12, 8))    # Increase figure size
plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size

plt.plot(df1['flow_time'], df1_diff, label='90mm')
plt.plot(df2['flow_time'], df2_diff, label='60mm')
plt.plot(df3['flow_time'], df3_diff, label='30mm')
plt.xlabel('Simulation Time')
plt.ylabel('Powder Flow Rate')
plt.legend()
plt.tight_layout()
plt.savefig('latex/report_assets/sim_grav_rate.png')
