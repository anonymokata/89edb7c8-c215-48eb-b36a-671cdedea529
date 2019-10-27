class WordSearchModel(object):
    CONST_ROW = "ROW"
    CONST_COL = "COL"

    def __init__(self, raw_word_search_rows=None):
        if raw_word_search_rows:
            self.__raw_rows = raw_word_search_rows
        else:
            self.__raw_rows = list()

        self.__raw_word_list = self.__extract_raw_word_list()
        self.__raw_grid_rows = self.__extract_raw_grid_rows()
        self.__grid = self.__build_grid()
        self.__word_list = self.__build_word_list()
        return

    def get_word_list(self):
        return self.__word_list

    def get_grid(self):
        return self.__grid

    def get_grid_dimension(self):
        dimensions_dict = dict()
        grid = self.get_grid()

        dimensions_dict[WordSearchModel.CONST_ROW] = len(grid)
        dimensions_dict[WordSearchModel.CONST_COL] = len(grid[0])

        return dimensions_dict

    def __extract_raw_word_list(self):
        if len(self.__raw_rows) > 0:
            self.__raw_word_list = self.__raw_rows[0].strip()
            return self.__raw_word_list.split(",")
        else:
            return list()

    def __extract_raw_grid_rows(self):
        raw_grid_rows = list()
        if len(self.__raw_rows) > 1:
            row_num = 0
            for r in self.__raw_rows:
                if row_num > 0:
                    raw_grid_rows.append(r.strip())
                else:
                    pass
                row_num += 1
        else:
            pass
        return raw_grid_rows

    def __build_grid(self):
        grid_list = list()
        if len(self.__raw_grid_rows) > 1:
            for r in self.__raw_grid_rows:
                char_array = r.split(",")
                grid_list.append(char_array)
        else:
            pass
        return grid_list

    def __build_word_list(self):
        word_list = list()
        for w in self.__raw_word_list:
            char_array = list(w)
            word_list.append(char_array)
        return word_list

#
# end of script
#
