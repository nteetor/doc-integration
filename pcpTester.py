#!/usr/bin/python2.7

import pcp, os

f = open('testFile1.txt')
pcp.main(f,None)
f.close()

# DIR_NAME="/Users/Teetor/Desktop/corpus/"
# RE_PATH="/Users/Teetor/Documents/Seventh Semester/Natural Language Processing/final project/code/testResults.csv"
# TEST_FILE=open(TEST_PATH,'a+')
# print TEST_FILE.name
# print TEST_FILE.closed

# #FILE=open(FILE_NAME)

# for f in os.listdir(DIR_NAME):
# 	if f[-4:] == ".txt":
# 		FILE = open(DIR_NAME+f)
# 		pcp.main(FILE,TEST_FILE)
# 		FILE.close()
# 	else:
# 		print f

# TEST_FILE.close()

