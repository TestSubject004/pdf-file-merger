# pdf-file-merger
merge multiple pdf files scattered over a bunch of directories

HOW TO USE - 

put the file in the root directory where your pdf files are and run the script

if you have a bunch of other directories, the script will look inside them, merge those files and output a result.pdf

CAUTION: THIS SCRIPT WILL ONLY MERGE THE FILES INSIDE A DIRECTORY. IT WILL NOT NOT MERGE FILES THAT ARE AT DIFFERENT LEVELS

example : if you have 3 pdf files in root directory and 4  files inside a directory inside the root directory, it will merge the 3 files as one in the root directory. It will merge the other 4 files in a separate merge file in that other directory. one result.pdf file per directory.
