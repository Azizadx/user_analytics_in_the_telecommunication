import pandas as pd


class Utils:
    @staticmethod
    def drop_duplicates_and_count(df):
        # Display the original DataFrame
        print("Original DataFrame:")
        print(df)

        # Count the number of duplicates
        num_duplicates = df.duplicated().sum()

        # Drop duplicates
        df = df.drop_duplicates()

        # Display the DataFrame after dropping duplicates
        print("\nDataFrame after dropping duplicates:")
        print(df)

        # Return the count of dropped duplicates
        return df

    @staticmethod
    def view_columns_with_missing_value(df):
        # Display the columns with missing values
        print("Columns with missing values:")
        return df.columns[df.isnull().any()]

    @staticmethod
    def view_percentage_of_missing_value(df):
        missing_percentage = (df.isnull().sum()/len(df)) * 100
        print("Percentage of missing value ")
        return missing_percentage
