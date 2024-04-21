#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:28:15 2024

@author: umzzangu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import stft

# WAV 파일에서 오디오 데이터 읽기
sample_rate, data = wavfile.read('72hz_sine.mp3')

# FFT 적용
fft_result = fft(data)
fft_freq = np.fft.fftfreq(len(fft_result))

# FFT 결과 시각화
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(fft_freq, np.abs(fft_result))
plt.title('FFT 결과')
plt.xlabel('빈도 (Hz)')
plt.ylabel('진폭')

# STFT 적용
f, t, Zxx = stft(data, fs=sample_rate, nperseg=1024)
Zxx_abs = np.abs(Zxx)

# STFT 결과 시각화
plt.subplot(2, 1, 2)
plt.pcolormesh(t, f, Zxx_abs, shading='gouraud')
plt.title('STFT 결과')
plt.ylabel('빈도 (Hz)')
plt.xlabel('시간 (sec)')
plt.tight_layout()
plt.show()
