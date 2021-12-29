# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:31:27 2021

@author: mizukiyuta
"""
#pip install pydub
#pip install ffmpeg
#pip install pyaudio
import pydub
from pydub import AudioSegment
from pydub.playback import play
import pylab as pl
import matplotlib.pyplot as plt
import wave
import numpy as np
import random
import os

def pre_deal(file_path):
    """音频解析，返回音频数据"""
    f = wave.open(file_path, 'rb')
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = f.readframes(nframes)  # 读取音频，字符串格式
    waveData = np.fromstring(strData, dtype=np.int16)  # 将字符串转化为int

    waveData = waveData[::nchannels]  # 根据声道数，转换为单声道
    
    #为了提升机器学习速度，修改采样率为20分之一，来降低数据量
    rate = 20.00
    framerate = framerate / rate  # 降低帧率
    nframes = nframes / rate  # 降低帧率
    waveData = waveData[::int(rate)]

    # wave幅值归一化
    max_ = float(max(abs(waveData)))
    waveData = waveData / max_

    return waveData, framerate, nframes

def plpot(waveData):
    """画图"""
    time = [i for i, v in enumerate(waveData)]
    plt.plot(time, waveData)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Single channel wavedata")
    plt.grid('on')  # 标尺，on：有，off:无。
    plt.show()


def mp3towav(file_path, to_file_path):
    """mp3文件转wav文件"""
    if os.path.exists(to_file_path):
        return to_file_path
    from pydub import AudioSegment
    print(file_path)
    song1 = AudioSegment.from_mp3(file_path)
    song1.export(to_file_path, 'wav')
    return to_file_path

if __name__ == '__main__':
    filepath="C:/Users//mizukiyuta/Desktop/atmosphere/DATA/2021-12-27-chen-lei/chen-12-27/"
    #filepath="C:/Users/mizukiyuta/Desktop/atmosphere/DATA/2021-12-27-chen-lei/lei-12-27/"
    mp3_name = "211227_1417_new"
    file_path = filepath+mp3_name+'.mp3'
    to_file_path = mp3towav(file_path, file_path.replace('mp3', 'wav'))
    data, _, _ = pre_deal(to_file_path)
    plpot(data)