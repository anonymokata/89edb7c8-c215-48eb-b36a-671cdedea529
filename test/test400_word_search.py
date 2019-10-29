import unittest
import helpers.log_helper as logger_helper
import etc.config as config
from word_search import WordSearch

__author__ = 'Ken Langer'

#
# ERROR triggering CSV files
#
CSV_EMPTY = 'data/test/empty.csv'
CSV_MISSING = 'data/test/bogus_missing_file.csv'

#
# Sample Production Files
#
CSV_STAR_TREK = 'data/sample/star_trek_word_search.csv'
CSV_FIREFLY = 'data/sample/firefly_word_search.csv'


class Test400WordSearch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test400WordSearch, self).__init__(*args, **kwargs)
        self.classname = "Test400WordSearch"
        self.log = logger_helper.get_logger(config.TEST_LOG_FILE)
        return

    def setUp(self):
        method = "setUp"
        msg = f"SetUp for {config.CONST_APP_NAME} {config.CONST_APP_VERSION}"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=msg)
        )
        return

    def tearDown(self):
        method = "tearDown"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="TearDown Completed")
        )
        return

    def test400_when_word_search_is_created_with_bad_file_error_is_raised(self):
        method = "test400_when_word_search_is_created_with_bad_file_error_is_raised"
        csv_file = CSV_MISSING

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Expecting FileNotFoundException")
        )
        with self.assertRaises(FileNotFoundError, msg=f"FileNotFoundError should have been triggered"):
            _ = WordSearch(word_search_csv=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
