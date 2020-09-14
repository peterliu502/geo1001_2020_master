# Clara Garcia Sanchez
# 05/04/2019
# Function in python to read data time series from PWIDS
#
# -Usage-
#	WS,WD,T,RH = readPWIDS(location,Npwids,DOYS,DOYE,HHS,HHE)
#
# -Inputs-
#	Folder of the data
#   Npwids
#   DOYS (day of the year start)
#	DOYE (day of the year end)
#   HHS (hour start)
#	HHE (hour end)
#
# -Outputs-
#	WS (wind speed)
#	WD (wind direction)
#   T  (temperature)
#   RH (relative humidity)
#
# Last Modified: 16/04/2019
import os
import numpy as np

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def readPWIDS(location,Npwids,DOYS,DOYE,HHS,HHE):
	pwids = Npwids
	startTime = '2003'+str(DOYS)+str(HHS)+'.0'
	endTime = '2003'+str(DOYE)+str(HHE)+'.0'
	for indPwids in range(0,np.size(pwids)):
		if pwids[indPwids] < 10:
			fileName = 'dpg_pwids0'+str(pwids[indPwids])+'-0317900-0321324.dat'
		else:
			fileName = 'dpg_pwids'+str(pwids[indPwids])+'-0317900-0321324.dat'

	day = []
	time = []
	WS = []
	WD = []
	T = []
	RH = []
	QC = []
	dayPlusTime = []
	c=0
	# with open('../PWIDS/'+fileName, encoding="utf8", errors='ignore') as f:
	with open(location+fileName, encoding="utf8", errors='ignore') as f:
		for line in f:
			c+=1
			fields = line.split(" ")
			if c > 61:
				day.append(fields[0])
				time.append(fields[1])
				if isfloat(fields[4]) and isfloat(fields[6]) and isfloat(fields[8]) and isfloat(fields[11]):
					WS.append(float(fields[4]))
					WD.append(float(fields[6]))
					T.append(float(fields[8]))
					RH.append(float(fields[11]))
				else:
					WS.append(10000)
					WD.append(10000)
					T.append(10000)
					RH.append(10000)
				QC.append(fields[12:14])
				dayPlusTime.append(str(fields[0]+fields[1]))
	f.close()
	startI = dayPlusTime.index(startTime)
	endI = dayPlusTime.index(endTime)

	WSf = np.array(WS[startI:endI])
	WDf = np.array(WD[startI:endI])
	Tf = np.array(T[startI:endI])
	RHf = np.array(RH[startI:endI])

	return WSf,WDf,Tf,RHf,dayPlusTime


