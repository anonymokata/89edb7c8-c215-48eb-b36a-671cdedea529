# Overview

_Word Search Kata_ is an implementation example based on specification
 provided Pillar Technology [here](https://github.com/PillarTechnology/kata-word
 -search/blob/master/README.md).  

## Main Goals
 
 The main goal is to create code that solves a word search puzzle which
  supports finding words
 
 * Horizontally 
 * Vertically
 * Diagonally Ascending
 * Diagonally Descending
 * A word in reverse in any direction

## Terms

| Term       | Description                                              |
|------------|----------------------------------------------------------|
| Word List  | List of words to find                                    |
| GRID       | Square box of characters that represents the word search |
 
## Considerations

* Words will not wrap around edges
* Words will be 2 characters or longer
* `GRID`s can be any size but will be square
* All words in the input file will be found in the `GRID`
* All characters in the `GRID` will be upper case.

## Input

The word search puzzle is described in a special CSV file.  

* First line has the list of words that are in the word search
* Second through `end-of-file`

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
,Y) coordinates describing the position of each character of that word.

The grid is ZERO based so C = (0,0) above and H = (14,14).  

```
KAYLEE: (6,4)(7,4)(8,4)(9,4)(10,4)(11,4)
DERRIAL: (3,6)(4,5)(5,4)(6,3)(7,2)(8,1)(9,0)
INARA: (0,7)(1,8)(2,9)(3,10)(4,11)
JAYNE: (10,0)(10,1)(10,2)(10,3)(10,4)
MALCOLM: (11,14)(11,13)(11,12)(11,11)(11,10)(11,9)(11,8)
RIVER: (7,1)(6,2)(5,3)(4,4)(3,5)
SIMON: (8,6)(7,6)(6,6)(5,6)(4,6)
WASH: (10,8)(9,7)(8,6)(7,5)
ZOE: (11,2)(11,1)(11,0)
```

**NOTE**: Within the code and logs, two dimensional arrays are used to store the
 `GRID`. These are stored in (row,col) format and are manipulated using `row
 ` and `col`. 

# Requirements and Setup

This application was developed using `Python 3.7`.  It is recommended that
 this same version or newer be used.   

## Project Structure

| Directory    | Purpose                                          |
|--------------|--------------------------------------------------|
| controller   | Main business logic. |
| data         | Provided / Example Word Search CSV files.         |
| etc          | Configuration and version management.             |
| exceptions   | Any custom exceptions.                            |
| helpers      | Utility methods.                                  |
| _logs_       | Default location for logs. Will be auto created.  |
| models       | Objects for storing data.                         |
| repositories | Used for managing input/output files.             |
| test         | All uni tests using the Python `unittest` package |

# Usage

## Running all Unittests

## Running Main Client Application



