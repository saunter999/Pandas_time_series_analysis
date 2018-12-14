#!/usr/bin/env python
import pandas as pd
from scipy import *
from pylab import *
from pandas import datetime
from pandas.plotting import autocorrelation_plot
from pandas.plotting import lag_plot
import numpy as np

from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame


def loading():
     figure(0)
     series = pd.read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
#     print series.head()
     series.plot()
     legend(loc=0)
     return series

def parser(x):
     return datetime.strptime('190'+x, '%Y-%m')

def lag_analysis(df,lag,case='homemade'):
   figure(1)
   if case=='homemade':
     ndata=len(df)
     if lag>ndata: print "Error:lag value excedes the total length of the data."
     lagdata=df[:-lag]
     plot(lagdata,df[lag:],"r*",markersize=5)
     xlabel("lag"+str(lag),size='large')
     ylabel("original one",size='large')
   else:
     lag_plot(df,lag)
     
def AutoCorFunction_ana(df,case='homemade'):
   figure(2)
   if case=='homemade':
      n=len(df)
      data = np.asarray(df)
      mu=np.mean(data)
      var=((data-mu)*(data-mu)).sum()/float(n)
      laglist=arange(n)+1
      ACF=[]
      for lag in laglist:
          cov=np.sum( (data[:-lag]-mu)*(data[lag:]-mu) )/float(n)
	  ACF.append(cov/var)
      ACF=array(ACF)
      autocorrelation_plot(df,label='Pandas_result')
      plot(laglist,ACF,'ro',label='homemade')
      legend(loc=0)

def ARIMA_ana(df):
     model = ARIMA(df, order=(5,1,0))
     model_fit = model.fit(disp=0)
     print model_fit.summary()
     residuals = DataFrame(model_fit.resid)
     residuals.plot(kind='kde')

if __name__=="__main__":
     df=loading()
     lag_analysis(df,2)     
     AutoCorFunction_ana(df)
     ARIMA_ana(df)
     show()

