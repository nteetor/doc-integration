import re, random, os, sys
from sys import exit
from pprint import pprint
from itertools import combinations
from string import letters, octdigits
from nltk import pos_tag, FreqDist
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt


def mean(L):
	''' Because Python has no mean function '''
	return sum(L)/len(L)

def sim(tokens):
	'''
	A function which takes a list of tokens (where each token is a string of words) and determines the tokens' similarity 
	NOTE: 'tokens' must be of length 3 due to simplification of implementation
	'''
	def simHelper(T):
		'''
		Given a token returns a pos tagged list 
		'''
		alphanum = letters+octdigits

		# part of speech word list for the text
		fullList = [word for subl in [pos_tag(wt(s)) for s in st(T)] for word in subl]

		# remove symbols and -NONE- tags from list by checking the first character of the word and tag
		posList = [word for word in fullList if word[1][0] in alphanum and word[0][0] in alphanum]

		return posList


	def tagFilter(item):
		pos = item[1]
		word = item[0]
		isNoun = pos in ['NN','NNP','NNS','NNPS']
		isYear = pos == 'CD' and len(word) == 4
		return isNoun or isYear

	# part of speech tag each token using the helper function
	taggedSet = [simHelper(t) for t in tokens]

	# remove none noun or year words from the tagged set
	targetSet = [[t[0].lower() for t in subl if tagFilter(t)] for subl in taggedSet]

	# convert all word lists to sets
	setSet = [set(t) for t in tokens]

	# a flattened version of targetSet for word count purposes
	flatSet = [w for subl in targetSet for w in subl]

	# woo hoo, TODO: convert to list comprehension
	intersectSum = len(setSet[0].intersection(setSet[1]))+len(setSet[1].intersection(setSet[2]))+len(setSet[0].intersection(setSet[2]))
	intersectSum = 1.0*intersectSum/(3.0*len(set(flatSet))) if len(set(flatSet)) != 0 else 0

	return intersectSum


def PCP(texts):
	''' Paragraph Combination Probability	'''
	return sim(texts)






	