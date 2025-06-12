import pandas as pd
import matplotlib.pyplot as plt

# Paths to your two Fluent output files
input_file1 = 'Research_Files/June/90mm_wide_wide.out'
input_file2 = 'Research_Files/June/30mm_wide_wide.out'

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

# Compute differences (mass change) between consecutive report_def_0 values
df1_diff = df1['report_def_0'].diff()
df2_diff = df2['report_def_0'].diff()

# Plot original comparison
plt.figure()
plt.plot(df1['flow_time'], df1['report_def_0'], label='1')
plt.plot(df2['flow_time'], df2['report_def_0'], label='2')
plt.xlabel('flow-time')
plt.ylabel('report-def-0 (mass)')
plt.title('Mass vs flow-time: two simulations')
plt.legend()
plt.tight_layout()
# plt.savefig('comparison_mass_vs_flow_time.png')
plt.show()
print("Saved comparison plot: comparison_mass_vs_flow_time.png")

# # Plot mass change (difference) vs flow_time
# plt.figure()
# plt.plot(df1['flow_time'].iloc[1:], df1_diff.iloc[1:], label='0.75 bar Δmass')
# plt.plot(df2['flow_time'].iloc[1:], df2_diff.iloc[1:], label='1.00 bar Δmass')
# plt.xlabel('flow-time')
# plt.ylabel('Δ report-def-0 (mass change)')
# plt.ylim([-0.1e-5, 0])
# plt.title('Mass change vs flow-time: two simulations')
# plt.legend()
# plt.tight_layout()
# plt.savefig('comparison_mass_change_vs_flow_time.png')
# print("Saved plot: comparison_mass_change_vs_flow_time.png")
