#!/usr/bin/python2.7

from os import listdir
from sys import exit
from csv import reader as csvReader
from random import randint
from numpy import repeat
from pprint import pprint
from pcp import PCP
from SimilarityMethods import FST, MCS

resultsFile = open('methodData.csv','r')

# files that we have already looked at
skipOver = [row[0] for row in csvReader(resultsFile, delimiter=',')]

# some screwy stuff was happening
resultsFile.close()

resultsFile = open('methodData.csv','a+')

for f in listdir('corpus/'):
  	if f[-4:] == ".txt" and not f in skipOver:
		fileName = f

		F = open('corpus/'+f)
		text = F.read()
		F.close()

		paragraphs = [s for s in text.split("\n\n") if s != "" ][:-1]

		# the index of the paragraph to sample
		if len(paragraphs) >= 3:
			index = randint(1,len(paragraphs)-2) if len(paragraphs) > 3 else 1
		# if the file is strange and 
		else :
			strangeFile = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (fileName,0,0,0,0,0,0,0,0,0,0)
			print strangeFile
			resultsFile.write(strangeFile+'\n')
			continue

		# will PCP end up better than guessing?
		guess = randint(0,len(paragraphs)-1)

		chanceResult = 1 if index == guess else 0

		# pull out of the paragraph
		sampledParagraph = paragraphs.pop(index)

		# repeat sample n amount of times
		rep = repeat(sampledParagraph,len(paragraphs))

		# consecutive pairs of paragraphs with the sampled paragraph attached
		paraPairs = zip(paragraphs[:-1], paragraphs[1:], rep)

		# the sampled paragraph with the two paragraphs it is supposed to be between
		actualTriple = [paragraphs[index-1], paragraphs[index], sampledParagraph]

		pcpActual = PCP(actualTriple)
		pcpScore = max([(PCP(p),p) for p in paraPairs], key = lambda x : x[0])
		pcpResult = 1 if actualTriple[0] == pcpScore[1][0] else 0
		pcpScore = pcpScore[0]

		mcsActual = MCS(actualTriple)
		mcsScore = max([(MCS(p),p) for p in paraPairs])
		mcsResult = 1 if actualTriple[0] == mcsScore[1][0] else 0
		mcsScore = mcsScore[0]

		fstActual = FST(actualTriple)
		fstScore = max([(FST(p),p) for p in paraPairs])
		fstResult = 1 if actualTriple[0] == fstScore[1][0] else 0
		fstScore = fstScore[0]

		finalOutput = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (fileName,pcpResult,pcpScore,pcpActual,mcsResult,mcsScore,mcsActual,fstResult,fstScore,fstActual,chanceResult)

		print finalOutput

		resultsFile.write(finalOutput+'\n')

 	else:
 		print 'Skipping %s' % (f)

resultsFile.close()