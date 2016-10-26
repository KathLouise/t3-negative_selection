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
                        count += 1
                        
                    word = [line.strip() for line in open('detector_words.txt')]
                    wordRandom = random.choice(word)
                        
        print fo.name                     
        fo.close()

        if(count == maxDetector):
            return

def detectorSpam(detector, path, maxDetector):
    match = 0
    i = 0
    output = open('result.txt', 'w+')

    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename, "r") as fo:
            for line in fo:
                for word in line.split(): 
                    if word in detector:
                        match += 1
                        i += 1
             
        if(match >= 10):
            output.write("spam %s\n\n" % fo.name )
        else:
            output.write("half %s\n\n" % fo.name )
            
        fo.close()
        i = 0
        match = 0
        
try:
    pathTraning = sys.argv[1]
    pathTest = sys.argv[2]
    maxDetector = 300
    detector = []
    generateDetectors(detector, maxDetector, pathTraning)
    detectorSpam(detector, pathTest, maxDetector)
except Exception, e: 
    print str(e)

