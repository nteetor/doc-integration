#!/usr/bin/python2.7

import random
from pcp import PCP
from SimilarityMethods import MCS, FST

f = open('testFile1.txt')

fooText = f.read()

fooPara = [s for s in fooText.split("\n\n") if s != ""][:-1]

index = random.randint(1,len(fooPara)-1)

texts = [fooPara[index-1], fooPara[index], fooPara[index+1]]

print texts[0]
print texts[1]
print texts[2]

print PCP(texts)
print MCS(texts)
print FST(texts)

f.close()
