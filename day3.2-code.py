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
	processMul=1														# on by default
	regex = '(mul\([0-9]+\,[0-9]+\))|(do\(\))|(don\'t\(\))'				# [0] mul(), [1] do(), [2] don't()
	reResult = re.findall(regex, rawData)
	
	for x in range(0,len(reResult)):
		
		if(reResult[x][0]):
			if(processMul):
				thisItem=reResult[x][0].replace('mul(', '')
				thisItem=thisItem.replace(')', '')
				thisPair=thisItem.split(',')
				sumTotal+=(int(thisPair[0])*int(thisPair[1]))
				print('[>] '+str(x)+' > ' + reResult[x][0] + ' - added')
			else:
				print('[>] '+str(x)+' > ' + reResult[x][0] + ' - suppressed')
		elif(reResult[x][1]):
			print('[>] '+str(x)+' > ' + reResult[x][1])
			processMul=1												# do detected
		elif(reResult[x][2]):
			print('[>] '+str(x)+' > ' + reResult[x][2])	
			processMul=0												# don't detected
			
			
	
	print('[>] total is '+str(sumTotal))
	
parseData(loadData())
