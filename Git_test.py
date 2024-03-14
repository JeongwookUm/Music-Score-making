#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:35:34 2024

@author: umzzangu

git, github test code
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 05:24:23 2024

@author: umzzangu
"""
import librosa
import matplotlib.pyplot as plt
import subprocess


# 원본 WebM 파일 경로
webm_input_path = "/Users/umzzangu/MusicScore/Soundtrack_download/testST_2.webm"

# 변환한 WAV 파일 경로와 이름
wav_output_path = "/Users/umzzangu/MusicScore/Soundtrack_download/testST_2.wav"
'''
# ffmpeg를 사용하여 WebM 파일을 WAV 형식으로 변환
command = ['/opt/homebrew/bin/ffmpeg', '-i', webm_input_path, wav_output_path]
subprocess.run(command)
'''
# Librosa를 사용하여 WAV 파일 불러오기
y, sr = librosa.load(wav_output_path)

# waveform plot
fig, ax = plt.subplots(nrows=3, sharex=True)

# x 축 범위를 음원의 처음부터 끝까지로 설정
ax[0].set_xlim(0, len(y) / sr)

librosa.display.waveshow(y, sr=sr, ax=ax[0])
ax[0].set(title='Envelope view, mono')
ax[0].label_outer()



