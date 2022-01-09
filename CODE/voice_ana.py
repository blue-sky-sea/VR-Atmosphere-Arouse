# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:31:27 2021

@author: mizukiyuta
"""
from pyAudioAnalysis import ShortTermFeatures as aF
from pyAudioAnalysis import MidTermFeatures as aF2
from pyAudioAnalysis import audioBasicIO as aIO 
import numpy as np 
import plotly.graph_objs as go 
import plotly
import IPython
import pandas as pd
import pydub
from pydub import AudioSegment
from pydub.playback import play

root="C:/Users/mizukiyuta/Desktop/atmosphere/DATA/"
base_dir="2021-12-27-cui-li/"
date="211227"
dir2="cui-12-27/"
dir1="li-12-27/"
N=4
def audioAnalysis(wav_path,csv_save_path):
    # 读取音频文件
    # fs是指文中开始所说的16kHz，即每秒取16000个样本，s是指你的音频文件总的样本数
    fs, s = aIO.read_audio_file(wav_path)
    
    #+++++++++++++++++++++++++++++++++++++
    #ADD by YUTA
    s = aIO.stereo_to_mono(s)
    #+++++++++++++++++++++++++++++++++++++

    # 例如我使用的pycharm，下面这个是用来播放音频文件的，可以删去不需要播放
    #IPython.display.display(IPython.display.Audio(file_path))

    # 利用总样本数/每秒多少个样本=时长，来输出你的音频文件有多长
    duration = len(s) / float(fs)
    print(f'duration = {duration} seconds')

    """
    # 提取短期信号，win和step代表窗口和步长，f为一个[68,片段长度]的矩阵，fn为特征名称
    win, step = 0.050, 0.050
    #win, step = 1, 1
    [f, fn] = aF.feature_extraction(s, fs, int(fs * win), int(fs * step))
    print(f)
    print(f'{f.shape[1]} frames, {f.shape[0]} short-term features')
    print('Feature names:')
    for i, nam in enumerate(fn):
        print(f'{i}:{nam}')
    # plot short-term energy
    # create time axis in seconds
    time = np.arange(0, duration - step, win) 
    # get the feature whose name is 'energy'
    energy = f[fn.index('energy'), :]
    mylayout = go.Layout(yaxis=dict(title="frame energy value"),
                         xaxis=dict(title="time (sec)"))
    plotly.offline.iplot(go.Figure(data=[go.Scatter(x=time, 
                                                    y=energy)], 
                                   layout=mylayout))
"""
    #win, step = 1, 1
    mid_window, mid_step = 1,1
    """aF2.mid_feature_extraction_to_file(file_path=file_path,
                                   mid_window=mid_window, mid_step=mid_step,
                                   short_window=win, short_step=step,
                                   output_file="./",
                                   store_short_features=True, store_csv=True,
                                   plot=True)"""
    sampling_rate=fs
    short_window,short_step= 0.050, 0.050
    mid_window=int(sampling_rate * mid_window)
    mid_step=int(sampling_rate * mid_step)
    win=int(sampling_rate * short_window)
    step=int(sampling_rate * short_step)
    mid_features, short_features, mid_feature_names = aF2.mid_feature_extraction(signal=s,sampling_rate=fs,
                                    mid_window=mid_window, mid_step=mid_step,
                                   short_window=win, short_step=step)
    print(mid_features,type(mid_features))
    
    
    print(f'{mid_features.shape[1]} frames, {mid_features.shape[0]} mid-term features')
    print('Feature names:')
    mid_colums=[]
    for i, nam in enumerate(mid_feature_names):
        print(f'{i}:{nam}')
        mid_colums.append(nam)
    #print(mid_colums)
    data1 = pd.DataFrame(mid_features.T,columns=mid_colums)
    #data1 = pd.DataFrame(mid_features,columns=mid_colums)
    print(data1)
    file_path=csv_save_path
    data1.to_csv(file_path,index=0)

if __name__ == '__main__':
    data_file = root+base_dir+dir1
    """
    mp3_path = data_file +"211223_1"+".mp3"
    MP3_File = AudioSegment.from_file(mp3_path)

    wav_path = data_file +"211223_1"+".wav"
    MP3_File.export(wav_path,format="wav")

    csv_save_path = data_file+"211223_1"+"test.csv"
    audioAnalysis(wav_path,csv_save_path)
    """
    for i in range(N):
        filename=date+"_"+str(i+1)
        mp3_path = data_file + filename + ".mp3"
        MP3_File = AudioSegment.from_file(mp3_path)

        wav_path = data_file + filename +".wav"
        MP3_File.export(wav_path,format="wav")
        
        csv_save_path = data_file + filename +".csv"
        audioAnalysis(wav_path,csv_save_path)
        print("saved csv to ",csv_save_path)
