import sys
import glob
import re
import os
import random

def generateDetectors(detector, maxDetector, path):
    count = 0
    match = 0

    word = [line.strip() for line in open('detector_words.txt')]
    wordRandom = random.choice(word)

    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename, "r") as fo:
            for line in fo:
                for candidate in line.split():
                    if ((candidate != wordRandom) and (count < maxDetector)):
                        detector.append(wordRandom)
                        print count
                        count += 1
                        
                    word = [line.strip() for line in open('detector_words.txt')]
                    wordRandom = random.choice(word)
                        
                     
        fo.close()
        #print count
        if(count ==  maxDetector):
            return

def detectorSpam(detector, path):
    match = 0
    i = 0

    output = open('result.txt', 'w+')
 
    for filename in glob.glob(os.path.join(path, '*')):
        while i < len(detector):
            match = matches(filename,detector[i])
            if(match == 1):
                output.write("%s\n" % filename.name + ' spam')
            else:
                output.write("%s\n" % filename.name + ' half')
            i += 1

try:
    pathTraning = sys.argv[1]
   # pathTest = sys.argv[2]
    maxDetector = 50
    detector = []
    generateDetectors(detector, maxDetector, pathTraning)
    print detector
    print len(detector)     
   # detectorSpam(detector, pathTest)
except Exception, e: 
    print str(e)

