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
	reportData=reportString.split(' ')
	safeFlag=1	# safe by default
	
	if(int(reportData[0])<int(reportData[1])):
		valueRise=1	# increase
	elif(int(reportData[0])>int(reportData[1])):
		valueRise=0	# decrease
	else:
		valueRise=0
		safeFlag=0	# break if unsafe
		
	for x in range(1,len(reportData)): # start from 1 to be able to look at the previous item
		reportDiff=int(reportData[x])-int(reportData[x-1])
		if(safeFlag==0):	# break if unsafe
			break
			
		if(valueRise==0):
			reportDiff=reportDiff*-1
		
		if(reportDiff<1 or reportDiff>3):
			safeFlag=0	# break if unsafe
	
	print('[>] checking safety of '+reportString+'... '+str(safeFlag)+' (valueRise='+str(valueRise)+')')
	return(safeFlag)

loadData()
