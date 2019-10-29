from repositories.word_search_repository import WordSearchRepository
from controllers.word_search_controller import WordSearchController
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


class WordSearch(object):
    def __init__(self, word_search_csv=None):
        self.classname = "WordSearch"
        method = "__init__"
        self.log = logger_helper.get_logger(config.LOG_FILE, log_to_console=False)
        msg = f"SetUp for {config.CONST_APP_NAME} {config.CONST_APP_VERSION}"
        self.log.info(
            logger_helper.format_log(classname=self.classname, method=method, msg=msg)
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started")
        )
        self.__word_search_csv = word_search_csv
        self.__word_search_repository = WordSearchRepository(csv_file=word_search_csv)
        self.__word_search_controller = WordSearchController(
            grid=self.__word_search_repository.get_word_search().get_grid()
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed")
        )
        return

    def get_word_list_as_strings(self):
        method = "get_word_list_as_strings"
        word_list_as_strings = list()
        word_list = self.__word_search_repository.get_word_search().get_word_list()
        for w in word_list:
            result = self.__word_search_controller.find_word(word_as_chars=w)
            word_str = ''.join(w)
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"Adding {str(w)} as {word_str}")
            )
            word_list_as_strings.append(word_str)

        return word_list_as_strings

    def get_solution(self):
        method = "get_solution"
        word_list = self.__word_search_repository.get_word_search().get_word_list()
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting Search for {len(word_list)} words")
        )
        results_dict = dict()
        for w in word_list:
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"Searching for {str(w)}")
            )
            result = self.__word_search_controller.find_word(word_as_chars=w)
            word_str = ''.join(w)
            xy_coords = ''
            if len(result) > 0:
                for coord_char in result:
                    xy_coords += f"({coord_char.get_x()},{coord_char.get_y()})"

            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"Found {word_str} {xy_coords}")
            )
            results_dict[word_str] = xy_coords

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Returning {len(results_dict)} search results")
        )
        return results_dict


if __name__ == '__main__':
    w = WordSearch("data/sample/firefly_word_search.csv")
    #w = WordSearch("data/sample/star_trek_word_search.csv")

#
# end of script
#
