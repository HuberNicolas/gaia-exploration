from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data" / "32130_AT2_25061944.csv"
OUTPUT_DIR = REPO_ROOT / "data_lab" / "output" / "excel"


def binarize_column(column, df, df_orig, positive_class):
    """
    Binarizes a specified column based on a positive class or classes and appends
    the binarized values to another DataFrame. It treats occurrences of the positive
    class(es) as 1 and all others as 0.

    Parameters:
    - column: the column name in 'df' to be binarized.
    - df: the DataFrame containing the column to be processed.
    - df_orig: the DataFrame to which the binarized values will be appended.
    - positive_class: a value or a list of values to be treated as the positive class (1).

    Returns:
    - df: the DataFrame with the added binarized column.
    - df_orig: the DataFrame with the binarized column values appended.
    """

    positive_classes = [positive_class] if isinstance(positive_class, str) else list(positive_class)

    # Directly create a binarized column based on whether the value is in positive_classes
    df[f"{column}_binarized"] = df[column].apply(lambda x: 1 if x in positive_classes else 0)

    # Mask to identify rows with non-null values in the original column
    mask = ~df[column].isnull()

    # Append the binarized values to df_orig based on the mask
    df_orig.loc[df.index[mask], f"{column}_applied_binarized"] = df.loc[mask, f"{column}_binarized"].values

    return df, df_orig


def main():
    df = pd.read_csv(filepath_or_buffer=DATA_FILE)

    df_orig = df.copy(deep=True)

    spytype_els_classes = df["SpType-ELS"].unique()

    # The first class in the file is B, so B becomes the positive class (1).
    # This matches the submitted task4.xlsx.
    positive_class = spytype_els_classes[0]
    df, df_orig = binarize_column("SpType-ELS", df, df_orig, positive_class)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_excel(OUTPUT_DIR / "task4.xlsx")


if __name__ == "__main__":
    main()
