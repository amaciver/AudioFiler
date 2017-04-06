import requests
import os
import sys
# import numpy as np

curpath = os.path.abspath(os.curdir)
pAApath = os.path.join(curpath, 'helpers/pyAudioAnalysis')
sys.path.append(pAApath)

from pyAudioAnalysis import audioFeatureExtraction as aF
from pyAudioAnalysis import audioAnalysis as aA
from pyAudioAnalysis import audioBasicIO as audioBasicIO

# from analysis_backend.helpers.pyAudioAnalysis.audioFeatureExtraction import *
# from analysis_backend.helpers.pyAudioAnalysis import audioAnalysis as aA
# from analysis_backend.helpers.pyAudioAnalysis import audioBasicIO as audioBasicIO
#

def downloadPreview(url):
    # r = requests.get(preview_url)
    r = requests.get("https://p.scdn.co/mp3-preview/7c548326fe87f76161403d00bbb3b65b988a2c17?cid=null")

    curpath = os.path.abspath(os.curdir)
    mp3_directory = "%s/%s" % ("data","preview.mp3")

    with open(os.path.join(curpath, mp3_directory), 'wb') as mp3_file:
        mp3_file.write(r.content)


downloadPreview("https://p.scdn.co/mp3-preview/7c548326fe87f76161403d00bbb3b65b988a2c17?cid=null")

#
# def bpm(filename):
#     Fs, x = audioBasicIO.readAudioFile(filename)
#     x_ = audioBasicIO.stereo2mono(x)
#     F = aF.stFeatureExtraction(x_, Fs, 0.050 * Fs, 0.050 * Fs)
#     BPM, ratio = aF.beatExtraction(F, 0.050, False)
#     return BPM
#
# vectors, filenames = aF.dirWavFeatureExtraction('./data/', 60, 30, 1, 1)
# bpms = map(bpm, [filenames])
#
# vectors_bpms = zip([vectors], bpms)
#
# arr = []
# for entry in vectors_bpms:
#     joined = np.append(entry[0], entry[1])
#     joined = joined.tolist()
#     arr.append(joined)
#
# arr = np.array(arr)
# results = zip(filenames, arr)
#
# arr2 = []
# for entry in results:
#     arr2.append(entry[1])
#
# # print results
# # print arr2
#
# ##read/write csv file
# # import csv
# # with open("test.csv", "wb") as the_file:
# #     csv.register_dialect("custom", delimiter=" ", skipinitialspace=True)
# #     writer = csv.writer(the_file, dialect="custom")
# #     for tup in results:
# #         writer.writerow(tup)
# #
# # reader = csv.reader(open("test.csv", "rb"), delimiter=' ')
# # for row in reader:
# #     print row
#
# print arr2
#
# ## save np object to txt
# # np.savetxt("subset_1000.txt", arr2)
# # load = np.loadtxt("test.txt")
# # print (np.array(load)[0])
