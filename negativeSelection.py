import sys
import glob
import re
import os
import random
from collections import Counter

def searchAdd(detector, word):
    if word not in detector:
        detector.append(word)
        
def countNumberWords(file):
    c = Counter()
    with open(file, 'rb') as f:
        for ln in f:
            c.update(ln.split())
            
    f.close()

    total = sum(c.values())
    return total
 
def generateDetectors(detector, maxDetector, path):
    count = 0
    notmatch = 0
 
    word = [line.strip() for line in open('detector_words.txt')]
    wordRandom = random.choice(word)
 
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename, "r") as fo:
            for line in fo:
                for candidate in line.split():
                    if ((candidate != wordRandom) and (count < maxDetector) and (notmatch < 15)):
                        searchAdd(detector, wordRandom)
                        count += 1
                        notmatch += 1;
                    word = [line.strip() for line in open('detector_words.txt')]
                    wordRandom = random.choice(word)

            fo.close()
            notmatch = 0

            if(count == maxDetector):
                return

def detectorSpam(detector, path, maxDetector):
    match = 0
    i = 0
    totalWords = 0;
    output = open('resultnew.txt', 'w+')
    spam = open('spam.txt', 'w+')

    for filename in glob.glob(os.path.join(path, '*.txt')):
        totalWords = countNumberWords(filename)
        with open(filename, "r") as fo:
            for line in fo:
                for word in line.split(): 
                    if word in detector:
                        match += 1
                        i += 1
             
        if(match > (totalWords/2)):
            spam.write("spam %s\n\n" % fo.name )
        else:
            output.write("half %s\n\n" % fo.name )
            
        fo.close()
        i = 0
        match = 0
        
try:
    pathTraning = sys.argv[1]
    pathTest = sys.argv[2]
    maxDetector = 1000
    detector = []
    generateDetectors(detector, maxDetector, pathTraning)
    detectorSpam(detector, pathTest, maxDetector)
except Exception, e: 
    print str(e)

