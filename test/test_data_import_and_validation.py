import unittest
from repositories.word_search_repository import WordSearchRepository
from exceptions.file_format_exception import FileFormatException
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


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
    def setUp(self):
        method = "setUp"
        self.classname = "TestDataImportAndValidation"
        self.log = logger_helper.get_logger(config.LOG_FILE)

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started")
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed")
        )
        return

    def test005_when_missing_csv_is_opened_error_is_raised(self):
        method = 'test20_when_missing_csv_is_opened_error_is_raised'
        csv_file = CSV_MISSING

        try:
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg="Expecting FileNotFoundException")
            )
            repo = WordSearchRepository(csv_file=csv_file)
            msg = f"FileNotFoundError should have been triggered"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
        except FileNotFoundError as ffe:
            msg = f"Received expected [{ffe}] for {csv_file}"
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )

    def test010_when_empty_csv_is_read_error_is_raised(self):
        method = 'test10_when_empty_csv_is_read_error_is_raised'
        csv_file = CSV_EMPTY

        try:
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg="Expecting FileFormatException")
            )
            repo = WordSearchRepository(csv_file=csv_file)
            msg = f"FileFormatException should have been triggered"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
        except FileFormatException as ffe:
            msg = f"Received expected [{ffe}] for {csv_file}"
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )


if __name__ == '__main__':
    unittest.main()
