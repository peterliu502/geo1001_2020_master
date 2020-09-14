# Clara Garcia-Sanchez
# 12/08/2020
################################# DO NOT CHANGE #####################################
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../common_functions/')
import numpy as np																	#
import matplotlib.pyplot as plt														#
import pandas as pd																	#
from analytic import ReadBabyBoom
import thinkstats2
import thinkplot
import numpy as np
import brfss
import scipy.stats as stats
import seaborn as sns


df = brfss.ReadBrfss(nrows=None)
female = df[df.sex==2]
female_heights = female.htm3.dropna()
mean, std = female_heights.mean(), female_heights.std()
print(mean, std)
median = female_heights.median()
print(median)
skewness = stats.skew(female_heights)
print(skewness)
kurtosis = stats.kurtosis(female_heights)
print(kurtosis)

nb = 50
fs = 12


# compute and plot pmf
def pmf(sample):
    c = sample.value_counts()
    p = c/len(sample)
    return p


df = pmf(female_heights)
c = df.sort_index()
fig = plt.figure(figsize=(30,6))
ax1 = fig.add_subplot(131)
ax1.bar(c.index,c.values)
# plt.show()

# plot pdf
# fig = plt.figure(figsize=(17,6))
ax2 = fig.add_subplot(132)
a1=ax2.hist(x=female_heights.astype(float),bins=nb, density=True, color='b',alpha=0.7, rwidth=0.85)
sns.distplot(female_heights.astype(float), color='k',ax=ax2)
# plt.show()

# plot cdf
# fig = plt.figure(figsize=(17,6))
ax3 = fig.add_subplot(133)
a1=ax3.hist(x=female_heights.astype(float),bins=nb, cumulative=True, color='b',alpha=0.7, rwidth=0.85)
ax3.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='k')
plt.show()

