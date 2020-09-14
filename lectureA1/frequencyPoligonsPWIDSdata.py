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
location = '../data/'
Npwids = np.array([15])
Period = 'IOP9'
if Period in'IOP9':
    #Day of the year and time range of interest
    DOYS = '208'
    DOYE = '208'
    HHS ='04:00:00'
    HHE ='04:30:00'
else:
    print('Period targeted not considered')
WS, WD, T, RH, dayPlusTime = readPWIDS(location,Npwids,DOYS,DOYE,HHS,HHE)

## Code to modify!
fig = plt.figure(figsize=(21,6))
fs = 14
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
[frequency,bins]=np.histogram(WS, bins=40)
ax1.plot(bins[:-1],frequency)
ax1.set_ylabel('Frequency',fontsize=fs)
ax1.set_xlabel('Wind Speed [m/s]',fontsize=fs)
ax1.tick_params(labelsize=fs)
ax2.hist(x=WS, bins=20, color='b',alpha=0.7, rwidth=0.85)
ax2.set_xlabel('Wind Speed [m/s]',fontsize=fs)
ax2.tick_params(labelsize=fs)
cdf_WS = np.cumsum(frequency)
ax3.plot(bins[:-1],cdf_WS)
ax3.set_ylabel('Cumulative number of samples',fontsize=fs)
ax3.set_xlabel('Wind Speed [m/s]',fontsize=fs)
ax3.tick_params(labelsize=fs)
plt.show()

