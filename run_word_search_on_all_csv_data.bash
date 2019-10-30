#!/usr/bin/env bash
#
# NAME:
#    Run Word Search on All CSV Data
#
# DESCRIPTION:
#    This script will process all the CSV files within the data/ sub-directory.
#    Please note that some of the CSV files have purpose made mistakes used  to
#    test the quality of the code processing them.   The type of error/mistake
#    should coorespond with the name of the file.  An apporpriate error message
#    should also be returned.
#
python3 word_search.py `find data -print |grep \.csv |awk '{printf("%s ",$1);}'`

# End of Script