# Clara Garcia-Sanchez
# 05/04/2019
# Function in python to extract Time Series WindSpeed and WindDirection from PWIDS
#
# -Usage-
#	[out1,out2] = testfunction(in1,in2)
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
#   TK
#   TMeas
#
# Last Modified: 05/04/2019
import numpy as np
from readPWIDS import readPWIDS
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.cm import get_cmap
location = '../data/'
Npwids = np.array([15])
Period = 'IOP9'
if Period in'IOP9':
    #Day of the year and time range of interest
    DOYS = '208'
    DOYE = '208'
    HHS ='04:00:00'
    HHE ='04:30:00'
elif Period in '23h':
    #Day of the year and time range of interest
    DOYS = '207'
    DOYE = '207'
    HHS ='23:05:00'
    HHE ='23:30:00'
else:
    print('Period targeted not considered')
WS, WD, T, RH, dayPlusTime = readPWIDS(location,Npwids,DOYS,DOYE,HHS,HHE)
# measurement sampling frequency
fs = 10
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig,ax= plt.subplots(1,2)
# ((ax1,ax2)) = ax
ax1.plot(np.linspace(0,180*10/60,180),WS,color=plt.cm.tab10(0),linewidth=2)
ax1.set_ylabel('Wind Speed [m/s]',fontsize=14)
ax1.set_xlabel('Time [min]',fontsize=14)
ax2.plot(np.linspace(0,180*10/60,180),WD,color=plt.cm.tab10(1),linewidth=3)
ax2.set_ylabel('Wind direction [$^{\circ}$]',fontsize=14)
ax2.set_xlabel('Time [min]',fontsize=14)
plt.show()

fig = plt.figure(figsize=(8,6))
n, bins, patches = plt.hist(x=WS, bins=11, color='b',alpha=0.7, rwidth=0.85)
plt.xlabel('Wind speed [m/s]',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
