from pyAudioAnalysis import audioFeatureExtraction as aF
from pyAudioAnalysis import audioAnalysis as aA
from pyAudioAnalysis import audioBasicIO as audioBasicIO

import numpy as np

# from pyAudioAnalysis import dirWavFeatureExtraction as ltFeatureExt
# from pyAudioAnalysis import beatExtraction as beatExtraction
# from pyAudioAnalysis import convertDirMP3ToWav as DirMp3ToWav


# convert every file in directory to WAV
# audioBasicIO.convertDirMP3ToWav('./test_data', 16000, 1, True)

def bpm(filename):
    Fs, x = audioBasicIO.readAudioFile(filename)
    x_ = audioBasicIO.stereo2mono(x)
    F = aF.stFeatureExtraction(x_, Fs, 0.050 * Fs, 0.050 * Fs)
    BPM, ratio = aF.beatExtraction(F, 0.050, False)
    return BPM

vectors, filenames = aF.dirWavFeatureExtraction('./test_data', 60, 30, 1, 1)
bpms = map(bpm, filenames)

# print vectors
# print filenames


# oh I'll have to wrap filenames and vectors in an array if there is only one file
vectors_bpms = zip(vectors, bpms)
# print vectors_bpms
# arr = np.array([])
arr = []
for entry in vectors_bpms:
    # print vector[0]
    # print vector[1]
    joined = np.append(entry[0], entry[1])
    joined = joined.tolist()
    # print joined
    arr.append(joined)
    # arr = np.concatenate((arr, joined), axis=0)
    # print arr

# print arr
# results = zip(filenames, vectors, bpms)
results = zip(filenames, arr)
#
print results

# record each tuple as a csv or something
# figure out how I'll be accessing the tags
