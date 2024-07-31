# Equi-width binning
import numpy as np
import pandas as pd

import math

def equi_width_binning(series, n_bins):
    min_value, max_value = series.min(), series.max()
    bin_edges = np.linspace(min_value, max_value, n_bins + 1)

    # Use pd.cut to handle the binning based on calculated edges
    bins = pd.cut(series, bins=bin_edges, labels=False, include_lowest=True)

    return bins

# Equi-depth binning
def equi_depth_binning(series, n_bins):
    sorted_series = series.sort_values()
    values_per_bin = len(series) // n_bins

    bins = pd.Series(index=series.index, dtype=int)
    for i, (index, value) in enumerate(sorted_series.items()):
        bins.at[index] = i // values_per_bin

    bins = bins.clip(upper=n_bins-1)

    return bins


df = pd.read_csv(filepath_or_buffer="./data/32130_AT2_25061944.csv")

# Define number of bins based on common best-practices; might be adjusted later
n_bins =  round(math.sqrt(df.shape[0]))


# Equi-width binning on RA_ICRS
df[f'RA_ICRS_equip_width_{n_bins}'] = equi_width_binning(df['RA_ICRS'], n_bins=n_bins)

# Equi-depth binning on RA_ICRS
df[f'RA_ICRS_equip_depth_{n_bins}'] = equi_depth_binning(df['RA_ICRS'], n_bins=n_bins)

# Equi-width binning on DE_ICRS
df[f'DE_ICRS_equip_width_{n_bins}'] = equi_width_binning(df['DE_ICRS'], n_bins=n_bins)

# Equi-depth binning on DE_ICRS
df[f'DE_ICRS_equip_depth_{n_bins}'] = equi_depth_binning(df['DE_ICRS'], n_bins=n_bins)

df.to_excel('./data_lab/output/excel/task1.xlsx')