import sys
import random
 
# total arguments
n = len(sys.argv)
readFilePath = sys.argv[1]
fileName = readFilePath[readFilePath.rfind('/')+1:]
  
# Opening file
file1 = open(readFilePath, 'r')
count = 0
pickedLines = [] 



# Declare a dictionary
dict = {}
 
# Method to check whether the word
# exists in dictionary or not
def uniqueWord(Word):
 
    if Word in dict:
 
        # If the word exists in dictionary then
        # simply increase its count
        dict[words] += 1
 
    else:
 
        # If the word does not exists in
        # dictionary update the dictionary
        # and make its count 1
        dict.update({words: 1})
 
 
 
i = 0;
for line in file1:
	
    sentence = line.strip();
    # Iterate over dictionary if the value
    # of the key is 1, then print the element
       # Extract each word from ListOfWords
    # and pass it to the method uniqueWord()
    ListOfWords = sentence.split(' ')
    for words in ListOfWords:
        uniqueWord(words)
uniques = ""
# Closing files
file1.close()

dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
outputFile = open(fileName+'_Uniques.txt', 'w')
numberOfWords = 0

for key, value in dict.items():
    numberOfWords += value 
    outputFile.write('%s#@##@%s\n' % (key, value))    
numberOfUniqueWords = len(dict)
print('number Of All Words: ',numberOfWords)
print('number Of Unique Words: ',numberOfUniqueWords)

#outputFile.write(uniques)	
outputFile.close()

