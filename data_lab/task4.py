import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder


import numpy as np
import pandas as pd


def binarize_column(column, df, df_orig, positive_class):
    """
    Binarizes a specified column based on a positive class or classes and appends
    the binarized values to another DataFrame. It treats occurrences of the positive
    class(es) as 1 and all others as 0.

    Parameters:
    - column: the column name in 'df' to be binarized.
    - df: the DataFrame containing the column to be processed.
    - df_orig: the DataFrame to which the binarized values will be appended.
    - positive_class: a list of unique values to be treated as the positive class (1).

    Returns:
    - df: the DataFrame with the added binarized column.
    - df_orig: the DataFrame with the binarized column values appended.
    """

    # Directly create a binarized column based on whether the value is in positive_classes
    df[f'{column}_binarized'] = df[column].apply(lambda x: 1 if x in positive_classes else 0)

    # Mask to identify rows with non-null values in the original column
    mask = ~df[column].isnull()

    # Append the binarized values to df_orig based on the mask
    df_orig.loc[df.index[mask], f'{column}_applied_binarized'] = df.loc[mask, f'{column}_binarized'].values

    return df, df_orig


df = pd.read_csv(filepath_or_buffer="./data/32130_AT2_25061944.csv")

df_orig = df.copy(deep=True)

spytype_els_classes = df['SpType-ELS'].unique()
spytype_els_classes[1]

positive_classes = spytype_els_classes[0] # define A as positive class
df, df_orig = binarize_column('SpType-ELS', df, df_orig, positive_classes)

df.to_excel('./data_lab/output/excel/task4.xlsx')
