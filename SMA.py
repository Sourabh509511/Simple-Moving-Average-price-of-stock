import pandas
import numpy
import matplotlib.pyplot as plt
import quandl
from matplotlib import style
import os

style.use('seaborn-bright')
current_dir=os.getcwd()
api_key=open(os.path.join(current_dir,'auth.txt'),'r').read()

data=quandl.get('NSE/ONGC',trim_start='1998-03-20',trim_end='2019-01-04',api_key=api_key)

data['5D']=numpy.round(data['Close'].rolling(window=5).mean(),2)

data['15D']=numpy.round(data['Close'].rolling(window=15).mean(),2)

data['30D']=numpy.round(data['Close'].rolling(window=30).mean(),2)


data[['Close','5D','15D','30D']].plot(grid=True,figsize=(50,50))
plt.show()