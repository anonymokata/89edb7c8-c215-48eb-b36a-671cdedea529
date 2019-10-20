import unittest
from repositories.word_search_repository import WordSearchRepository
from exceptions.file_format_exception import FileFormatException

#
# ERROR Triggering CSV files
#
CSV_EMPTY = 'data/test/empty.csv'
CSV_MISSING = 'data/test/bogus_missing_file.csv'

#
# GOOD CSV files
#
CSV_ABC_GOOD_GRID_GOOD_WORDS = 'data/test/abc_good_grid_good_words.csv'


class TestDataImportAndValidation(unittest.TestCase):
    def test005_when_missing_csv_is_opened_error_is_raised(self):
        method = 'test20_when_missing_csv_is_opened_error_is_raised'
        try:
            csv_file = CSV_MISSING
            repo = WordSearchRepository(csv_file=csv_file)
            self.fail(f"ERROR: {method} - {csv_file} should have triggered FileFormatException")

        except FileNotFoundError as ffe:
            print(f"SUCCESS: {method} - Received expected [{ffe}] for {csv_file}")

    def test010_when_empty_csv_is_read_error_is_raised(self):
        method = 'test10_when_empty_csv_is_read_error_is_raised'
        try:
            csv_file = CSV_EMPTY
            repo = WordSearchRepository(csv_file=csv_file)
            self.fail(f"ERROR: {method} - {csv_file} should have triggered FileFormatException")

        except FileFormatException as ffe:
            print(f"INFO: {method} - Received expected [{ffe}] for {csv_file}")


if __name__ == '__main__':
    unittest.main()
