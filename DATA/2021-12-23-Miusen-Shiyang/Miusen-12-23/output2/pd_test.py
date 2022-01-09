##author:mizukiyuta

import numpy as np

import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

from scipy import stats
from scipy.stats import norm

import time
import datetime

import neurokit2 as nk


##---------------------------------------------------
##------------------IMPORTANT------------------------
##---------------------------------------------------
#You should change data's experiment date and collaborator name
##---------------------------------------------------
root="C:/Users/mizukiyuta/Desktop/atmosphere/DATA/"

#d
##---------------------------------------------------
##read data's info (self-report csv)
file_name="data0.csv"
print("Read csv:",file_name)
#sr_df =  pd.read_csv('%s/%s' % (data_path, sr_file_name),encoding='unicode_escape')#SR.csv
df = pd.read_csv(file_name)
print(df)
print("-"*50)
#input(len(sr_df))
##---------------------------------------------------
