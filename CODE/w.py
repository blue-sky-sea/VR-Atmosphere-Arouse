# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:04:47 2021

@author: mizukiyuta
"""


import wave
import pylab as pl
import matplotlib.pyplot as plt

import numpy as np
import os
f = wave.open(r"C://Users//mizukiyuta//Desktop//atmosphere//211223_001_new.WAV",'rb')

params = f.getparams()
nchannels,sampwidth,framerate,nframes = params[:4]
print(params)

str_data = f.readframes(nframes)
#截取n秒-m秒的声音
#n=46
#m=46+30
#str_data = str_data[n * sampwidth * framerate : m * sampwidth * framerate]

f.close()

wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1,2
wave_data = wave_data.T
#waveData = waveData*1.0/(max(abs(waveData)))

time = np.arange(0,nframes)*(1.0/framerate)

print(wave_data)
print(len(wave_data))
plt.plot(time,wave_data[1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude") 
plt.title("Single channel wavedata")
plt.show()