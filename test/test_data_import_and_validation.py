import unittest
from repositories.word_search_repository import WordSearchRepository
from exceptions.file_format_exception import FileFormatException

CSV_EMPTY = 'data/test/empty.csv'


class TestDataImportAndValidation(unittest.TestCase):
    def test10_when_empty_csv_is_read_error_is_raised(self):
        try:
            csv_file = CSV_EMPTY
            repo = WordSearchRepository(csv_file=csv_file)
            self.fail(f"ERROR: {csv_file} should have triggered FileFormatException")

        except FileFormatException as ffe:
            print(f"Received expected [{ffe}] for {csv_file}")


if __name__ == '__main__':
    unittest.main()
