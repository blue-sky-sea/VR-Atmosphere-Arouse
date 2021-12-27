# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:31:27 2021

@author: mizukiyuta
"""
#pip install pydub
#pip install ffmpeg
#pip install pyaudio
from pydub import AudioSegment
from pydub.playback import play

voice = AudioSegment.from_file("./002.mp3").set_frame_rate(22050)

start_m = 46*1000
end_m = (46+10)*1000
new_voice = voice[start_m:end_m]
play(new_voice)