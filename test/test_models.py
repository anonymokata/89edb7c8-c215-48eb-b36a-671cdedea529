import unittest
import helpers.log_helper as logger_helper
import etc.config as config

from models.word_search_model import WordSearchModel

__author__ = 'Ken Langer'


class TestModels(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestModels, self).__init__(*args, **kwargs)
        self.classname = "TestModels"
        self.log = logger_helper.get_logger(config.LOG_FILE)
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

    def test200_when_raw_word_search_rows_is_none_lists_are_empty(self):
        method = "test200_when_raw_word_search_rows_is_none_lists_are_empty"
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        m = WordSearchModel(raw_word_search_rows=None)
        self.assertEqual(len(m.get_word_list()), 0, "get_word_list should be a length of zero")
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
