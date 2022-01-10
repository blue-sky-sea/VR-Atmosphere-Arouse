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

"""
starttime="14:58:05PM"
starttime= date_ + " " + starttime.strip('PM').strip('AM')
print(starttime)"""
#input()
##---------------------------------------------------
##------------------IMPORTANT------------------------
##---------------------------------------------------
#You should change data's experiment date and collaborator name
##---------------------------------------------------
root="C:/Users/mizukiyuta/Desktop/atmosphere/DATA/"
year="2021"
date="12-27"
date_ = year+'-'+date
name="li"
date_2="21"+date.replace("-","")
#d
##---------------------------------------------------
##read data's info (self-report csv)
file_name=name+"-"+date+"Dataset.csv"
#file_name="Miusen-12-23Dataset.csv"
print("Read csv:",file_name)
#sr_df =  pd.read_csv('%s/%s' % (data_path, sr_file_name),encoding='unicode_escape')#SR.csv
set_df = pd.read_csv(file_name,encoding='unicode_escape')
print(set_df)
print("-"*50)
#input(len(sr_df))
##---------------------------------------------------
##---------------------------------------------------
##read data's info (self-report csv)
file_name=name+"-"+date+"SR.csv"
print("Read csv:",file_name)
#sr_df =  pd.read_csv('%s/%s' % (data_path, sr_file_name),encoding='unicode_escape')#SR.csv
sr_df = pd.read_csv(file_name,encoding='unicode_escape')
print(sr_df)
print("-"*50)
#input(len(sr_df))
##---------------------------------------------------
def savecsv(filepath,data):
	data.to_csv(filepath,index=0)
	print("saved to ",filepath)
	print("-"*50) 

for i in range(len(sr_df)):
	print()
	file_name= date_2 + "_" +str(i+1)+".csv"
	voice_df = pd.read_csv(file_name,encoding='unicode_escape')
	file_name="rv"+str(i)+".csv"
	rv_df = pd.read_csv(file_name,encoding='unicode_escape')
	df = pd.concat([rv_df,voice_df],axis=1)

	save_filePath="data"+str(i)+".csv"
	savecsv(save_filePath,df)



for i in range(len(set_df)):
	ID=set_df.iloc[i]["ID"]
	data_number=ID.split("_")[0]
	
	data_name="data"+str(data_number)+".csv"
	data_df = pd.read_csv(data_name,encoding='unicode_escape')
	data_df['Time'] = pd.to_datetime(data_df['Time'])

	starttime = str(set_df['StartTime'].iloc[i])
	endtime = str(set_df['EndTime'].iloc[i])
	starttime= date_ + " " + starttime.strip('PM').strip('AM')
	endtime= date_ + " " + endtime.strip('PM').strip('AM')


	#print(data)
	print(ID,ID.split("_"),data_number,starttime,endtime)
	data = data_df[(data_df['Time'] >=starttime) & (data_df['Time'] < endtime)]
	#data.reset_index(drop=True, inplace=True)
	
	save_filePath = "data"+str(ID)+".csv"
	savecsv(save_filePath,data)

	#print(df.iloc[i]["ID"])
