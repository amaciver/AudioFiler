from pyAudioAnalysis import audioFeatureExtraction as aF
from pyAudioAnalysis import audioAnalysis as aA
from pyAudioAnalysis import audioBasicIO as audioBasicIO

# from pyAudioAnalysis import dirWavFeatureExtraction as ltFeatureExt
# from pyAudioAnalysis import beatExtraction as beatExtraction
# from pyAudioAnalysis import convertDirMP3ToWav as DirMp3ToWav


# convert every file in directory to WAV
audioBasicIO.convertDirMP3ToWav('../test_data', 16000, 1, true)

def bpm(filename):
    Fs, x = audioBasicIO.readAudioFile(filename)
    F = aF.stFeatureExtraction(x, Fs, 0.050 * Fs, 0.050 * Fs)
    BPM, ratio = aF.beatExtraction(F, 0.050, False)
    return BPM

vectors, filenames = aF.dirWavFeatureExtraction('../test_data', 60, 30, 1, 1)
bpms = map(bpm, filenames)

results = zip(filenames, [vectors], bpms)

print results

# record each tuple as a csv or something
# figure out how I'll be accessing the tags
