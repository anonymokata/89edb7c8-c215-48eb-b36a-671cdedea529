from exceptions.file_format_exception import FileFormatException


class WordSearchRepository(object):
    def __init__(self, csv_file=None):
        self.__csv_file = csv_file
        self.__csv_data = self.__read_csv_file()
        self.__check_csv_length()
        return

    def __read_csv_file(self):
        with open(self.__csv_file) as fh:
            data = fh.readlines()
        return data

    def __check_csv_length(self):
        if self.__csv_data is None:
            raise FileFormatException(f"{self.__csv_file} was unable to be read")
        elif len(self.__csv_data) == 0:
            raise FileFormatException(f"{self.__csv_file} is zero length")
        else:
            pass
        return

#
# end of script
#
