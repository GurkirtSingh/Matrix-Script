#!/bin/python


# Get number of raws and column (a comma seperate values) from first input line.
rawNcolumn = raw_input().rstrip().split()

num_raw = int(rawNcolumn[0])
num_column = int(rawNcolumn[1])

# Make a matrix list from input according to raws
matrix = []
for _ in range(num_raw):
  column_items = raw_input()
  matrix.append(column_items)
  
 # 

