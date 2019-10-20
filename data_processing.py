import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

FILE_PATH = "/Users/suenwailun/Sync Documents/University/Y4S1/BT4222 Mining Web Data for Business Insights/Assignments/Assignment 3/data_assignment3_students.csv"
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

def bin_dates(date_series:pd.Series, method="year", num_bins = 3, date_format="%d/%m/%Y"):
    """
    Takes in a series with dates, parses the datestrings, and bins them by year or by a specified number of bins
    """
    parsed_date_series = pd.to_datetime(date_series, format=date_format)
    if method == "bins":
        return pd.cut(parsed_date_series,bins=num_bins,labels=False)
    elif method == "year":
        return parsed_date_series.dt.year
