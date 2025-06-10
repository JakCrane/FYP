# import pandas as pd
# import matplotlib.pyplot as plt

# def read_mass_file_to_df(filename):
#     # Skip first 3 header lines, then read columns
#     df = pd.read_csv(
#         filename,
#         delim_whitespace=True,
#         skiprows=3,
#         names=['time_step', 'mass', 'flow_time']
#     )
#     return df

# if __name__ == "__main__":
#     filenames = [
#         "Research_Files/May/new_old_no_grav.out",
#         "Research_Files/May/new_old_grav.out",
#     ]

#     # Set global matplotlib rcParams for consistent styling
#     plt.rcParams.update({
#         'legend.fontsize': 24,
#         'lines.linewidth': 4,
#         'axes.labelsize': 28,
#         'xtick.labelsize': 24,
#         'ytick.labelsize': 24
#     })

#     dfs = []
#     for fname in filenames:
#         df = read_mass_file_to_df(fname)
#         dfs.append(df)
#     all_data = pd.concat(dfs, ignore_index=True)

#     plt.figure(figsize=(12, 8))
#     # Plot only the first file's data
#     subset = dfs[0]
#     plt.plot(subset['flow_time'], subset['mass'], color='orange')

#     plt.xlabel('Simulation Time (s)')
#     plt.ylabel('Integral of Volume Fraction')
#     plt.xlim(0, 10)
#     plt.ylim(0, 6)
#     plt.grid(True)
#     plt.tight_layout()
#     output_path = "latex/report_assets/old_design_out_no_grav.png"
#     plt.savefig(output_path)
#     plt.close()









import pandas as pd

import matplotlib.pyplot as plt

def read_mass_file_to_df(filename, label):
    # Skip first 3 header lines, then read columns
    df = pd.read_csv(
        filename,
        delim_whitespace=True,
        skiprows=3,
        names=['time_step', 'mass', 'flow_time']
    )
    df['label'] = label
    return df

if __name__ == "__main__":
    filenames = [
        "Research_Files/May/new_old_no_grav.out",
        "Research_Files/May/new_old_grav.out"
    ]
    labels = [
        "No Gravity",
        "With Gravity"
    ]

    # Set global matplotlib rcParams for consistent styling
    plt.rcParams.update({
        'legend.fontsize': 24,
        'lines.linewidth': 4,
        'axes.labelsize': 28,
        'xtick.labelsize': 24,
        'ytick.labelsize': 24
    })

    dfs = []
    for fname, label in zip(filenames, labels):
        df = read_mass_file_to_df(fname, label)
        dfs.append(df)
    all_data = pd.concat(dfs, ignore_index=True)

    plt.figure(figsize=(12, 8))
    for label in labels:
        subset = all_data[all_data['label'] == label]
        plt.plot(subset['flow_time'], subset['mass'], label=label)

    plt.xlabel('Simulation Time (s)')
    plt.ylabel('Amount of Powder in Tank')
    plt.xlim(0, 10)
    plt.ylim(0, 6)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    output_path = "latex/report_assets/old_design_out.png"
    plt.savefig(output_path)
    plt.close()
