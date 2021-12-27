# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:29:46 2021

@author: mizukiyuta
"""
wave_file=r"C://Users//mizukiyuta//Desktop//atmosphere//211223_001.WAV"
import pylab as pl
import matplotlib.pyplot as plt
import wave
import numpy as np
# 打开已有的音频
with wave.open("./211223_001.WAV", 'rb') as wr:
      # 参数：(nchannels, sampwidth, framerate, nframes, comptype, compname)
      params = wr.getparams()
      print(params)
      #channels
      channels = params[0]
      # 采样位数
      sampwidth = params[1]
      # 采样频率
      framerate = params[2]
      # 总帧数
      nframes = params[3]
      # 读取音频数据
      data = wr.readframes(nframes)
      
# 写入新音频
with wave.open("./211223_001_new_solved.WAV", 'wb') as ww:
      # 有需要可以分别设置各项参数
      ww.setparams(params)
      # 帧数据是byte[]的格式，索引 = 秒数 * 采样位数(字节) * 采样率
      #print(data)
      n=52
      m=52+60*3-20
      new_data=data[ n *channels * sampwidth * framerate : m *channels* sampwidth * framerate]
      
      wave_data = np.fromstring(new_data, dtype=np.short)
      print(wave_data,type(wave_data))
      wave_data[(wave_data<208)&  (wave_data>-208)]=0
      #print(wave_data,type(wave_data))
      #wave_data.tostring()
      #ww.writeframes(new_data)
      ww.writeframes(wave_data.tostring())


f = wave.open("./211223_001_new_solved.WAV",'rb')
str_data = f.readframes(nframes)
params = f.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
print(params)
#b_data=np.frombuffer(new_data,dtype=np.float32)
#print(b_data,len(b_data))
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1,2
wave_data = wave_data.T
print(wave_data,len(wave_data))
      #print(wave_data)
#print(wave_data)
#print(len(wave_data))

time = np.arange(0,nframes)*(1.0/framerate)

#print(wave_data)
#print(len(wave_data))
plt.plot(time,wave_data[1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude") 
plt.title("Single channel wavedata")
plt.show()