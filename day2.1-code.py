listFile='day2.1-input.txt'

def loadData():
	reportList=[]
	safeList=[]
	fileHandler = open(listFile,'r')
	
	print('[>] loading data from '+listFile)
	
	for line in fileHandler:
		reportList.append(line.strip())
		safeList.append(determineSafety(line.strip()))
	
	print('[>] total number of safe reports: '+str(sum(safeList))+'/'+str(len(reportList)))
		
def determineSafety(reportString):
	reportData=list(map(int,reportString.split(' ')))					# convert list to ints
	safeFlag=1															# safe by default
	lastDiff=0
	
	for x in range(0,len(reportData)-1):									
		if(reportData[x]==reportData[x+1]):							# duplicate items
			safeFlag=0
			break
		else:
			thisDiff=reportData[x+1]-reportData[x]
			if(thisDiff>3 or thisDiff<-3):							# difference too great
				safeFlag=0
				break
			if((thisDiff>0 and lastDiff<0) or (thisDiff<0 and lastDiff>0)):
				safeFlag=0											# direction change
				break
			else:
				lastDiff=thisDiff
	print('[>] checking safety of '+reportString+'... '+str(safeFlag))
	return(safeFlag)

loadData()
