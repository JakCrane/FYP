import pandas as pd
import matplotlib.pyplot as plt


input_file1 = 'Research_Files/June/60mm_grav.out'
input_file2 = 'Research_Files/June/60mm_grav_initial.out'
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

# Plot original comparison
plt.figure()
plt.rc('legend', fontsize=24)   # Increase legend font size
plt.rc('lines', linewidth=4)    # Further increase line width
plt.rc('axes', labelsize=28)    # Increase axis label font size
plt.figure(figsize=(12, 8))    # Increase figure size
plt.rc('xtick', labelsize=24)   # Increase x-axis tick font size
plt.rc('ytick', labelsize=24)   # Increase y-axis tick font size

plt.plot(df1['flow_time'], df1['report_def_0'], label='0.0001s time step')
plt.plot(df2['flow_time'], df2['report_def_0'], label='0.00005s time step')
plt.xlabel('Simulation Time')
plt.ylabel('Amount of Powder in System')
plt.legend()
plt.tight_layout()
plt.savefig('latex/report_assets/fluent_sucks.png')
# plt.show()
