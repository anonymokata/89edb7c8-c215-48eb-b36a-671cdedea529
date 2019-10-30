------
# Overview

_Word Search Kata_ is an implementation example that is based on a `specification` provided by Pillar Technology [located here](https://github.com/PillarTechnology/kata-word-search/blob/master/README.md).  

## Main Goals
 
The main goal is to create code that will solve a word search puzzle which supports finding words:
 
* Horizontally 
* Vertically
* Diagonally Ascending
* Diagonally Descending
* Reverse in any direction

## Terms

| Term       | Description                                                          |
|------------|----------------------------------------------------------------------|
| GRID       | Two dimensional array of characters that represents the word search. |
| Word List  | List of words to find within the GRID.                               |
 
## Considerations

* Words will **not** wrap around edges
* Words must be 2 characters or longer
* `GRID`s can be any size but must be square
* All words in the input file will be found in the `GRID`
* All characters in the `GRID` will be upper case.

## Input

The word search puzzle is described within the specification as a special CSV file.  

* First line has the list of words that are in the word search
* Second through `end-of-file` are the characters that make up the GRID
* All values are comma delimited.

### Example Input File

```
KAYLEE,DERRIAL,INARA,JAYNE,MALCOLM,RIVER,SIMON,WASH,ZOE
C,F,R,Y,M,R,R,G,C,L,J,E,K,V,O
W,G,H,U,Y,F,Z,R,A,Y,A,O,Y,B,H
C,N,I,M,K,B,I,I,N,T,Y,Z,K,T,P
H,Q,U,N,R,V,R,L,Z,N,N,L,B,J,V
F,Y,L,R,E,R,K,A,Y,L,E,E,O,I,G
N,N,D,R,E,Y,K,H,Y,P,S,A,I,D,C
Y,N,T,D,N,O,M,I,S,T,W,G,F,U,U
I,R,U,Z,S,T,F,R,U,A,Y,B,X,D,T
P,N,Z,D,G,R,E,S,H,O,W,M,U,W,S
B,J,A,V,H,D,C,N,P,C,M,L,X,G,C
Z,D,P,R,B,S,D,T,Y,V,T,O,F,Q,U
A,H,F,X,A,J,A,P,Q,V,A,C,K,W,M
S,V,J,P,J,B,O,W,W,J,W,L,S,Y,A
Q,O,A,Z,H,F,O,J,R,Y,B,A,S,A,R
N,O,B,I,S,W,T,Q,X,C,V,M,G,W,H
```

## Output

The output will be in the format of a `WORD` from the `Word List` and the (X
,Y) coordinates describing the position of each character of that word.  Each coordinate will be comma delimited.

The grid is ZERO based so C = (0,0) in the top left corner and H = (14,14) in the bottom right corner.  

### Example Output

```
Processing Word Search: data/sample/firefly_word_search.csv
KAYLEE: (6,4),(7,4),(8,4),(9,4),(10,4),(11,4)
DERRIAL: (3,6),(4,5),(5,4),(6,3),(7,2),(8,1),(9,0)
INARA: (0,7),(1,8),(2,9),(3,10),(4,11)
JAYNE: (10,0),(10,1),(10,2),(10,3),(10,4)
MALCOLM: (11,14),(11,13),(11,12),(11,11),(11,10),(11,9),(11,8)
RIVER: (7,1),(6,2),(5,3),(4,4),(3,5)
SIMON: (8,6),(7,6),(6,6),(5,6),(4,6)
WASH: (10,8),(9,7),(8,6),(7,5)
ZOE: (11,2),(11,1),(11,0)
```

**NOTE**: Within the code and logs, two dimensional arrays are used to store the `GRID`. These are stored in (row,col) format and are manipulated using variables like `row` and `col`.  The `row` and `col` values are translated to `x` and `y` as the results are displayed.

# Requirements and Setup

This application was developed using `Python 3.7`.  It is recommended that this same version or newer be used.  Python 3.7.4 was common at the time this was created.  

* It is expected that `python` or `python3` be in the path.  
* On Windows, `python` typically points to the latest python version so replace `python3` with `python` when running this application on Windows systems.

## Cloning

This project uses `git` as source control.  To use this project, simply clone the repo into a working directory.  Ensure `master` is the branch checked out.  For linux, macOS, or Window Subsystem for Linux; consider giving execute permissions to `word_search.py`.

```
% chmod +x word_seach.py
```

This way you can run `./word_search.py ....`.

## Virtual Environments

This project does not use any special libraries so `venv` is not required.

## Project Structure

| Directory      | Purpose                                           |
|----------------|---------------------------------------------------|
| ./controller   | Main business logic.                              |
| ./data         | Provided / Example Word Search CSV files.         |
| ./etc          | Configuration and version management.             |
| ./exceptions   | Any custom exceptions.                            |
| ./helpers      | Utility methods.                                  |
| ./_logs_       | Default location for logs. Will be auto created.  |
| ./models       | Objects for storing data.                         |
| ./repositories | Used for managing input/output files.             |
| ./test         | All unittests using the Python `unittest` package |
| ./             | Project root                                      |

# Usage

There are a few ways to launch this application depending on if you want to have it solve a word search or run unit-tests.  

To execute the following scenarios, navigate to the root directory the cloned project. This will likely be `word_search_kata` unless you cloned into a custom directory name. 

You can use your own word search CSV but there are examples in `data/test` and `data/sample`.  These files are used for unit-testing so they should not be modified. 

If you look at the link above for the Pillar Technology specifications, there is a reference to sites which can help you generate your own word search 

This has been tested using macOS 10.15 and Windows 10 (17.03).

## Command Line Syntax

IF you run the `word_search.py` with no arguments, you will get a little help page.

```
user@MBA word_search_kata % python3 word_search.py
APPLICATION:
    Word Search Kata 19.10.00
DESCRIPTION:
    Word Search Kata is an implementation example based on specification provided by
    Pillar Technology.  The goal is to programmatically solve a word search puzzle.
MORE INFORMATION:
    https://github.com/PillarTechnology/kata-word-search/blob/master/README.md
USAGE:
     Provide one or many word search formatted CSV files
     python3 word_search.py word_search_1.csv word_search_2.csv ... word_search_N.csv
EXAMPLE:
     python3 word_search.py word_search_A.csv word_search_B.csv
user@MBA % 
```

## Logging

Within the project root, there is a `logs` directory where you will find a log for `word_search.py` called `word_search_kata.log` and a separate log file for `unittesting` called `test_word_search_kata.log`.   The behavior of these logs is controlled in `etc/config.py`.  

## Running all Tests

To run all tests, run the following command from a terminal (bash, zsh, CMD,..) within the `project root` directory.

```
user@MBA word_search_kata % python3 -m unittest discover
```

There will be a lot of output to the console.  The logging (DEBUG, INFO, WARN,....) will be written to the log file for easier review.

## Running Specific Tests

To run the testing for just one area, you can specify the file that area is in.

```
% python3 -m unittest test/test100_grid_word_search.py
```

In this case, all the tests for the test class `Test100GridWordSearch` will be executed.

## Running Main Client Application

The following example will process two word search CSV files.  The number of files can be variable with one or many.  This is launched within the `project root` directory.

```
user@MBA word_search_kata % python3 word_search.py data/sample/firefly_word_search.csv data/
sample/star_trek_word_search.csv
```

The output will provide the file processed and the puzzle solution in the form of coordinates where each letter of the word was found.

```
Word Search Kata 19.10.00
 
Processing Word Search: data/sample/firefly_word_search.csv
KAYLEE: (6,4),(7,4),(8,4),(9,4),(10,4),(11,4)
DERRIAL: (3,6),(4,5),(5,4),(6,3),(7,2),(8,1),(9,0)
INARA: (0,7),(1,8),(2,9),(3,10),(4,11)
JAYNE: (10,0),(10,1),(10,2),(10,3),(10,4)
MALCOLM: (11,14),(11,13),(11,12),(11,11),(11,10),(11,9),(11,8)
RIVER: (7,1),(6,2),(5,3),(4,4),(3,5)
SIMON: (8,6),(7,6),(6,6),(5,6),(4,6)
WASH: (10,8),(9,7),(8,6),(7,5)
ZOE: (11,2),(11,1),(11,0)
 
Processing Word Search: data/sample/star_trek_word_search.csv
BONES: (0,6),(0,7),(0,8),(0,9),(0,10)
KHAN: (5,9),(5,8),(5,7),(5,6)
KIRK: (4,7),(3,7),(2,7),(1,7)
SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)
SULU: (3,3),(2,2),(1,1),(0,0)
UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)
user@MBA word_search_kata % 
```

# Troubleshooting / FAQ

### Tests will not run

Ensure that you are in the `project root` and not within a sub directory of the project.  Some of the tests use relative path to find data files.

### I am seeing string formatting errors

Be sure you are using `Python3.7` or newer.  Older versions of python do not support format strings `f"{my_variable} is a great variable}"`.  Check your python version.

### I tried one of the `data/test` files an am getting error messages

Some of the CSV files in `data/tests` purposely have bad data for testing.  Try files in the `data/sample` directory

### When I look at the coordinates within the logs they are reversed from the final output on the console

Within the code, characters in the grid are referenced by (row,column) notation.  This is much clearer to follow when coding.   Once the solution is determined, the results are returned in (X,Y) format.  `CharCoordinateModel` does this translation.

-----