import sys
import random
 
# total arguments
n = len(sys.argv)
readFilePath = sys.argv[2]
numberOfLines = int(sys.argv[1])
  
# Opening file
file1 = open(readFilePath, 'r')
count = 0
pickedLines = [] 
i = 0;
for line in file1:
    if count == numberOfLines:
    	break;
    sentence = line.strip();
    		
    if len(sentence)>70 and len(sentence)<200 and i%1000==1 and bool(random.getrandbits(1))==True:
    	count += 1
    	pickedLines.append(sentence+'\n')
    i += 1
 
# Closing files
file1.close()

outputFile = open('phosha'+str(int(random.getrandbits(16)))+'.txt', 'w')
outputFile.writelines(pickedLines)	
outputFile.close()

