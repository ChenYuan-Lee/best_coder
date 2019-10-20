import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

FILE_PATH = ""
data = pd.read_csv(FILE_PATH)

def correlation_with_target(dataframe: pd.DataFrame, target_column_name: str):
    # Compute Correlation between columns
    for column in dataframe:
        print(f'Correlation between {column} and target is {dataframe[target_column_name].corr(dataframe[column])}')

def find_missing_data(dataframe: pd.DataFrame):
    # Find out missing data percentage for columns which are missing data
    for column in dataframe:
        num_missing_data = dataframe[column].isna().sum()
        len_data =len(dataframe)
        if num_missing_data:
            print(f'Mising data rate for {column} is {(num_missing_data/len_data*100).round(2)}%')

def log_transform(series: pd.Series):
    return (series - series.min() + 1).transform(np.log)

