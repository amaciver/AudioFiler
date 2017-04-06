import requests
import os
import sys
import numpy as np

curpath = os.path.abspath(os.curdir)
pAApath = os.path.join(curpath, 'helpers/pyAudioAnalysis')
mp3_directory = os.path.join(curpath, "data/preview.mp3")
sys.path.append(pAApath)

from pyAudioAnalysis import audioFeatureExtraction as aF
from pyAudioAnalysis import audioAnalysis as aA
from pyAudioAnalysis import audioBasicIO as audioBasicIO


def downloadPreview(preview_url):
    r = requests.get(preview_url)


    with open(os.path.join(mp3_directory), 'wb') as mp3_file:
        mp3_file.write(r.content)

def bpm():
    Fs, x = audioBasicIO.readAudioFile(mp3_directory)
    x_ = audioBasicIO.stereo2mono(x)
    F = aF.stFeatureExtraction(x_, Fs, 0.050 * Fs, 0.050 * Fs)
    BPM, ratio = aF.beatExtraction(F, 0.050, False)
    return BPM

def extractFeatures():
    vectors, filenames = aF.dirWavFeatureExtraction(os.path.join(curpath, 'data'), 60, 30, 1, 1)
    arr = []
    joined = np.append(vectors, bpm())
    joined = joined.tolist()
    arr.append(joined)

    return arr
