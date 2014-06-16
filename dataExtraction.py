#!/usr/bin/python2.7

from nltk import pos_tag
from pprint import pprint
from os import listdir
from string import letters, octdigits
from nltk import FreqDist as fd
from csv import reader as csvReader
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import WhitespaceTokenizer

def mean(l):
	return sum(l)/len(l) if len(l)>0 else 0

def convertTag(tag):
	nounTags = ['NN','NNP','NNS','NNPS']
	verbTags = ['VB','VBD','VBG','VBN','VBP','VBZ']
	adjTags = ['JJ','JJR','JJS']
	advTags = ['RB','RBR','RBS']

	if tag in nounTags:
		return 'n'
	elif tag in verbTags:
		return 'v'
	elif tag in adjTags:
		return 'a' 
	elif tag in advTags:
		return 'r'
	else:
		return None 

resultsFile = open('corpusData.csv','r')

# files that we have already looked at
skipOver = [row[0] for row in csvReader(resultsFile, delimiter=',')]

# some screwy stuff was happening
resultsFile.close()

resultsFile = open('corpusData.csv','a+')

for f in listdir('corpus/'):
 	if f[-4:] == ".txt" and not f in skipOver:
 		fileName = f

 		F = open('corpus/'+f)
 		text = F.read()
 		F.close()

		alphanum = letters+octdigits

		paragraphs = [s for s in text.split("\n\n") if s != "" ][:-1]
		numParagraphs = len(paragraphs)

		# average paragraph size
		wst = WhitespaceTokenizer()
		paraWordCounts = [len(wst.tokenize(p)) for p in paragraphs]

		# the approximate number of words in the document
		numWords = sum(paraWordCounts)

		# the average number of words per paragraph
		avgParagraphLen = mean(paraWordCounts)

		# rejoin the paragraphs
		text = ' '.join(paragraphs)

 		# part of speech word list for the text
 		text = [word for subl in [pos_tag(wt(s)) for s in st(text)] for word in subl]

 		# remove symbols from list by checking the first character of the word
 		text = [word for word in text if word[0][0] in alphanum]

 		# convert words to lowercase and convert Penn Tree Bank tags to WordNet tags
 		text = [(word[0].lower(), convertTag(word[1])) for word in text]

 		# remove Nones
 		text = [word for word in text if word[1]]

 		nouns = [word for word in text if word[1] == 'n']
 		numNouns = len(nouns)

 		verbs = [word for word in text if word[1] == 'v']
 		numVerbs = len(verbs)

 		adjectives = [word for word in text if word[1] == 'a']
 		numAdjectives = len(adjectives)

 		adverbs = [word for word in text if word[1] == 'r']
 		numAdverbs = len(adverbs)

 		numTargetWords = numNouns+numVerbs+numAdjectives+numAdverbs

 		finalOutput = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (fileName,numWords,numParagraphs,avgParagraphLen,numNouns,numVerbs, numAdjectives,numAdverbs,numTargetWords)

 		print finalOutput

 		# write output to csv file
 		resultsFile.write(finalOutput+'\n')

 	else:
 		print 'Skipping %s' % (f)

resultsFile.close()