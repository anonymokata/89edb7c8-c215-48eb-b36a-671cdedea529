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
CSV_ABC_GOOD_GRID_GOOD_WORDS = 'data/test/abc_grid_horiz_words.csv'


class TestGridWordSearch(unittest.TestCase):
    def setUp(self):
        method = "setUp"
        self.classname = "TestGridWordSearch"
        self.log = logger_helper.get_logger(config.LOG_FILE)

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

    def test105_when_horiz_word_is_in_grid_char_coordinates_are_returned(self):
        method = 'test105_when_horiz_word_is_in_grid_char_coordinates_are_returned'
        csv_file = CSV_ABC_GOOD_GRID_GOOD_WORDS
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started ------------------")
        )

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

            if not_found_count > 0:
                msg = f"{not_found_count} of {len(repo.get_word_search().get_word_list())} words not found in {csv_file}."
                self.log.error(
                    logger_helper.format_log(classname=self.classname, method=method, msg=msg)
                )
                self.fail(msg)
            else:
                pass

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

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed ----------------")
        )
        return


if __name__ == '__main__':
    unittest.main()

#
# end of script
#
