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
#####################################################################################
df = ReadBabyBoom()
diffs = df.minutes.diff()
cdf = thinkstats2.Cdf(diffs, label = 'actual')

thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='minute', ylabel='CDF')
