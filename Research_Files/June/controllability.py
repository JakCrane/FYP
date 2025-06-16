import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    # 'Pressure': [2.66, 2.66, 2.66, 3.08, 3.08, 3.08, 3.51, 3.51, 3.51],
    'Pressure': [4, 4, 4, 5, 5, 5, 6, 6, 6],
    'Mass Flow Rate': [20, 24, 29, 34, 32, 40, 55, 53, 40],
}
df = pd.DataFrame(data)
import matplotlib.pyplot as plt

# # Scatter plot
# plt.scatter(df['Pressure'], df['Mass Flow Rate'], color='blue', label='Data')

# # Fit a line through the origin (y = m*x), must pass through (0, 0)
# # Least squares solution for y = m*x
# m = np.dot(df['Pressure'], df['Mass Flow Rate']) / np.dot(df['Pressure'], df['Pressure'])
# x_vals = np.linspace(0, df['Pressure'].max(), 100)
# y_vals = m * x_vals

# # Plot line of best fit
# plt.plot(x_vals, y_vals, color='red', label='Best Fit (through 0,0)')
# plt.xlabel('Pressure')
# plt.ylabel('Mass Flow Rate')
# plt.legend()
# plt.grid(True)
# plt.show()

# Scatter plot
plt.figure(figsize=(18, 12))    # Make figure even larger
plt.grid(True, linewidth=3, zorder=0)
plt.scatter(df['Pressure'], df['Mass Flow Rate'], color='blue', label='Experimental Data', s=600, zorder=3)  # Increase marker size and set zorder above grid

# Fit a line through the origin (y = m*x), must pass through (0, 0)
# Least squares solution for y = m*x
m = np.dot(df['Pressure'], df['Mass Flow Rate']) / np.dot(df['Pressure'], df['Pressure'])
# Fit a standard line of best fit (y = m*x + c)
coeffs = np.polyfit(df['Pressure'], df['Mass Flow Rate'], 1)
m, c = coeffs
x_vals = np.linspace(df['Pressure'].min(), df['Pressure'].max(), 100)
y_vals = m * x_vals + c

# Plot line of best fit
plt.plot(x_vals, y_vals, color='red', label='Best Fit', linewidth=10)  # Thicker line

plt.xlabel('Stagnation Pressure (bar)', fontsize=48, labelpad=30)
plt.ylabel('Mass Flow Rate (g/s)', fontsize=48, labelpad=30)
plt.legend(fontsize=32, loc='upper left')
plt.xticks(fontsize=32)
plt.yticks(fontsize=32)
plt.tight_layout(pad=4)
plt.savefig('./latex/report_assets/controllability_py_raw.png')
