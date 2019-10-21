import os

__author__ = 'Ken Langer'

#
# application information
#
CONST_APP_NAME = "Word Search Kata"
CONST_APP_VERSION = "19.10.00"
#
# logging formatter
#
FORMAT = '%(asctime)-15s: %(levelname)-7s - %(message)s'
LOG_FILE = os.path.join("logs", "word_search_kata.log")
FILE_ENCODING = "utf-8"

#
# word search constants
#
MIN_WORD_LENGTH = 2

#
# end of file
#
