import unittest
from controllers.word_search_controller import WordSearchController
from repositories.word_search_repository import WordSearchRepository
from exceptions.file_format_exception import FileFormatException
from exceptions.word_length_exception import WordLengthException
from exceptions.grid_dimension_exception import GridDimensionException

import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'

#
# GOOD CSV files
#
CSV_ABC_GRID_HORIZ_WORDS = 'data/test/abc_good_grid_horiz_words.csv'
CSV_ABC_GRID_HORIZ_REVERSE_WORDS = 'data/test/abc_good_grid_horiz_reverse_words.csv'
CSV_ABC_GRID_VERT_WORDS = 'data/test/abc_good_grid_vert_words.csv'
CSV_ABC_GRID_VERT_REVERSE_WORDS = 'data/test/abc_good_grid_vert_reverse_words.csv'
CSV_ABC_GRID_DIAG_ASC_WORDS = 'data/test/abc_good_grid_diag_asc_words.csv'
CSV_ABC_GRID_DIAG_ASC_REVERSE_WORDS = 'data/test/abc_good_grid_diag_asc_reverse_words.csv'
CSV_ABC_GRID_DIAG_DESC_WORDS = 'data/test/abc_good_grid_diag_desc_words.csv'
CSV_ABC_GRID_DIAG_DESC_REVERSE_WORDS = 'data/test/abc_good_grid_diag_desc_reverse_words.csv'

#
# GOOD CSV with NotFound Data
#
CSV_ABC_GRID_NOTFOUND_WORDS = 'data/test/abc_good_grid_notfound_words.csv'


class TestGridWordSearch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGridWordSearch, self).__init__(*args, **kwargs)
        self.classname = "TestGridWordSearch"
        self.log = logger_helper.get_logger(config.TEST_LOG_FILE)
        return

    def setUp(self):
        method = "setUp"
        msg = f"SetUp for {config.CONST_APP_NAME} {config.CONST_APP_VERSION}"
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg=msg)
        )
        return

    def tearDown(self):
        method = "tearDown"
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="TearDown Completed")
        )
        return

    def test000_when_controller_is_not_passed_a_grid_error_is_raised(self):
        method = "test000_when_controller_is_not_passed_a_grid_error_is_raised"
        try:
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
            )
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg="Expecting ValueError")
            )

            _ = WordSearchController(grid=None)

            msg = f"ValueError should have been triggered"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            self.fail(msg)
        except ValueError as ve:
            msg = f"Received expected [{ve}]"
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test105_when_horiz_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test105_when_horiz_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_HORIZ_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test110_when_reverse_horiz_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test110_when_reverse_horiz_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_HORIZ_REVERSE_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test120_when_vert_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test120_when_vert_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_VERT_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test125_when_reverse_vert_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test125_when_reverse_vert_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_VERT_REVERSE_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test130_when_diag_asc_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test130_when_diag_asc_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_DIAG_ASC_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test135_when_reverse_diag_asc_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test135_when_reverse_diag_asc_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_DIAG_ASC_REVERSE_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test140_when_diag_desc_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test140_when_diag_desc_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_DIAG_DESC_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test145_when_reverse_diag_desc_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test145_when_reverse_diag_desc_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GRID_DIAG_DESC_REVERSE_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test150_when_words_are_notfound(self):
        method = 'test150_when_words_are_notfound_'
        csv_file = CSV_ABC_GRID_NOTFOUND_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        self.__main_test_executor(csv_file=csv_file, not_found_ok=True)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def __main_test_executor(self, csv_file=None, not_found_ok=False):
        method = '__main_test_executor'

        try:
            self.log.info(
                logger_helper.format_log(classname=self.classname, method=method, msg=f"Using {csv_file}")
            )
            repo = WordSearchRepository(csv_file=csv_file)
            controller = WordSearchController(grid=repo.get_word_search().get_grid())

            not_found_count = len(repo.get_word_search().get_word_list())
            for w in repo.get_word_search().get_word_list():
                self.log.info(
                    logger_helper.format_log(classname=self.classname, method=method, msg=f"Searching for {w}")
                )
                coord_list = controller.find_word(word_as_chars=w)
                if len(coord_list) > 0:
                    not_found_count -= 1
                    self.log.info(
                        logger_helper.format_log(classname=self.classname, method=method, msg=f"{w} FOUND")
                    )
                    c_string = ""
                    for c in coord_list:
                        c_string += f"{str(c)} "
                    self.log.info(
                        logger_helper.format_log(classname=self.classname, method=method, msg=f"{c_string} FOUND")
                    )
                else:
                    self.log.warning(
                        logger_helper.format_log(classname=self.classname, method=method, msg=f"{w} NOT FOUND")
                    )

            if not_found_count > 0 and not not_found_ok:
                msg = f"{not_found_count} of {len(repo.get_word_search().get_word_list())} words notfound in {csv_file}"
                self.log.error(
                    logger_helper.format_log(classname=self.classname, method=method, msg=msg)
                )
                self.fail(msg)
            elif not_found_count > 0:
                msg = f"{not_found_count} of {len(repo.get_word_search().get_word_list())} words notfound in {csv_file}"
                self.log.info(
                    logger_helper.format_log(classname=self.classname, method=method, msg=msg)
                )
            else:
                msg = f"All {len(repo.get_word_search().get_word_list())} words were found in {csv_file}."
                self.log.info(
                    logger_helper.format_log(classname=self.classname, method=method, msg=msg)
                )

        except FileFormatException as ffe:
            msg = f"Received Exception of [{ffe}] for {csv_file}"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            self.fail(msg)
        except WordLengthException as wle:
            msg = f"Received Exception of [{wle}] for {csv_file}"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            self.fail(msg)
        except GridDimensionException as gde:
            msg = f"Received Exception of [{gde}] for {csv_file}"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            self.fail(msg)
        return

#
# end of script
#
