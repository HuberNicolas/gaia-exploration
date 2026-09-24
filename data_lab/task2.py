from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data" / "32130_AT2_25061944.csv"
OUTPUT_DIR = REPO_ROOT / "data_lab" / "output" / "excel"



def scale_column(column, df, df_orig, method='minmax'):
    """
    Scales a column in 'df' using the specified 'method' and appends the scaled values to 'df_orig'.

    Parameters:
    - column: the column name in 'df' to be scaled.
    - df: the original DataFrame containing the column to be scaled.
    - df_orig: the DataFrame to which the scaled values will be appended.
    - method: the scaling method to use ('minmax', 'robust', 'softmax', or 'standard').

    Returns:
    - df: the DataFrame with the scaled column added.
    - df_orig: the DataFrame with the scaled column values appended.
    """

    # Select the scaler based on the 'method' parameter
    if method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    elif method == 'standard':
        scaler = StandardScaler()
    elif method == 'softmax':
        scaler = None  # handled below
    else:
        raise ValueError(f"Unsupported scaling method ({method}). Choose 'minmax', 'robust', 'softmax' or 'standard'.")

    # Reshape the data to (-1, 1) because it's a single feature
    values = df[column].values.reshape(-1, 1)

    # Apply the selected scaler
    if method == 'softmax':
        # Custom softmax scaling
        exp_values = np.exp(values - np.max(values))
        scaled_values = exp_values / np.sum(exp_values)
    else:
        # Scikit-learn scaling
        scaled_values = scaler.fit_transform(values)

    # Assign scaled values back to df with a new column name
    df[f'{column}_scaled_{method}'] = scaled_values.flatten()

    # Create a temporary Series for the scaled values with the same index as df
    scaled_series = pd.Series(scaled_values.flatten(), index=df.index)

    # Mask to identify rows with non-null values that were scaled
    mask = ~df[column].isnull()

    # Assign scaled values to df_orig based on the mask
    df_orig.loc[df.index[mask], f'{column}_applied_scaled_{method}'] = scaled_series[mask].values

    return df, df_orig


def main():
    df = pd.read_csv(filepath_or_buffer=DATA_FILE)

    df_orig = df.copy(deep=True)

    df, df_orig = scale_column('Age-Flame', df, df_orig, 'minmax')
    df, df_orig = scale_column('Age-Flame', df, df_orig, 'standard')

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_excel(OUTPUT_DIR / "task2.xlsx")


if __name__ == "__main__":
    main()
