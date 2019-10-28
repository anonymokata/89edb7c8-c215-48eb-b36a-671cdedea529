import os
import logging

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
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "word_search_kata.log")
TEST_LOG_FILE = os.path.join(LOG_DIR, "test_word_search_kata.log")
FILE_ENCODING = "utf-8"
LOG_LEVEL = logging.INFO

#
# word search constants
#
MIN_WORD_LENGTH = 2

#
# end of file
#
