#!/Users/tt/Desktop/kaggle_houseprice
# coding: utf-8

from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split as ts
import sys
#from numpy import *
#import numpy
import pandas as pd
from os import listdir
import numpy as np
from sklearn.model_selection import train_test_split

def drop_feature(data):
    df=data
    """to_drop =['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10', 'AUX_RIGHT',
           'Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z', 'Gyro_X',
           'Gyro_Y', 'Gyro_Z', 'HeadBandOn', 'HSI_TP9', 'HSI_AF7', 'HSI_AF8',
           'HSI_TP10', 'Battery', 'Elements']"""
    to_drop =['HRV_SDANN1', 'HRV_SDNNI1', 'HRV_SDANN2', 'HRV_SDNNI2',
           'HRV_SDANN5', 'HRV_SDNNI5', 'HRV_ULF','HRV_VLF','Time']
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
    p_n=0
    n_n=0
    for dir_name in dirList:
        if(dir_name==".DS_Store"):
            print("DS_Store!PASS")
            continue
        else:

             data_path=dir_path + dir_name+"/"
             
             dataset_file_name = dir_name+"Dataset.csv" #cuidenwen-09-24SR.csv
             print("try to read SRcsv: ",data_path,dataset_file_name)
             dataset_df =  pd.read_csv('%s/%s' % (data_path, dataset_file_name),encoding='unicode_escape')#SR.csv
             #sr_df = drop_feature2(sr_df)
             #print(data_path,dataset_df)
             #input()
             for i in range(len(dataset_df)):
                 ID=str(dataset_df["ID"].iloc[i])

                 data_file_name="data"+ID+".csv"
                 data_df =  pd.read_csv('%s/%s' % (data_path, data_file_name),encoding='unicode_escape')
                 data_df = drop_feature(data_df)
                 #print(data_file_name)
                 data_=[]
                 if(len(data_df)>=60):
                     for j in range(60):
                         data_.extend(data_df.iloc[j].values)
                 else:
                     input("?")
                     continue

                 label_=0

                 score= float(dataset_df["Excite"].iloc[i])
                 if(score<3):
                    label_=1.0
                    p_n=p_n+1
                 elif(score>=3):
                    label_=-1.0
                    n_n=n_n+1
                 #print(ID,score,label_)
                 data_.extend([label_])
                 my_matrix.append(data_)
            

    my_matrix=np.array(my_matrix)
    #my_matrix=np.array(my_matrix)



    #print(len(my_matrix))
    #print(my_matrix)
    #X, y = my_matrix[:,:-1],my_matrix[:,-1]
    X,y=1,2
    print("正样本数：",p_n," 负样本数：",n_n)
    X, y = my_matrix[:,:-1],my_matrix[:,-1]
    return X,y


dir_path="C:/Users/mizukiyuta/Desktop/ATMO/Dataset/"
X,y = loadEmotion(dir_path)
print(y)