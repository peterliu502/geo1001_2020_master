# Clara Garcia-Sanchez
# 12/08/2020
################################# DO NOT CHANGE #####################################
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../common_functions/')
import numpy as np																	#
import matplotlib.pyplot as plt														#
import pandas as pd																	#
import thinkstats2
import brfss
from scipy import stats
#####################################################################################
df = brfss.ReadBrfss(nrows=None)
sample = thinkstats2.SampleFixedRows(df, 0, 5000)
heights, weights = sample.htm3, sample.wtkg2

# Step 1 --- remove nan numbers
heights = heights[~np.isnan(heights)]
weights = weights[~np.isnan(weights)]

# Step 2 --- interpolate to equal size samples
heights1 = np.interp(np.linspace(0,len(weights),len(weights)),np.linspace(0,len(heights),len(heights)),heights)

# Step 3 --- normalize because variables have different units
heights_normalized = (heights1 - heights1.mean())/heights1.std()
weights_normalized = (weights - weights.mean())/weights.std()

# Step 4 --- compute statistics
pcoef = stats.pearsonr(heights_normalized,weights_normalized)
prcoef = stats.spearmanr(heights_normalized,weights_normalized)
print(pcoef,prcoef)
print(np.cov(heights_normalized,weights_normalized))

# Step 4 --- scatter plot dimensional variables
fig = plt.figure(figsize=(17,5))
ax1 = fig.add_subplot(111)
ax1.scatter(heights1,weights,c='b')
# ax1.scatter(heights_normalized,weights_normalized,c='b')
ax1.set_xlabel('Heights [cm]')
ax1.set_ylabel('Weights [kg]')
plt.show()

# the reason for the columns shape is because heights are rounded to the nearest inch
# to correct we would need to jitter data (look at thinkStats2 book page 93 on how to 
# do that )