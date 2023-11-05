import sys
import random
 
# total arguments
n = len(sys.argv)
wordSet1FilePath = sys.argv[1]
wordSet2FilePath = sys.argv[2]
file1Name = wordSet1FilePath[wordSet1FilePath.rfind('/')+1:wordSet1FilePath.rfind('.')]
file2Name = wordSet2FilePath[wordSet2FilePath.rfind('/')+1:wordSet2FilePath.rfind('.')]
  
# Opening file



def parseFile(filePath):
 
    d = {}
    with open(filePath) as f:
    	for line in f:
    	    (key, val) = line.strip().split('#@##@')
    	    d[str(key)] = str(val)
    return d 
def getCommonWords(wordSet1,wordSet2):
    commonWords = {}
    for key, value in wordSet1.items(): 
   #    outputFile.write('%s:%s\n' % (key, value))    
        if key in wordSet2:
    	     commonWords[key] = int(value)+int(wordSet2[key])
    return commonWords	
def unionWords(wordSet1,wordSet2):
    unionWords = wordSet1.copy();
    for key, value in wordSet2.items():
        if key not in wordSet1:
            unionWords[key] = value
    return unionWords     
def wordsNotInTheOtherSet(wordSet1,wordSet2):
    WordsInSet1Only = {};
    for key, value in wordSet1.items():
        if key not in wordSet2:
            WordsInSet1Only[key] = value
    return WordsInSet1Only 

def writeDictToFile(dict,fileName):

    outputFile = open(fileName, 'w')
    for key, value in dict.items(): 
        outputFile.write('%s:%s\n' % (key, value))    

    #outputFile.write(uniques)	
    outputFile.close()




wordSet1 = parseFile(wordSet1FilePath)
wordSet2 = parseFile(wordSet2FilePath)
print('wordSet1: ',len(wordSet1))
print('wordSet2: ',len(wordSet2))
commonWords = getCommonWords(wordSet1,wordSet2)
print('commonWords: ',len(commonWords))
writeDictToFile(commonWords,'CommonWords.txt')

unionWords = unionWords(wordSet1,wordSet2)
print('unionWords: ',len(unionWords))
writeDictToFile(commonWords,'unionWords.txt')
wordsInSet1Only = wordsNotInTheOtherSet(wordSet1,wordSet2)
print('words in set1: ',file1Name,len(wordsInSet1Only))
writeDictToFile(wordsInSet1Only,file1Name+'_only.txt')

wordsInSet2Only = wordsNotInTheOtherSet(wordSet2,wordSet1)
print('words in set2: ',file2Name,len(wordsInSet2Only))
writeDictToFile(wordsInSet2Only,file2Name+'_only.txt')

