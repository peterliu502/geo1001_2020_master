# Clara Garcia-Sanchez
# 12/08/2020
################################# DO NOT CHANGE #####################################
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/claragarciasan/Documents/TUD/Classes/GEO1001/geo1001.2020/common_functions/')
import numpy as np																	#
import matplotlib.pyplot as plt														#
import pandas as pd																	#
from analytic import ReadBabyBoom 
import thinkstats2
import thinkplot
import first
from scipy import stats
#####################################################################################
# compare pregnancy lengths
live, firsts, others = first.MakeFrames()
data = firsts.prglngth.values, others.prglngth.values
print(data)
t, p = stats.ttest_ind(data[0],data[1])
print("t = " + str(t))
print("p = " + str(p))

# compare babies weights
data1 = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
t1, p1 = stats.ttest_ind(data1[0],data1[1])
print("t = " + str(t1))
print("p = " + str(p1))
