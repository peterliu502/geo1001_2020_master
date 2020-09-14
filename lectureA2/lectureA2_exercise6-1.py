 # Clara Garcia-Sanchez
# 12/08/2020
################################# DO NOT CHANGE #####################################
import sys
# insert at 1, 0 is the script path (or '' in REPL)

sys.path.append(sys.path[0]+'../common_functions/')
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
female = df[df.sex == 2]
female_heights = female.htm3.dropna()

# Exercise 1
print("mean value is:", np.mean(female_heights),
      "\nmedian value is: ", np.median(female_heights),
      "\nstd deviation value is:", np.std(female_heights),
      "\nvariance value is:", np.var(female_heights),
      "\nskewness value is:", stats.skew(female_heights),
      "\nkurtosis value is:", stats.kurtosis(female_heights))

# Exercise 2
bins_num = 50
[frequency, bins] = np.histogram(female_heights, bins=bins_num)
fig = plt.figure(figsize=(30, 6))

# pmf
ax1 = fig.add_subplot(131)
ax1.bar(female_heights.value_counts(normalize=True).index,
        female_heights.value_counts(normalize=True).values)

# pdf
ax2 = fig.add_subplot(132)
sns.distplot(female_heights.astype(float), bins=bins_num, kde=True)
#  thinkplot.Pdf(thinkstats2.EstimatedPdf(female_heights))

# cdf
ax3 = fig.add_subplot(133)
sns.kdeplot(female_heights.astype(float), shade=True, cumulative=True)

#  thinkplot.Cdf(thinkstats2.Cdf(female_heights))
plt.show()
