from nltk import pos_tag
from pprint import pprint
from itertools import combinations
from math import log, exp
from string import letters, octdigits
from nltk import FreqDist as fd
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt



# Python has a Statistics module for 3.4 and greater
def mean(L):
	return sum(L)/len(L) if len(L) > 0 else 0

def __extractSynSets(T):
	'''
	Given a text T (as a string) find all words that have WordNet synsets
	@return a unique list of SynSet objects
	'''

	'''
	CONSTANTS
	'''
	nounTags = ['NN','NNP','NNS','NNPS']
	verbTags = ['VB','VBD','VBG','VBN','VBP','VBZ']
	adjTags = ['JJ','JJR','JJS']
	advTags = ['RB','RBR','RBS']
	alphanum = letters+octdigits

	
	def convertTag(tag):
		'''
		Converts a Penn Tree Bank POS tag to a WordNet
		@return the converted tag otherwise None
		'''
		if tag in nounTags:
			return 'n'
		elif tag in verbTags:
			return 'v'
		elif tag in adjTags:
			return 'as' # adjectives in WordNet can be head adj 'a' or satellite adj 's'
		elif tag in advTags:
			return 'r'
		else:
			return None 
	
	def getSynSet(w):
		'''
		For a word 'w' with POS tag 'tag' find the corresponding WordNet synset
		@return the best matching sysnset for 'w' otherwise None
		'''
		tag = w[1]
		word = w[0]

		# get the list of possible synsets for w
		sets = wn.synsets(word)
		
		if not tag or sets == []:
			return None

		# look through the list of possible synsets for the first one w/ a pos tag that matches 'tag'
		for s in sets:
			if s.pos in tag:
				return s

		return None

	# part of speech word list for the text
	fullList = [word for subl in [pos_tag(wt(s)) for s in st(T)] for word in subl]

	# remove symbols and -NONE- tags from list by checking the first character of the word and tag
	posList = [word for word in fullList if word[1][0] in alphanum and word[0][0] in alphanum]

	# convert words to lowercase and convert Penn Tree Bank tags to WordNet tags
	posList = [(word[0].lower(), convertTag(word[1])) for word in posList]

	# remove words for which there is no WordNet tag (i.e. tag is None) and remove duplicate values
	posList = list(set([word for word in posList if word[1]]))

	# for the words in the POS list create a list of syn sets using their tags (remove None values)
	synSets = [n for n in [getSynSet(w) for w in posList] if n] 

	return synSets

def __MCS(T1,T2):
	'''
	A similarity function based on the work of Mihalcea, Corely, & Strappavara (2006; MCS)
	T1 and T2 are two text files passed in as strings
	@return a similarity score for T1 and T2 based on maximum word similarities
	'''

	def sim(w,T):
		'''
		Returns the maximum similarity between word w (where w is a Synset object) and text T (where T is a list of Synsets)
		'''
		T = [t for t in T if t.pos == w.pos]
		foo = [w.wup_similarity(t) for t in T]
		return max(foo) if foo != [] else 0

	t1SynSets = __extractSynSets(T1)
	t2SynSets = __extractSynSets(T2)

	# calculate the average score for each text
	t1SimScore = mean([n for n in [sim(w,t2SynSets) for w in t1SynSets] if n])
	#t1SimScore = mean(t1SimScore)

	t2SimScore = mean([n for n in [sim(w,t1SynSets) for w in t2SynSets] if n])
	#t2SimScore = mean(t2SimScore)

	# final score is the average of all text scores
	finalScore = (t1SimScore+t2SimScore)/2

	#print 'MCS similarity score %s' % (finalScore)
	return finalScore

def MCS(texts):
	return mean([__MCS(t[0],t[1]) for t in combinations(texts,2)])

def __FST(T1,T2):
	'''
	A similarity function based on the work of Fernando and Stevenson (FST; 2008)
	T1 and T2 are strings of text
	'''
	
	def sim(word,W):
		'''
		Returns the similarity between word 1 and all words in the list of words W using the Wu-Palmer similarity metric
		'''
		def simHelper(w1,w2):
			if not w1.pos ==w2.pos:
				return 0
			# the paper suggests using a minimum similarity threshold
			wupScore = w1.wup_similarity(w2)
			return wupScore if wupScore and wupScore > .5 else 0
		
		return [simHelper(word,w) for w in W]

	synSets = __extractSynSets(T1)+__extractSynSets(T2)

	#print synSets

	scoreMatrix = [sim(s,synSets) for s in synSets]

	# pull non-zero values out of matrix
	scoreList = [s for sl in scoreMatrix for s in sl if s]

	# the final score is the average of all non-zero similarity scores
	finalScore = mean(scoreList)

	# print 'FST similarity score %s' % (finalScore)
	return finalScore

def FST(texts):
	return mean([__FST(t[0],t[1]) for t in combinations(texts,2)])
	






