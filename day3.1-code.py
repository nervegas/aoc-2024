import re

listFile='day3.1-input.txt'

def loadData():
	fileHandler = open(listFile,'r')
	rawData=''
	
	print('[>] loading data from '+listFile)
	
	for line in fileHandler:
		rawData+=line.strip()
	
	return(rawData)

def parseData(rawData):
	sumTotal=0
	regex = 'mul\([0-9]+\,[0-9]+\)'
	reResult = re.findall(regex, rawData)
	
	for x in range(0,len(reResult)):
		print('[>] '+str(x)+' > ' + reResult[x])
		reResult[x]=reResult[x].replace('mul(', '')
		reResult[x]=reResult[x].replace(')', '')
		thisPair=reResult[x].split(',')
#		print('[>>] '+str(x)+' > ' + thisPair[0] + 'x' + thisPair[1] + '=' + str(int(thisPair[0])*int(thisPair[1])))
		sumTotal+=(int(thisPair[0])*int(thisPair[1]))
	
	print('[>] total is '+str(sumTotal))
	
parseData(loadData())
