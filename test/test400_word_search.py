import unittest
import os
import helpers.log_helper as logger_helper
import etc.config as config
import word_search
from word_search import WordSearch
from exceptions.file_format_exception import FileFormatException
from exceptions.grid_dimension_exception import GridDimensionException

__author__ = 'Ken Langer'

#
# ERROR triggering CSV files
#
CSV_EMPTY = 'data/test/empty.csv'
CSV_MISSING = 'data/test/bogus_missing_file.csv'
CSV_BAD_GRID = 'data/test/abc_bad_grid_good_words.csv'
CSV_NOTFOUND_WORDS = 'data/test/abc_good_grid_notfound_words.csv'

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

    def test410_when_word_search_is_created_with_empty_file_error_is_raised(self):
        method = "test410_when_word_search_is_created_with_empty_file_error_is_raised"
        csv_file = CSV_EMPTY

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Expecting FileFormatException")
        )
        with self.assertRaises(FileFormatException, msg=f"FileFormatException should have been triggered"):
            _ = WordSearch(word_search_csv=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test420_when_word_search_is_created_with_bad_grid_error_is_raised(self):
        method = "test420_when_word_search_is_created_with_bad_grid_error_is_raised"
        csv_file = CSV_BAD_GRID

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Expecting GridDimensionException")
        )
        with self.assertRaises(GridDimensionException, msg=f"GridDimensionException should have been triggered"):
            _ = WordSearch(word_search_csv=csv_file)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test430_when_word_search_searches_for_words_all_are_found(self):
        method = "test430_when_word_search_searches_for_words_all_are_found"
        csv_file = CSV_STAR_TREK

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        word_search = WordSearch(word_search_csv=csv_file)
        result_dict = word_search.get_solution()
        for w_str in word_search.get_word_list_as_strings():
            self.assertTrue(w_str in result_dict, msg=f"{w_str} is not in results with {len(result_dict)}")
            self.assertTrue(len(result_dict[w_str]), msg=f"{w_str} has no value so nothing was found")

        for w in result_dict:
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=f"{w} {result_dict[w]}")
            )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test440_when_word_search_searches_for_notfound_words_no_coordinates_are_returned(self):
        method = "test440_when_word_search_searches_for_notfound_words_no_coordinates_are_returned"
        csv_file = CSV_NOTFOUND_WORDS

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        word_search = WordSearch(word_search_csv=csv_file)
        result_dict = word_search.get_solution()
        for w_str in word_search.get_word_list_as_strings():
            self.assertTrue(w_str in result_dict, msg=f"{w_str} is not in results with {len(result_dict)}")
            self.assertFalse(len(result_dict[w_str]), msg=f"{w_str} has no value so nothing was found")

        for w in result_dict:
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=f"{w} {result_dict[w]}")
            )

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test450_when_main_is_called_with_no_file_zero_is_returned(self):
        method = "test450_when_main_is_called_with_no_file_zero_is_returned"

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        arg_list = list()
        arg_list.append(os.path.join(os.curdir, "dummy.py"))

        self.assertEqual(0, word_search.main(argv=arg_list), "Expected zero since no file was provided")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test460_when_main_is_called_with_one_file_one_is_returned(self):
        method = "test460_when_main_is_called_with_one_file_one_is_returned"

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        arg_list = list()
        arg_list.append(os.path.join(os.curdir, "dummy.py"))
        arg_list.append(CSV_STAR_TREK)

        self.assertEqual(1, word_search.main(argv=arg_list), "Expected one since a good file was provided")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test465_when_main_is_called_with_two_files_two_is_returned(self):
        method = "test465_when_main_is_called_with_two_files_two_is_returned"

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        arg_list = list()
        arg_list.append(os.path.join(os.curdir, "dummy.py"))
        arg_list.append(CSV_STAR_TREK)
        arg_list.append(CSV_FIREFLY)

        self.assertEqual(2, word_search.main(argv=arg_list), "Expected two since two good files were provided")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test470_when_main_is_called_with_notfound_file_zero_is_returned(self):
        method = "test470_when_main_is_called_with_notfound_file_zero_is_returned"

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        arg_list = list()
        arg_list.append(os.path.join(os.curdir, "dummy.py"))
        arg_list.append(CSV_MISSING)

        self.assertEqual(0, word_search.main(argv=arg_list), "Expected zero since a missing file was provided")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test480_when_main_is_called_with_empty_file_zero_is_returned(self):
        method = "test480_when_main_is_called_with_empty_file_zero_is_returned"

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        arg_list = list()
        arg_list.append(os.path.join(os.curdir, "dummy.py"))
        arg_list.append(CSV_EMPTY)

        self.assertEqual(0, word_search.main(argv=arg_list), "Expected zero since an empty file was provided")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test490_when_main_is_called_with_bad_grid_file_zero_is_returned(self):
        method = "test490_when_main_is_called_with_bad_grid_file_zero_is_returned"

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        arg_list = list()
        arg_list.append(os.path.join(os.curdir, "dummy.py"))
        arg_list.append(CSV_BAD_GRID)

        self.assertEqual(0, word_search.main(argv=arg_list), "Expected zero since a file was provided that has a bad grid")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
