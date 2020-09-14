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
print(np.size(heights))


# normalize function
def normalize(my_array):
    my_mean = np.mean(my_array)
    my_std = np.std(my_array)
    return (my_array - my_mean) / my_std


# delete nan value and normalize them
heights = heights[~np.isnan(heights)] = normalize(heights[~np.isnan(heights)])
weights = weights[~np.isnan(weights)] = normalize(weights[~np.isnan(weights)])


# match their length, interpolate data from heights to the length of weights
my_heights = np.interp(np.linspace(0, len(weights), len(weights)),  # provide an array from 0 to len(weights), step is 1
                       np.linspace(0, len(heights), len(heights)),  # provide an array from 0 to len(heights), step is 1
                       heights)

spearman_r = stats.spearmanr(my_heights, weights)
pearson_r = stats.pearsonr(my_heights, weights)
covariance = np.cov(my_heights, weights)

print(np.nan in spearman_r,
      np.nan in pearson_r,
      np.nan in covariance)
print("correlation: \n", spearman_r,
      "\npearson_r: \n", pearson_r,
      "\ncovariance: \n", covariance)


# draw a scatter plot
fig = plt.figure(figsize=(16, 16))
ax1 = fig.add_subplot(111)
ax1.scatter(normalize(my_heights), normalize(weights), c="b")
plt.show()
