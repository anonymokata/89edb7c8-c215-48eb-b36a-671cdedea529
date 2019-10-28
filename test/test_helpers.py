import os
import uuid
import unittest
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


class TestHelpers(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHelpers, self).__init__(*args, **kwargs)
        self.classname = "TestHelpers"
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

    def test300_when_raw_word_search_rows_is_none_lists_are_empty(self):
        method = "test200_when_raw_word_search_rows_is_none_lists_are_empty"
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        guid_sub_directory = str(uuid.uuid4())
        directory = os.path.join(config.LOG_DIR, guid_sub_directory)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Creating {directory}")
        )
        logger_helper.create_logger_directory(directory=directory)
        self.assertTrue(os.path.exists(directory), msg=f"{directory} was not created or has a problem")
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Created {directory}")
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Removing {directory}")
        )
        os.rmdir(directory)
        self.assertFalse(os.path.exists(directory), msg=f"{directory} could not be removed")

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
