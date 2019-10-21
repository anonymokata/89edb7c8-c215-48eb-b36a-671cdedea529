class WordSearchModel(object):
    def __init__(self, raw_word_search_rows=None):
        if raw_word_search_rows:
            self.__raw_rows = raw_word_search_rows
            self.__word_list = self.__extract_word_list()
        else:
            self.__raw_rows = list()
        return

    def __extract_word_list(self):
        if len(self.__raw_rows) > 0:
            self.__raw_word_list = self.__raw_rows[0].strip()
            return self.__raw_word_list.split(",")
        else:
            return list()

    def get_word_list(self):
        return self.__word_list

#
# end of script
#
