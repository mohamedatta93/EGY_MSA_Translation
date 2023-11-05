import sys
import random
import pyarabic.araby as araby

# total arguments
n = len(sys.argv)
readFilePath = sys.argv[1]
fileName = readFilePath[sys.argv[1].rfind('/')+1:sys.argv[1].rfind('.')]


def normalizeArabicText(sentence):
    sentence = sentence.replace('ة','ه')
    sentence = sentence.replace('أ','ا')
    sentence = sentence.replace('ى','ي')
    sentence = sentence.replace('إ','ا')
    sentence = sentence.replace('،','')
    sentence = sentence.replace(',','')
    sentence = sentence.replace('؟','')
    sentence = sentence.replace('-','')
    sentence = sentence.replace('ـ','')
    sentence = sentence.replace('(','')
    sentence = sentence.replace(')','')
    
    sentence = sentence.replace(':','')
    sentence = araby.strip_diacritics(sentence)
    sentence = sentence.replace('"','')
    sentence = sentence.replace('!','')
    sentence = sentence.replace('تُ','ت')
    sentence = sentence.replace('إ','ا')
    
    
    
    return sentence
# Opening file
file1 = open(readFilePath, 'r')
count = 0
pickedLines = [] 
i = 0;

for line in file1:
    sentence = line.strip();
    sentence = normalizeArabicText(sentence)
    	
    pickedLines.append(sentence+'\n')
 
# Closing files
file1.close()

outputFile = open(fileName+'_Normalized.txt', 'w')
outputFile.writelines(pickedLines)	
outputFile.close()

