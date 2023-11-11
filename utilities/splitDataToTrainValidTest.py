import sys
import random
 
# total arguments
n = len(sys.argv)
readFilePathLang1 = sys.argv[1]
readFilePathLang2 = sys.argv[2]
fileName1 = readFilePathLang1[readFilePathLang1.rfind('/')+1:readFilePathLang1.rfind('.')]
fileName2 = readFilePathLang2[readFilePathLang2.rfind('/')+1:readFilePathLang2.rfind('.')]
print(fileName1,fileName2)
# Opening file
fileLang1 = open(readFilePathLang1, 'r')
fileLang2 = open(readFilePathLang2, 'r')
lang1Sentences = [];
lang2Sentences = [];

for line in fileLang1:
    lang1Sentences.append(line.strip()+"\n");
for line in fileLang2:
    lang2Sentences.append(line.strip()+"\n");
print(len(lang1Sentences),len(lang2Sentences)) 
# Closing files
fileLang1.close()
fileLang2.close()



## shuffle the arrays
temp = list(zip(lang1Sentences, lang2Sentences))
random.shuffle(temp)
lang1Sentences, lang2Sentences = zip(*temp)



lang1Sentences_Train = lang1Sentences[0:57000];
lang2Sentences_Train = lang2Sentences[0:57000];
lang1Sentences_Valid = lang1Sentences[57000:57100];
lang2Sentences_Valid = lang2Sentences[57000:57100];
lang1Sentences_Test = lang1Sentences[57100:];
lang2Sentences_Test = lang2Sentences[57100:];



 ### train
outputFile = open(fileName1+"_train_"+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(lang1Sentences_Train)	
outputFile.close()
outputFile = open(fileName2+"_train_"+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(lang2Sentences_Train)	
outputFile.close()

### valid

outputFile = open(fileName1+"_valid_"+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(lang1Sentences_Valid)	
outputFile.close()
outputFile = open(fileName2+"_valid_"+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(lang2Sentences_Valid)	
outputFile.close()

######### test
outputFile = open(fileName1+"_test_"+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(lang1Sentences_Test)	
outputFile.close()
outputFile = open(fileName2+"_test_"+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(lang2Sentences_Test)	
outputFile.close()


