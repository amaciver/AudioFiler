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

# oh I'll have to wrap filenames and vectors in an array if there is only one file
vectors_bpms = zip(vectors, bpms)

arr = []
for entry in vectors_bpms:
    joined = np.append(entry[0], entry[1])
    joined = joined.tolist()
    arr.append(joined)

arr = np.array(arr)
results = zip(filenames, arr)

np.savetxt("test.txt", arr)
print results
