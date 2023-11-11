import sys
import random
 
# total arguments
n = len(sys.argv)
readFilePath1 = sys.argv[1]
readFilePath2 = sys.argv[2]
fileName1 = readFilePath1[readFilePath1.rfind('/')+1:readFilePath1.rfind('.')]
fileName2 = readFilePath2[readFilePath2.rfind('/')+1:readFilePath2.rfind('.')]
print(fileName1,fileName2)
# Opening file
file1 = open(readFilePath1, 'r')
file2 = open(readFilePath2, 'r')
file1Sentences = [];
file2Sentences = [];

for line in file1:
    file1Sentences.append(line.strip()+"\n");
for line in file2:
    file2Sentences.append(line.strip()+"\n");
print(len(file1Sentences),len(file2Sentences)) 
# Closing files
file1.close()
file2.close()

countOfCommonSentences = 0;
for sentence1 in file2Sentences:
    for sentence2 in file1Sentences:
        if sentence1 == sentence2:
            countOfCommonSentences += 1

print(countOfCommonSentences)
    
