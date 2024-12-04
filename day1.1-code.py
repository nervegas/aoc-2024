listFile='day1.1-input.txt'

def loadData():
	firstList=[]
	secondList=[]
	distanceList=[]
	
	fileHandler = open(listFile,'r')
	
	print('[>] loading data from '+listFile)
	
	for line in fileHandler:
		currentLine=(line.strip()).split("\t")
		firstList.append(int(currentLine[0]))
		secondList.append(int(currentLine[1]))
	
	print('[>] data loaded from '+listFile)
	print('[>] total pairs loaded: '+str(len(firstList))+'::'+str(len(secondList)))
	
	print('[>] sorting lists...')
	firstList=sorted(firstList)
	secondList=sorted(secondList)
	
	print('[>] generating distances...')
	for x in range(0,len(firstList)):
		currentRange=firstList[x]-secondList[x]
		if(currentRange<0):
			currentRange=currentRange*-1
		distanceList.append(currentRange);
	print('[>] done.')
	
	totalRange=sum(distanceList)
	
	print('[>] total distance for '+str(len(distanceList))+' pairs is: '+str(totalRange))
	
loadData()
