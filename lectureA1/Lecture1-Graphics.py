# Clara Garcia-Sanchez
# 05/04/2019
# Function in python to extract Time Series WindSpeed and WindDirection from PWIDS
# -Usage-
#	[out1,out2] = testfunction(in1,in2)
# -Inputs-
#	Folder of the data
#   Npwids
#   DOYS (day of the year start)
#	DOYE (day of the year end)
#   HHS (hour start)
#	HHE (hour end)
# -Outputs-
#	WS (wind speed)
#	WD (wind direction)
#   TK
#   TMeas
#
# Last Modified: 18/06/2020
################################# DO NOT CHANGE #####################################
import numpy as np																	#
from readPWIDS import readPWIDS														#
import matplotlib.pyplot as plt														#
import seaborn as sns																#
import pandas as pd																	#
location = 'data/'																	#
Npwids = np.array([15])																#
#Day of the year and time range of interest											#
DOYS = '208'																		#
DOYE = '208'																		#
HHS ='04:00:00'																		#
HHE ='04:30:00'																		#
WS, WD, T, RH, dayPlusTime = readPWIDS(location,Npwids,DOYS,DOYE,HHS,HHE)			#
#####################################################################################

# Possible cases: histograms, frequency_polygons, boxplots, boxplots_advanced
plot_type = 'boxplots'
fs = 14

if plot_type == 'histograms':
		## Code to modify for HISTOGRAMS PART!
		fig = plt.figure(figsize=(14,6))
		ax1 = fig.add_subplot(121)
		ax2 = fig.add_subplot(122)
		ax1.hist(x=WS, bins=5, density=True, color='b',alpha=0.7, rwidth=0.85)
		ax1.set_ylabel('Frequency',fontsize=fs)
		ax1.set_xlabel('Wind Speed [m/s]',fontsize=fs)
		ax1.tick_params(labelsize=fs)
		ax2.hist(x=WD, bins=5, color='b',alpha=0.7, rwidth=0.85)
		ax2.set_xlabel('Wind Direction [$^{\circ}$]',fontsize=fs)
		ax2.tick_params(labelsize=fs)
		plt.show()

elif plot_type == 'frequency_polygons':
		## Code to modify for FREQUENCY_POLYGONS PART!
		fig = plt.figure(figsize=(21,6))
		ax1 = fig.add_subplot(131)
		ax2 = fig.add_subplot(132)
		ax3 = fig.add_subplot(133)
		[frequency,bins]=np.histogram(WS, bins=11)
		ax1.plot(bins[:-1],frequency)
		ax1.set_ylabel('Frequency',fontsize=fs)
		ax1.set_xlabel('Wind Speed [m/s]',fontsize=fs)
		ax1.tick_params(labelsize=fs)
		ax2.hist(x=WS, bins=11, color='b',alpha=0.7, rwidth=0.85)
		ax2.set_xlabel('Wind Speed [m/s]',fontsize=fs)
		ax2.tick_params(labelsize=fs)
		cdf_WS = np.cumsum(frequency)
		ax3.plot(bins[:-1],cdf_WS)
		ax3.set_ylabel('Cumulative number of samples',fontsize=fs)
		ax3.set_xlabel('Wind Speed [m/s]',fontsize=fs)
		ax3.tick_params(labelsize=fs)
		plt.show()

elif plot_type == 'boxplots':
		## Code to modify for BOXPLOTS PART!
		fig = plt.figure(figsize=(14,6))
		fs = 14
		ax1 = fig.add_subplot(121)
		ax2 = fig.add_subplot(122)
		ax1.boxplot(WS,showmeans=True)
		ax1.set_ylabel('Wind Speed [m/s]',fontsize=fs)
		ax1.tick_params(labelsize=fs)
		ax2.boxplot(WD,showmeans=True)
		ax2.set_ylabel('Wind Direction [$^{\circ}$]',fontsize=fs)
		ax2.tick_params(labelsize=fs)
		plt.show()
elif plot_type == 'boxplots_advanced':
		## Code to modify for ADVANCED BOXPLOTS PART!
		sns.set()
		WS = np.array([WS])
		WD = np.array([WD])
		data = np.concatenate((WS,WD),axis=0)
		df = pd.DataFrame(data.T,columns=['WS','WD'],dtype=float)
		fig = plt.figure(figsize=(14,6))
		fs = 14
		ax1 = fig.add_subplot(121)
		ax2 = fig.add_subplot(122)
		sns.boxplot(data=df['WS'], showfliers = False, ax=ax1)
		sns.swarmplot(data=df['WS'], color=".25", ax=ax1)
		ax1.set(ylabel='Wind Speed [m/s]')
		ax1.tick_params(labelsize=fs)
		sns.boxplot(data=df['WD'], showfliers = False, ax=ax2)
		sns.swarmplot(data=df['WD'], color=".25", ax=ax2)
		ax2.set(ylabel='Wind Direction [$^{\circ}$]')
		ax2.tick_params(labelsize=fs)
		plt.show()
else:
	print('Is the name of the plot you entered correct? It doesnt seem to match any option\n')
