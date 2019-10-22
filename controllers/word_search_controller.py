from models.char_coordinate_model import CharCoordinateModel
import helpers.log_helper as logger_helper
import etc.config as config

__author__ = 'Ken Langer'


class WordSearchController(object):
    def __init__(self, grid=None):
        method = "__init__"
        self.classname = "WordSearchController"
        self.log = logger_helper.get_logger(config.LOG_FILE)

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Started")
        )
        if grid:
            self.__grid = grid
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method, msg=f"GRID {str(self.__grid)}")
            )
        else:
            raise ValueError("GRID cannot be None")

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method, msg="Completed")
        )
        return

    def find_word(self, word_as_chars=None):
        method = "find_word"
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Searching for {str(word_as_chars)}")
        )
        coord_list = self.__search_horizontal(word_as_chars=word_as_chars)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Found {len(coord_list)} chars")
        )
        return coord_list

    def __search_horizontal(self, word_as_chars=None):
        method = "__search_horizontal"
        match_char_list = None
        char_list = list()
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting HORIZ Search {str(word_as_chars)}")
        )

        row_len = len(self.__grid)
        if row_len > 0:
            col_len = len(self.__grid[0])
        else:
            col_len = 0

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"row_len={row_len} x col_len={col_len}")
        )

        for row_pos in range(0, row_len):
            char_list.clear()

            for col_pos in range(0, col_len):
                c = col_pos
                r = row_pos
                if r in range(0, row_len) and c in range(0, col_len):
                    coordinate = CharCoordinateModel(c=self.__grid[r][c], row=r, col=c)
                    char_list.append(coordinate)
                else:
                    coordinate = CharCoordinateModel("#", row=r, col=c)
                    self.log.warning(
                        logger_helper.format_log(classname=self.classname, method=method,
                                                 msg=f"{str(coordinate)} is out of bounds. Breaking out.")
                    )
                    break

            match_char_list = self.__find_in_char_list(word_as_chars=word_as_chars, char_list_from_grid=char_list)

            if len(match_char_list) > 0:
                break
            else:
                pass

        if match_char_list:
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"RETURNING {len(match_char_list)} matching characters")
            )
            return match_char_list
        else:
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"RETURNING 0 matching characters")
            )
            return list()

    def __find_in_char_list(self, word_as_chars=None, char_list_from_grid=None):
        method = "__find_in_char_list"
        match_char_list = list()
        found_count = 0

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Search for {str(word_as_chars)} in char_list_from_grid")
        )

        if len(word_as_chars) <= len(char_list_from_grid):
            for col_pos in range(0, len(char_list_from_grid)):
                for w in range(0, len(word_as_chars)):
                    if word_as_chars[w] == char_list_from_grid[col_pos].get_c():
                        match_char_list.append(char_list_from_grid[col_pos])
                        found_count += 1
                    else:
                        match_char_list.clear()
                        found_count = 0
                    col_pos += 1
                    if col_pos >= len(char_list_from_grid):
                        break

                if found_count == len(word_as_chars):
                    break
                else:
                    pass
        else:
            self.log.warning(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"{str(word_as_chars)} is longer then {len(char_list_from_grid)}")
            )

        if len(match_char_list) == len(word_as_chars):
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"RETURNING {len(match_char_list)} matching characters")
            )
            return match_char_list
        else:
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"RETURNING 0 matching characters")
            )
            return list()

#
# end of script
#
