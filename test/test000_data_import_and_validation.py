import unittest
from repositories.word_search_repository import WordSearchRepository
from exceptions.file_format_exception import FileFormatException
from exceptions.word_length_exception import WordLengthException
from exceptions.grid_dimension_exception import GridDimensionException

import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'

#
# ERROR Triggering CSV files
#
CSV_EMPTY = 'data/test/empty.csv'
CSV_MISSING = 'data/test/bogus_missing_file.csv'
CSV_ABC_GOOD_GRID_BAD_WORDS = 'data/test/abc_good_grid_bad_words.csv'
CSV_ABC_MISSING_GRID_GOOD_WORDS = 'data/test/abc_missing_grid_good_words.csv'
CSV_ABC_BAD_GRID_GOOD_WORDS = 'data/test/abc_bad_grid_good_words.csv'

#
# GOOD CSV files
#
CSV_ABC_GOOD_GRID_GOOD_WORDS = 'data/test/abc_good_grid_good_words.csv'


class Test000DataImportAndValidation(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test000DataImportAndValidation, self).__init__(*args, **kwargs)
        self.classname = "Test000DataImportAndValidation"
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

    def test005_when_missing_csv_is_opened_error_is_raised(self):
        method = 'test20_when_missing_csv_is_opened_error_is_raised'
        csv_file = CSV_MISSING
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Expecting FileNotFoundException")
        )

        with self.assertRaises(FileNotFoundError, msg=f"FileNotFoundError should have been triggered"):
            _ = WordSearchRepository(csv_file=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test010_when_empty_csv_is_read_error_is_raised(self):
        method = 'test10_when_empty_csv_is_read_error_is_raised'
        csv_file = CSV_EMPTY

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Expecting FileFormatException")
        )

        with self.assertRaises(FileFormatException, msg=f"FileFormatException should have been triggered"):
            _ = WordSearchRepository(csv_file=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test020_when_good_csv_is_read_a_word_list_is_found(self):
        method = 'test020_when_good_csv_is_read_a_word_list_is_found'
        csv_file = CSV_ABC_GOOD_GRID_GOOD_WORDS
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        repo = WordSearchRepository(csv_file=csv_file)
        self.assertGreater(len(repo.get_word_search().get_word_list()), 0, msg=f"Could not find words in {csv_file}")

        for w in repo.get_word_search().get_word_list():
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=f"Word {w}")
            )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test025_when_word_list_is_short_error_is_raised(self):
        method = 'test025_when_word_list_is_short_error_is_raised'
        csv_file = CSV_ABC_GOOD_GRID_BAD_WORDS
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Expecting WordLengthException")
        )

        with self.assertRaises(WordLengthException, msg=f"WordLengthException should have been triggered"):
            _ = WordSearchRepository(csv_file=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test030_when_good_csv_is_read_a_grid_is_found(self):
        method = 'test030_when_good_csv_is_read_a_grid_is_found'
        csv_file = CSV_ABC_GOOD_GRID_GOOD_WORDS
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        repo = WordSearchRepository(csv_file=csv_file)

        for r in repo.get_word_search().get_grid():
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=f"Row {r}")
            )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test035_when_grid_is_missing_error_is_raised(self):
        method = 'test025_when_grid_is_missing_error_is_raised'
        csv_file = CSV_ABC_MISSING_GRID_GOOD_WORDS
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="GridDimensionException Expected")
        )

        with self.assertRaises(GridDimensionException, msg=f"GridDimensionException should have been triggered"):
            _ = WordSearchRepository(csv_file=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test037_when_grid_is_not_square_error_is_raised(self):
        method = 'test037_when_grid_is_not_square_error_is_raised'
        csv_file = CSV_ABC_BAD_GRID_GOOD_WORDS
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
        )
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="GridDimensionException Expected")
        )

        with self.assertRaises(GridDimensionException, msg=f"GridDimensionException should have been triggered"):
            _ = WordSearchRepository(csv_file=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
