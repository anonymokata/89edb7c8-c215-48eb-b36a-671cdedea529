from exceptions.file_format_exception import FileFormatException
from exceptions.grid_dimension_exception import GridDimensionException
from exceptions.word_length_exception import WordLengthException
from models.word_search_model import WordSearchModel
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
        self.__word_search_model = WordSearchModel(raw_word_search_rows=self.__csv_data)
        self.__check_word_length()
        self.__check_grid_size()

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed")
        )
        return

    def get_word_search(self):
        return self.__word_search_model

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

    def __check_word_length(self):
        method = "__check_word_length"
        for w in self.get_word_search().get_word_list():
            if len(w) < config.MIN_WORD_LENGTH:
                msg = f"raising WordLengthException - {w} is {len(w)} which FAILS minimum of {config.MIN_WORD_LENGTH}"
                self.log.error(
                    logger_helper.format_log(classname=self.classname, method=method, msg=msg)
                )
                raise WordLengthException(msg)
            else:
                msg = f"{w} is {len(w)} which passes minimum of {config.MIN_WORD_LENGTH}"
                self.log.debug(
                    logger_helper.format_log(classname=self.classname, method=method, msg=msg)
                )
        return

    def __check_grid_size(self):
        method = "__check_grid_size"
        if len(self.get_word_search().get_grid()) > 0:
            pass
        else:
            msg = f"raising GridDimensionException since grid is missing"
            self.log.error(
                logger_helper.format_log(classname=self.classname, method=method, msg=msg)
            )
            raise GridDimensionException(msg)
        return

#
# end of script
#
