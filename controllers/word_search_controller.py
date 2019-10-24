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
        if len(coord_list) < 1:
            coord_list = self.__search_vertical(word_as_chars=word_as_chars)
            if len(coord_list) < 1:
                coord_list = self.__search_horizontal_reverse(word_as_chars=word_as_chars)
                if len(coord_list) < 1:
                    coord_list = self.__search_vertical_reverse(word_as_chars=word_as_chars)
                    if len(coord_list) < 1:
                        coord_list = self.__search_diagonal_ascending(word_as_chars=word_as_chars)
                        if len(coord_list) < 1:
                            coord_list = self.__search_diagonal_ascending_reverse(word_as_chars=word_as_chars)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

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
                                     msg=f"row_len={row_len} by col_len={col_len}")
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

    def __search_horizontal_reverse(self, word_as_chars=None):
        method = "__search_horizontal_reverse"
        word_as_chars_reverse = list()
        word_as_chars_reverse.extend(word_as_chars)
        word_as_chars_reverse.reverse()

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Original HORIZ Search {str(word_as_chars)}")
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting REVERSE HORIZ Search {str(word_as_chars_reverse)}")
        )
        tmp_coord_list = self.__search_horizontal(word_as_chars=word_as_chars_reverse)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"RETURNING {len(tmp_coord_list)} matching characters")
        )

        coord_list = list()
        coord_list.extend(tmp_coord_list)
        coord_list.reverse()

        return coord_list

    def __search_vertical(self, word_as_chars=None):
        method = "__search_vertical"
        match_char_list = None
        char_list = list()
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting VERT Search {str(word_as_chars)}")
        )

        row_len = len(self.__grid)
        if row_len > 0:
            col_len = len(self.__grid[0])
        else:
            col_len = 0

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"row_len={row_len} by col_len={col_len}")
        )

        for col_pos in range(0, col_len):
            char_list.clear()

            for row_pos in range(0, row_len):
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

    def __search_vertical_reverse(self, word_as_chars=None):
        method = "__search_vertical_reverse"
        word_as_chars_reverse = list()
        word_as_chars_reverse.extend(word_as_chars)
        word_as_chars_reverse.reverse()

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Original VERT Search {str(word_as_chars)}")
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting REVERSE VERT Search {str(word_as_chars_reverse)}")
        )
        tmp_coord_list = self.__search_vertical(word_as_chars=word_as_chars_reverse)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"RETURNING {len(tmp_coord_list)} matching characters")
        )

        coord_list = list()
        coord_list.extend(tmp_coord_list)
        coord_list.reverse()

        return coord_list

    def __search_diagonal_ascending(self, word_as_chars=None):
        method = "__search_diagonal_ascending"
        match_char_list = None
        char_list = list()
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting DIAG ASC Search {str(word_as_chars)}")
        )
        row_len = len(self.__grid)
        if (row_len > 0):
            col_len = len(self.__grid[0])
        else:
            col_len = 0

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"row_len={row_len} by col_len={col_len}")
        )
        for col_pos in range(0, col_len):
            char_list.clear()

            for row_pos in range(0, (row_len - col_pos)):
                r = row_pos
                c = col_pos + r
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

        if len(match_char_list) < 1:
            for row_pos in range(1, row_len):
                char_list.clear()

                for col_pos in range(0, (col_len - row_pos)):
                    c = col_pos
                    r = row_pos + c
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

    def __search_diagonal_ascending_reverse(self, word_as_chars=None):
        method = "__search_diagonal_ascending_reverse"
        word_as_chars_reverse = list()
        word_as_chars_reverse.extend(word_as_chars)
        word_as_chars_reverse.reverse()

        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Original VERT Search {str(word_as_chars)}")
        )
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Starting REVERSE DIAGONAL ASCENDING Search {str(word_as_chars_reverse)}")
        )
        tmp_coord_list = self.__search_diagonal_ascending(word_as_chars=word_as_chars_reverse)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"RETURNING {len(tmp_coord_list)} matching characters")
        )

        coord_list = list()
        coord_list.extend(tmp_coord_list)
        coord_list.reverse()

        return coord_list

    def __find_in_char_list(self, word_as_chars=None, char_list_from_grid=None):
        method = "__find_in_char_list"
        match_char_list = list()
        found_count = 0

        char_list_from_grid_as_string = self.__char_list_from_grid_to_string(char_list_from_grid=char_list_from_grid)
        self.log.debug(
            logger_helper.format_log(classname=self.classname, method=method,
                                     msg=f"Search for {str(word_as_chars)} in {char_list_from_grid_as_string}")
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
                                         msg=f"{str(word_as_chars)} is longer then {len(char_list_from_grid)} SKIPPING")
            )

        if len(match_char_list) == len(word_as_chars):
            self.log.debug(
                logger_helper.format_log(classname=self.classname, method=method,
                                         msg=f"RETURNING {len(match_char_list)} matching characters")
            )
            return match_char_list
        else:
            return list()

    @staticmethod
    def __char_list_from_grid_to_string(char_list_from_grid=None):
        s = ""
        for coord in char_list_from_grid:
            s += f"{str(coord)} "
        return s.strip()

#
# end of script
#
