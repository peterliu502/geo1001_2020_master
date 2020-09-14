import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import csv
import scipy.stats as stats
import seaborn as sns


with open('../data/PEP_2012_PEPANNRES_with_ann.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    population_estimate_2012 = [row[-1] for row in reader][2:]
    population_estimate_2012 = [int(population_estimate_2012[i])
                                for i in range(len(population_estimate_2012))
                                if (population_estimate_2012[i] != "(X)") and (population_estimate_2012[i] != "0")]
with open('../data/PEP_2012_PEPANNRES_with_ann.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    population_estimate_2011 = [row[-2] for row in reader][2:]
    population_estimate_2011 = [int(population_estimate_2011[i])
                                for i in range(len(population_estimate_2011))
                                if (population_estimate_2011[i] != "(X)") and (population_estimate_2011[i] != "0")]
with open('../data/PEP_2012_PEPANNRES_with_ann.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    population_estimate_2010 = [row[-3] for row in reader][2:]
    population_estimate_2010 = [int(population_estimate_2010[i])
                                for i in range(len(population_estimate_2010))
                                if (population_estimate_2010[i] != "(X)") and (population_estimate_2010[i] != "0")]
with open('../data/PEP_2012_PEPANNRES_with_ann.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    estimates_base_2010 = [row[-4] for row in reader][2:]
    estimates_base_2010 = [int(estimates_base_2010[i])
                           for i in range(len(estimates_base_2010))
                           if (estimates_base_2010[i] != "(X)") and (estimates_base_2010[i] != "0")]
with open('../data/PEP_2012_PEPANNRES_with_ann.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    census_2010 = [row[-5] for row in reader][2:]
    census_2010 = [int(census_2010[i])
                   for i in range(len(census_2010))
                   if (census_2010[i] != "(X)") and (census_2010[i] != "0")]

bins_num = 30

fig = plt.figure(figsize=(40, 50))
# census_2010
# census_2010_pdf
ax1_pdf = fig.add_subplot(5, 4, 1)
sns.distplot(census_2010, hist=False)

# census_2010_cpdf
ax1_cpdf = fig.add_subplot(5, 4, 2)
ax1_cpdf.set_xscale('log')
ax1_cpdf.set_yscale('log')
sns.distplot(census_2010, hist=False)

# census_2010_cdf
ax1_cdf = fig.add_subplot(5, 4, 3)
sns.kdeplot(census_2010, cumulative=True)

# census_2010_ccdf
ax1_ccdf = fig.add_subplot(5, 4, 4)
ax1_ccdf.set_xscale('log')
ax1_ccdf.set_yscale('log')
sns.kdeplot(census_2010, cumulative=True)

# estimates_base_2010
# estimates_base_2010_pdf
ax2_pdf = fig.add_subplot(5, 4, 5)
sns.distplot(estimates_base_2010, hist=False)

# estimates_base_2010_cpdf
ax2_cpdf = fig.add_subplot(5, 4, 6)
ax2_cpdf.set_xscale('log')
ax2_cpdf.set_yscale('log')
sns.distplot(estimates_base_2010, hist=False)

# estimates_base_2010_cdf
ax2_cdf = fig.add_subplot(5, 4, 7)
sns.kdeplot(estimates_base_2010, cumulative=True)

# estimates_base_2010_ccdf
ax2_ccdf = fig.add_subplot(5, 4, 8)
ax2_ccdf.set_xscale('log')
ax2_ccdf.set_yscale('log')
sns.kdeplot(estimates_base_2010, cumulative=True)

# population_estimate_2010
# population_estimate_2010_pdf
ax3_pdf = fig.add_subplot(5, 4, 9)
sns.distplot(population_estimate_2010, hist=False)

# population_estimate_2010_cpdf
ax3_cpdf = fig.add_subplot(5, 4, 10)
ax3_cpdf.set_xscale('log')
ax3_cpdf.set_yscale('log')
sns.distplot(population_estimate_2010, hist=False)

# population_estimate_2010_cdf
ax3_cdf = fig.add_subplot(5, 4, 11)
sns.kdeplot(population_estimate_2010, cumulative=True)

# population_estimate_2010_ccdf
ax3_ccdf = fig.add_subplot(5, 4, 12)
ax3_ccdf.set_xscale('log')
ax3_ccdf.set_yscale('log')
sns.kdeplot(population_estimate_2010, cumulative=True)

# population_estimate_2011
# population_estimate_2011_pdf
ax4_pdf = fig.add_subplot(5, 4, 13)
sns.distplot(population_estimate_2011, hist=False)

# population_estimate_2011_cpdf
ax4_cpdf = fig.add_subplot(5, 4, 14)
ax4_cpdf.set_xscale('log')
ax4_cpdf.set_yscale('log')
sns.distplot(population_estimate_2011, hist=False)

# population_estimate_2011_cdf
ax4_cdf = fig.add_subplot(5, 4, 15)
sns.kdeplot(population_estimate_2011, cumulative=True)

# population_estimate_2011_ccdf
ax4_ccdf = fig.add_subplot(5, 4, 16)
ax4_ccdf.set_xscale('log')
ax4_ccdf.set_yscale('log')
sns.kdeplot(population_estimate_2011, cumulative=True)

# population_estimate_2012
# population_estimate_2012_pdf
ax5_pdf = fig.add_subplot(5, 4, 17)
sns.distplot(population_estimate_2012, hist=False)

# population_estimate_2012_cpdf
ax5_cpdf = fig.add_subplot(5, 4, 18)
ax5_cpdf.set_xscale('log')
ax5_cpdf.set_yscale('log')
sns.distplot(population_estimate_2012, hist=False)

# population_estimate_2012_cdf
ax5_cdf = fig.add_subplot(5, 4, 19)
sns.kdeplot(population_estimate_2012, cumulative=True)

# population_estimate_2012_ccdf
ax5_ccdf = fig.add_subplot(5, 4, 20)
ax5_ccdf.set_xscale('log')
ax5_ccdf.set_yscale('log')
sns.kdeplot(population_estimate_2012, cumulative=True)
plt.show()