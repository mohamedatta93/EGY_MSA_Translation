import sys
import random
 
# total arguments
n = len(sys.argv)
readFilePath = sys.argv[1]
print('attttttttttttttttttttttttttttttttttttttttttttttttta0',sys.argv[1])
fileName = readFilePath[sys.argv[1].rfind('/')+1:sys.argv[1].rfind('.')]
header = '<refset trglang="egy" setid="sentences" srclang="any">\n<doc sysid="ref" docid="1564248" genre="news" origlang="msa">\n'
segment = '<p>\n<seg id="{0}">{1}</seg>\n</p>\n'
footer = '</doc> </refset>'
print(fileName) 
# Opening file
file1 = open(readFilePath, 'r')
lines = [] 
for line in file1: 
    lines.append(line.strip())
print('Number of lines: ',len(lines))
# Closing files
file1.close()
sgmLines = [header]

counter = 1
for line in lines:
    
    sgmLine = segment.format(counter,line)
    print(sgmLine)
    counter += 1
    sgmLines.append(sgmLine)
sgmLines.append(footer)

outputFile = open(fileName+'.sgm', 'w')
outputFile.writelines(sgmLines)	
outputFile.close()

