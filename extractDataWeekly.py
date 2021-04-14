# import excel reader and other dependencies
import xlrd, sys, os, glob, csv, xlwt
from xlutils.copy import copy
from datetime import datetime

# Create necessary lists and vars
fileList = []
fileDate = []
lastMonthCases = 0
lastMonthDeaths = 0
lastWeekCases = 0
lastWeekDeaths = 0
weekIDs = ['W1','W2','W3','W4','W5','W6','W7','W8','W9','W10','W11','W12','W13','W14','W15','W16','W17','W18','W19','W20','W21','W22','W23','W24','W25','W26','W27','W28','W29','W30','W31','W32','W33','W34','W35','W36','W37','W38','W39','W40','W41','W42','W43','W44','W45','W46','W47','W48','W49','W50','W51','W52']
weekEndDates = ['04-07-2020','04-14-2020','04-21-2020','04-28-2020','05-05-2020','05-12-2020','05-19-2020','05-26-2020','06-02-2020','06-09-2020','06-16-2020','06-23-2020','06-30-2020','07-07-2020','07-14-2020','07-21-2020','07-28-2020','08-04-2020','08-11-2020','08-18-2020','08-25-2020','09-01-2020','09-08-2020','09-15-2020','09-22-2020','09-29-2020','10-06-2020','10-13-2020','10-20-2020','10-27-2020','11-03-2020','11-10-2020','11-17-2020','11-24-2020','12-01-2020','12-08-2020','12-15-2020','12-22-2020','12-29-2020','01-05-2021','01-12-2021','01-19-2021','01-26-2021','02-02-2021','02-09-2021','02-16-2021','02-23-2021','03-02-2021','03-09-2021','03-16-2021','03-23-2021','03-30-2021']


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
			initsheet.write(0,9,"WEEK ID")
			initsheet.write(0,10,"WEEKLY CASES")
			initsheet.write(0,11,"WEEKLY DEATHS")
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
		for i in range(len(weekEndDates)):
				if fileDate[fileNum] == weekEndDates[i]:
					ewb.get_sheet(0).write(rowNum,9, weekIDs[i])
					ewb.get_sheet(0).write(rowNum,10, int(fileCases[indexNum])-lastWeekCases)
					ewb.get_sheet(0).write(rowNum,11, int(fileDeaths[indexNum])-lastWeekDeaths)
					lastWeekCases = int(fileCases[indexNum])
					lastWeekDeaths = int(fileDeaths[indexNum])
		
		ewb.save(stateOfInterest+".xls") # Saves and closes file
		lastFileCases = fileCases[indexNum]
		lastFileDeaths = fileDeaths[indexNum]
	
