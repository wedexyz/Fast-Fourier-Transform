#program to show the filtering
#written by Syahril Siregar
#2017/6/27
#Sendai

import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.fftpack

w1 = 100 #frequency asli
w2 = 150 #frequency asli
w3 = 300 #frequency asli
w4 = 400 #frequency asli
N = 1000
T = 1.0/1000
t = np.linspace(0,N*T,N)
y =1*(np.sin(w1*2*np.pi*t)+np.cos(w2*2*np.pi*t)+np.sin(w3*2*np.pi*t)+np.cos(w4*2*np.pi*t))
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
plt.subplot(211)
plt.plot(t,y)
plt.title('Signal')
plt.subplot(212)
plt.plot(xf,2.0/N * np.abs(yf[:N//2]))
plt.title('Frekuensi')
plt.show()
