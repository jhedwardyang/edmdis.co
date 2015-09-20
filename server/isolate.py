from pylab import*
import numpy as np
from scipy.io import wavfile
import pandas as pd

def process(c0):
    c0fft = fft(c0)
    c0ffthi = np.copy(c0fft)

    #fftshift(c0fft)
    tot = len(c0fft)
    #print type(c0fft[0])

    for i in range(0, tot/2):

        if i < (tot / 50):
            c0fft[i] *= 3
            c0fft[tot - i - 1] *= 3
            c0ffthi[i] = 0# /= 5
            c0ffthi[tot - i - 1] = 0 #/= 5
        else:
            c0fft[i] = 0 #/= 5
            c0fft[tot - i - 1] = 0 #/= 5
            c0ffthi[i] *= 3
            c0ffthi[tot - i - 1] *= 3


    c0 = ifft(c0fft)
    c0hi = ifft(c0ffthi)

    c0_copy = np.copy(c0)
    c0hi_copy = np.copy(c0hi)

    for i in range(0, len(c0) - 4):
        c0[i + 2] = (c0_copy[i] + c0_copy[i + 1] + c0_copy[i + 2] + c0_copy[i + 3] + c0_copy[i + 4]) / 20
        c0hi[i + 2] = (c0hi_copy[i] + c0hi_copy[i + 1] + c0hi_copy[i + 2] + c0hi_copy[i + 3] + c0hi_copy[i + 4]) / 20

    c0 = (c0 * 1.0 / max(c0)) * 10000
    c0hi = (c0hi * 1.0 / max(c0hi)) * 10000

    return c0, c0hi

def isolate(target):
    sampFreq, snd = wavfile.read(target)
    snd = snd[:sampFreq*60]#[:sampFreq*60]

    snd_edit = np.empty_like(snd)

    c0 = snd[:,0] 
    c1 = snd[:,1]

    c0, c0hi = process(c0)
    #c1, c1hi = process(c1)

    snd[:,0] = c0
    snd[:,1] = c0#c1
    
    wavfile.write(target[:-4] + '_low.wav', sampFreq, snd)

    snd[:,0] = c0hi
    snd[:,1] = c0hi#c1hi
    wavfile.write(target[:-4] + '_high.wav', sampFreq, snd)
