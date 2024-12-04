listFile='day1.1-input.txt'

def loadData():
	firstList=[]
	secondList=[]
	similarityList=[]
	
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
	
	print('[>] generating similarities...')
	for x in range(0,len(firstList)):
		currentMatchCount=0
		for y in range(0,len(secondList)):
			if(firstList[x]==secondList[y]):
				currentMatchCount+=1
		similarityList.append(currentMatchCount*firstList[x])
	
	print('[>] done.')
	print('[>] total similarity value: '+str(sum(similarityList)))
loadData()

'''
print('[>] printing first 10 sets:')
	for x in range(0,100):
		print("\t"+str(firstList[x])+"::"+str(secondList[x])+':sim:'+str(similarityList[x]))
	print('[>] done.')
'''
