# This file contains solution for "Matrix Script" problem on the HackerRank website.
# Link to the problem:- https://www.hackerrank.com/challenges/matrix-script/problem

# Resources:-
# https://docs.python.org/3/library/re.html
# https://regexr.com/
# https://stackoverflow.com/questions/51505166/python-re-sub-grab-a-single-character-from-a-group

import re
from typing import final
# Get number of raws and column (a comma seperate values) from first input line.
rawNcolumn = input().rstrip().split()

num_raw = int(rawNcolumn[0])
num_column = int(rawNcolumn[1])

# Make a list from input according to raws
matrix = []
for _ in range(num_raw):
  matrix.append(input())

# conevrt matrix to a string, which is written in column format
parsed_string = ''
for i in range(num_column):
  for j in range(num_raw):
    parsed_string += matrix[j][i]

# create a regular-expression to search non-alphanumaric characters and space between two alphanumaric characters
data_re = re.compile(r'([\w]{1}[\W]+[\w]{1})')

# find and replace matches to first and last char with space between eg. "a b"
final_string = re.sub(data_re, lambda m: "{} {}".format(m.group(1)[0], m.group(1)[-1]), parsed_string)
print(final_string)






