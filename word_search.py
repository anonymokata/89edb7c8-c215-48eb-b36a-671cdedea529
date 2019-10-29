from repositories.word_search_repository import WordSearchRepository
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


class WordSearch(object):
    def __init__(self, word_search_csv=None):
        self.classname = "WordSearch"
        self.method = "__init__"
        self.log = logger_helper.get_logger(config.LOG_FILE, log_to_console=False)

        self.__word_search_csv = word_search_csv
        self.__word_search_repository = WordSearchRepository(csv_file=word_search_csv)

        return


if __name__ == '__main__':
    w = WordSearch("data/sample/firefly_word_search.csv")
    #w = WordSearch("data/sample/star_trek_word_search.csv")

#
# end of script
#
