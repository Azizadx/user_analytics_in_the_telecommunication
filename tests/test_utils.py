import unittest
import pandas as pd

from utlis import Utils


class TestUtils(unittest.TestCase):
    def setUp(self):

        data = {'A': [1, 2, 2, 3, 4],
                'B': [5, 6, 7, 8, 9]}
        self.df = pd.DataFrame(data)

    def test_drop_duplicates_and_count(self):
        utils = Utils()
        result_df = utils.drop_duplicates_and_count(self.df.copy())

        print("Original DataFrame:")
        print(self.df)

        print("\nExpected DataFrame after dropping duplicates:")
        print(self.df.drop_duplicates())

        print("\nActual DataFrame after dropping duplicates:")
        print(result_df)

        self.assertEqual(len(result_df), len(set(result_df['A'])))
        self.assertEqual(len(result_df), len(set(result_df['B'])))

    def test_view_columns_with_missing_value(self):
        utils = Utils()
        columns_with_missing_values = utils.view_columns_with_missing_value(
            self.df)
        self.assertEqual(len(columns_with_missing_values), 0)

    def test_view_percentage_of_missing_value(self):
        utils = Utils()
        missing_percentage = utils.view_percentage_of_missing_value(self.df)
        self.assertEqual(len(missing_percentage), len(self.df.columns))


if __name__ == '__main__':
    unittest.main()
