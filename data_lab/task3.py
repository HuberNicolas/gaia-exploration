from pathlib import Path

import pandas as pd
from sklearn.preprocessing import LabelEncoder

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data" / "32130_AT2_25061944.csv"
OUTPUT_DIR = REPO_ROOT / "data_lab" / "output" / "excel"


def discretize_column(column, df, df_orig, bins, categories):
    """
    Discretizes the specified column into categories based on bins, encodes the categories numerically,
    and appends the numerically encoded values to another DataFrame.

    Parameters:
    - column: the column name in 'df' to be discretized and encoded.
    - df: the DataFrame containing the column to be processed.
    - df_orig: the DataFrame to which the numerically encoded values will be appended.
    - bins: the bins used for discretization.
    - categories: the labels for the discretized categories.

    Returns:
    - df: the DataFrame with the added categorized and numerically encoded columns.
    - df_orig: the DataFrame with the numerically encoded column values appended.
    """

    # Discretize the column based on the provided bins and categories
    categorized_column_name = f"{column}_categorized"
    df[categorized_column_name] = pd.cut(df[column], bins=bins, labels=categories, right=False)

    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()

    # Fit and transform the categories to numeric values
    numeric_column_name = f"{column}_numeric"
    df[numeric_column_name] = label_encoder.fit_transform(df[categorized_column_name])

    # Mask to identify rows with non-null values in the categorized column
    mask = ~df[categorized_column_name].isnull()

    # Append the numerically encoded values to df_orig based on the mask
    df_orig.loc[df.index[mask], f"{column}_applied_category"] = df.loc[mask, categorized_column_name].values
    df_orig.loc[df.index[mask], f"{column}_applied_numeric"] = df.loc[mask, numeric_column_name].values

    return df, df_orig


def main():
    df = pd.read_csv(filepath_or_buffer=DATA_FILE)

    df_orig = df.copy(deep=True)

    # Introduce categories and the corresponding quantities
    mass_flame_categories = ["Small", "Medium", "Large"]
    mass_flame_bins = [0, 2, 4, 8]

    df, df_orig = discretize_column("Mass-Flame", df, df_orig, mass_flame_bins, mass_flame_categories)

    # Display the frequency of the categories
    frequencies = df["Mass-Flame_categorized"].value_counts()
    print(frequencies)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_excel(OUTPUT_DIR / "task3.xlsx")


if __name__ == "__main__":
    main()
