import os
import uuid
import unittest
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


class Test300Helpers(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test300Helpers, self).__init__(*args, **kwargs)
        self.classname = "Test300Helpers"
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

    def test300_when_log_directory_is_missing_log_directory_is_created(self):
        method = "test300_when_log_directory_is_missing_log_directory_is_created"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        guid_sub_directory = str(uuid.uuid4())
        directory = os.path.join(config.LOG_DIR, guid_sub_directory)
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Creating {directory}")
        )
        logger_helper.create_logger_directory(directory=directory)
        self.assertTrue(os.path.exists(directory), msg=f"{directory} was not created or has a problem")
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Created {directory}")
        )
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Removing {directory}")
        )
        os.rmdir(directory)
        self.assertFalse(os.path.exists(directory), msg=f"{directory} could not be removed")

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test310_when_log_to_console_is_False_propagate_is_False(self):
        method = "test310_when_log_to_console_is_False_propagate_is_False"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )
        old_propagate = self.log.propagate
        logger_helper.set_log_propagation(log=self.log, log_to_console=False)
        self.assertFalse(self.log.propagate, msg=f"self.log.propagate expected to be False preventing console logging")

        # Setting propagate back to original value
        logger_helper.set_log_propagation(log=self.log, log_to_console=old_propagate)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

    def test320_when_log_to_console_is_True_propagate_is_True(self):
        method = "test320_when_log_to_console_is_True_propagate_is_True"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

        old_propagate = self.log.propagate
        logger_helper.set_log_propagation(log=self.log, log_to_console=True)
        self.assertTrue(self.log.propagate, msg=f"self.log.propagate expected to be True which allows console logging")

        # Setting propagate back to original value
        logger_helper.set_log_propagation(log=self.log, log_to_console=old_propagate)

        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return

#
# end of script
#
