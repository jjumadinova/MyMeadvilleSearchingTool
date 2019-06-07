# My Meadville Youth Data

Data on youth from My Meadville interviews extracted by the learning algorithm.

## Results for youth-related keywords
Another set of programs is then run on the output of the learning algorithm. These programs
go through all of the folders that were generated by the learning algorithm and that are
located in the `output_files` folder.

## Original Data Files
The transcribed interview files are located inside the `input_files` folder.
These files were used as an input to the learning programs.

## Output from the learning algorithm
The algorithm goes through the input files and for each file, it extracts what it deems important
for a short summary and generates a list of keywords that appear frequently or are
considered important. This extracted information is stored in the `sum.md` file located
in the newly generated folder with the input file name as its name, which is in turn
located inside the `output_files` folder.

## Results for youth-related keywords
Another set of programs is then run on the output of the learning algorithm. These programs
go through all of the folders in the `output_files` directory that were generated by the learning algorithm 
and they seek to find matches to specific keywords in those
documents. Once a match found, the document name, the keyword, and 20 words surrounding
the keyword in the document are recorded in the `YouthData.md` file. The keywords that are
used for this search are:
* children
* grow meadville
* park
* parks
* play
* youth
* park programs
* teen
* summer
