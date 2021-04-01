# import excel reader and other dependencies
import xlrd, sys, os, glob, csv, xlwt
from xlutils.copy import copy
from datetime import datetime

# Create necessary lists and vars
fileList = []
fileDate = []
lastMonthCases = 0
lastMonthDeaths = 0

# Get state of interest from user
stateOfInterest = input("Which state? (case-Sensitive): ")

# Get list of files (assuming all files are same format of MM-DD-YYYY.csv)
os.chdir("csse_covid_19_daily_reports_us")
for fileName in glob.glob("*.csv"):
	fileList.append(fileName)

# Create date list, removing .csv from name
for i in range(len(fileList)):
	print(fileList[i].replace(".csv",""))
	fileDate.append(fileList[i].replace(".csv",""))

# Sort by date
fileDate.sort(key=lambda date: datetime.strptime(date, "%m-%d-%Y"))
print(fileDate)

for fileNum in range(len(fileDate)):
	# Open CSV file
	with open(fileDate[fileNum]+".csv") as csv_file:
		# Read file
		csv_reader = csv.reader(csv_file, delimiter=",")
		# Create necessary lists
		fileStates = []
		fileCases = []
		fileDeaths = []
		indexNum = 0
		# Extract data from CSV file. States are in Row 0, Cases in Row 5, Deaths in Row 6
		for row in csv_reader:
			fileStates.append(row[0])
			fileCases.append(row[5])
			fileDeaths.append(row[6])
		# Find index num of state of interest
		for i in range(len(fileStates)):
			if fileStates[i] == stateOfInterest:
				indexNum = i
		rowNum = fileNum + 1
		# Create notebook, if this is the first runthrough.
		if fileNum == 0:
			initwb = xlwt.Workbook()
			initsheet = initwb.add_sheet(stateOfInterest)
			initsheet.write(0,0,"STATE")
			initsheet.write(0,1, "FILE NAME")
			initsheet.write(0,2,"DATE")
			initsheet.write(0,3, "CUMULATIVE CASES")
			initsheet.write(0,4, "CUMULATIVE DEATHS")
			initsheet.write(0,5,"NEW DAILY CASES")
			initsheet.write(0,6,"NEW DAILY DEATHS")
			initsheet.write(0,7,"MONTHLY CASES")
			initsheet.write(0,8,"MONTHLY DEATHS")
			initwb.save(stateOfInterest+".xls")
			
		# Read export notebook.
		ewb = copy(xlrd.open_workbook(stateOfInterest+".xls"))
		ewb.get_sheet(0).write(rowNum,0,fileStates[indexNum]) #Writes State Name (to confirm correct index selection)
		ewb.get_sheet(0).write(rowNum,1,fileDate[fileNum]+".csv") # Write File Name
		ewb.get_sheet(0).write(rowNum,2,fileDate[fileNum]) # Write Date
		ewb.get_sheet(0).write(rowNum,3,fileCases[indexNum]) # Write Cases
		ewb.get_sheet(0).write(rowNum,4,fileDeaths[indexNum]) # Write Death
		# Calculating new cases/deaths
		if fileNum == 0: # For first row, just put the number of cases/deaths.
			ewb.get_sheet(0).write(rowNum,5,fileCases[indexNum]) 
			ewb.get_sheet(0).write(rowNum,6,fileDeaths[indexNum])
		else:
			ewb.get_sheet(0).write(rowNum,5,int(fileCases[indexNum])-int(lastFileCases))
			ewb.get_sheet(0).write(rowNum,6,int(fileDeaths[indexNum])-int(lastFileDeaths))
		print(fileDate[fileNum], fileStates[indexNum],fileCases[indexNum],fileDeaths[indexNum]) # Outputs to user
		# Calculates monthly rate
		try:
			errorCheck = fileDate[fileNum+1]
			if fileDate[fileNum].find(fileDate[fileNum+1][0]+fileDate[fileNum+1][1]+fileDate[fileNum+1][2]) == -1:
				if fileNum ==0:
					lastMonthCases = 0
					lastMonthDeaths = 0
				ewb.get_sheet(0).write(rowNum,7,int(fileCases[indexNum])-lastMonthCases)
				ewb.get_sheet(0).write(rowNum,8,int(fileDeaths[indexNum])-lastMonthDeaths)
				lastMonthCases = int(fileCases[indexNum])
				lastMonthDeaths = int(fileDeaths[indexNum])
		except:
			print("Script Complete.")
		ewb.save(stateOfInterest+".xls") # Saves and closes file
		lastFileCases = fileCases[indexNum]
		lastFileDeaths = fileDeaths[indexNum]
	
