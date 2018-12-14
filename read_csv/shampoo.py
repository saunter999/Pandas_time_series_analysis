#!/usr/bin/env python
import pandas as pd
from scipy import *
from pylab import *
from pandas import datetime

"""
header sets the legend of x,y axis. Default is the first line
index_col sets the x values.Default is the natural iterator
"""

def loading1():
     series = pd.read_csv('shampoo-sales.csv', header=1, squeeze=True)
     print series.head()
     series.plot()
     legend(loc=0)

def loading2():
     series = pd.read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
     print series.head()
     series.plot()
     legend(loc=0)

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')



if __name__=="__main__":
     loading2()
     show()

