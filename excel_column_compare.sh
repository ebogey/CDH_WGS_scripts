#!bin/bash

##Need to have first arg the original excel file, 2nd arg is the first sheet to pull from, 3rd arg is the other sheet, 4th arg is the column to be comparing in both sheets (assumes both sheets are setup the same)

python ~/xlsx2csv-release-0.7/xlsx2csv.py -s $2 $1 $1.sheet$2.csv #Pull first sheet

python ~/xlsx2csv-release-0.7/xlsx2csv.py -s $3 $1 $1.sheet$3.csv #Pull second sheet

cut -d, -f $4 $1.sheet$2.csv >$1.sheet$2.col$4.txt #Cut commands pull the wanted column from each of the created csv files

cut -d, -f $4 $1.sheet$3.csv >$1.sheet$3.col$4.txt

vimdiff $1.sheet$2.col$4.txt $1.sheet$3.col$4.txt #Shows the differences in vim, should do this so an output file is created


