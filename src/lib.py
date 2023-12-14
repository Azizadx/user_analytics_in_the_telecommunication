import pandas as pd


class Lib:
    @staticmethod
    def get_top_3_manufacturer_handsets(df, manufacturer):
        # Filter the DataFrame based on the manufacturer name
        filtered_df = df.loc[df['Handset Manufacturer'] == manufacturer]

        # Group by Handset Manufacturer and Handset Type, then aggregate the count
        grouped_df = filtered_df.groupby(['Handset Manufacturer', 'Handset Type']).agg(
            count=('Handset Type', 'count'))

        # Select the top 5 handsets based on count
        top_handsets = grouped_df.nlargest(5, 'count')

        # Return the result
        return top_handsets
