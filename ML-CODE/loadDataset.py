#!/Users/tt/Desktop/kaggle_houseprice
# coding: utf-8

from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split as ts
import sys
#from numpy import *
import numpy
import pandas as pd
from os import listdir


def drop_feature(data):
    df=data
    """to_drop =['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10', 'AUX_RIGHT',
           'Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z', 'Gyro_X',
           'Gyro_Y', 'Gyro_Z', 'HeadBandOn', 'HSI_TP9', 'HSI_AF7', 'HSI_AF8',
           'HSI_TP10', 'Battery', 'Elements']"""
    to_drop =['HRV_SDANN1', 'HRV_SDNNI1', 'HRV_SDANN2', 'HRV_SDNNI2',
           'HRV_SDANN5', 'HRV_SDNNI5', 'HRV_ULF','HRV_VLF','Time','TimeStamp']
    # 丢弃特征 drop columns
    df.drop(to_drop, axis=1, inplace=True)
    #print("feature droped!")
    return df
def drop_feature2(data):
    df=data
    to_drop =['Date','StartTime','EndTime','Goal','world',
    'Unhappy-Happy','Calm-Excited','Controlled-Incontrol']
    df.drop(to_drop, axis=1, inplace=True)
    return df

def loadEmotion(dir_path):
    dirList = listdir(dir_path)
    print(dirList)
    data=[]
    label=[]
    my_matrix=[]
    
    for dir_name in dirList:
        if(dir_name==".DS_Store"):
            print("DS_Store!PASS")
            continue
        else:
             data_path=dir_path + dir_name+"/"
             
             dataset_file_name = dir_name+"Dataset.csv" #cuidenwen-09-24SR.csv
             print("try to read csv: ",data_path,dataset_file_name)
             dataset_df =  pd.read_csv('%s/%s' % (data_path, dataset_file_name),encoding='unicode_escape')#SR.csv
             #sr_df = drop_feature2(sr_df)
             #print(data_path,dataset_df)
             #input()
             for i in range(len(dataset_df)):
                 ID=str(dataset_df["ID"].iloc[i])
                 data_file_name="data"+ID+".csv"
                 print(data_file_name)
            
    import numpy as np
    from sklearn.model_selection import train_test_split
    my_matrix=np.array(my_matrix)



    #print(len(my_matrix))
    #print(my_matrix)
    X, y = my_matrix[:,:-1],my_matrix[:,-1]

 
    return X,y
	
dir_path="C:/Users/mizukiyuta/Desktop/Dataset/"
loadEmotion(dir_path)