from exceptions.file_format_exception import FileFormatException
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


class WordSearchRepository(object):
    def __init__(self, csv_file=None):
        method = "__init__"
        self.classname = "WordSearchRepository"
        self.log = logger_helper.get_logger(config.LOG_FILE)

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started")
        )

        self.__csv_file = csv_file
        self.__csv_data = self.__read_csv_file()
        self.__check_csv_length()

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed")
        )
        return

    def __read_csv_file(self):
        method = "__read_csv_file"
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Reading {self.__csv_file}")
        )

        with open(self.__csv_file) as fh:
            data = fh.readlines()

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg=f"Read {len(data)}")
        )
        return data

    def __check_csv_length(self):
        method = "__check_csv_length"
        if self.__csv_data is None:
            msg = f"raising FileFormatException {self.__csv_file} was unable to be read"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            raise FileFormatException(msg)
        elif len(self.__csv_data) == 0:
            msg = f"raising FileFormatException {self.__csv_file} is zero length"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            raise FileFormatException(msg)
        else:
            msg = f"{self.__csv_file} has a length of {len(self.__csv_data)}"
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
        return

#
# end of script
#
