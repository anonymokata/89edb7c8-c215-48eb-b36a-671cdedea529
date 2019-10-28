import unittest
import helpers.log_helper as logger_helper
import etc.config as config

from models.word_search_model import WordSearchModel
from models.char_coordinate_model import CharCoordinateModel

__author__ = 'Ken Langer'


class TestModels(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestModels, self).__init__(*args, **kwargs)
        self.classname = "TestModels"
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

    def test200_when_raw_word_search_rows_is_none_lists_are_empty(self):
        method = "test200_when_raw_word_search_rows_is_none_lists_are_empty"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        m = WordSearchModel(raw_word_search_rows=None)
        self.assertEqual(len(m.get_word_list()), 0, "get_word_list should be a length of zero")
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test250_when_x_and_y_are_returned_x_equals_col_and_y_equals_row(self):
        method = "test250_when_x_and_y_are_returned_x_equals_col_and_y_equals_row"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        c = CharCoordinateModel(c="X", row="5", col="6")
        self.assertEqual(c.get_col(), c.get_x(), msg=f"col={c.get_col()} does not equal x={c.get_x()}")
        self.assertEqual(c.get_row(), c.get_y(), msg=f"row={c.get_row()} does not equal y={c.get_y()}")
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test255_when_c_is_returned_value_matches_what_is_passed(self):
        method = "test255_when_c_is_returned_value_matches_what_is_passed"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        c = CharCoordinateModel(c="X", row="5", col="6")
        self.assertEqual(c.get_c(), "X", msg=f"c={c.get_c()} does not equal 'X'")
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
