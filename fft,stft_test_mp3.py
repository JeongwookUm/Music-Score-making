#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:33:23 2024

@author: umzzangu
"""

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# mp3 파일 로드
file_path = 'Bass_D.mp3'
data, sample_rate = librosa.load(file_path, sr=None)

# FFT 적용
fft_result = np.fft.fft(data)
fft_freq = np.fft.fftfreq(len(fft_result), 1/sample_rate)

# FFT 결과 시각화
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(fft_freq, np.abs(fft_result))
plt.title('FFT')
plt.xlabel('(Hz)')
plt.ylabel('Amplitue')

# x축 스케일 조정
plt.xlim(0,400)

# STFT 적용
D = librosa.stft(data, n_fft=2048, hop_length=512)
DB = librosa.amplitude_to_db(abs(D), ref=np.max)

# STFT 결과 시각화
plt.subplot(2, 1, 2)
librosa.display.specshow(DB, sr=sample_rate, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('STFT')
plt.tight_layout()
plt.show()
