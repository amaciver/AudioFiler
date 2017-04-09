from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas as pd
import numpy as np

def run_forests(vectors):
    single_song_features = np.array(features_array, dtype='int32')
    classifications = []
    for i in range(0, 20):
        clf = joblib.load("./trained_forest/model_%(i)s.pk1" % locals())
        preds = clf.predict(single_song_features)
        classifications.append(preds[0])

    return(classifications)
