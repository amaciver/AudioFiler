import os
import sys
import requests
import numpy as np

curpath = os.path.abspath(os.curdir)
tf_path = os.path.join(curpath, 'helpers/tensorflow')
model_path = os.path.join(curpath, 'helpers/completed_model')
forest_path = os.path.join(curpath, 'helpers/trained_forest')

sys.path.append(tf_path)
sys.path.append(model_path)

import tensorflow as tf
import math
from scipy import stats
import os

# test object
# b = np.array([[0.028668688727673662, 0.010296874642310268, 2.979289570795993, 0.07771797022261993, 0.12198492962551129, 0.07406470247848689, 0.001981627735053664, 0.039223117818555996, -23.012398288066628, 2.450383013402157, -0.7209535825894928, 0.07425339479431828, -0.47001386542844525, 0.006088903086235553, 0.01620690020921406, 0.21418823151639632, -0.052091687642100086, -0.014820133215621163, -0.04205860250594405, 0.04366025985499307, -0.031519931259828125, 0.002860475089759992, 0.0003646468375155665, 0.002032433781725561, 0.0021552882054243646, 0.0025839743774277875, 0.0009058216527170049, 0.0008695032351243258, 0.00068567444148368, 0.0006254911744017183, 0.0007357199054872923, 0.0006408451163334997, 0.002221595279796925, 0.0020110988491125782, 0.006846064570096212, 0.008456917276021512, 0.34895182207509867, 0.06382364407926983, 0.0707189929354555, 0.06751763540513239, 0.0010086845302658034, 0.014315807864655895, 4.4706546531721365, 0.43612756476174575, 0.40739917406157244, 0.35130193768906803, 0.2341932299542251, 0.1972104508417759, 0.23544222276288154, 0.1671490418787359, 0.3489483337061661, 0.2637239292016653, 0.23975431205775216, 0.21894401585821305, 0.2024376957834217, 0.006628432758045184, 0.00038632059557007806, 0.005343911639298718, 0.002902033201242365, 0.00517548217374744, 0.002131617367862237, 0.0012211411343064536, 0.0009310703900695344, 0.0005492201558132859, 0.0007178880923363045, 0.0007566149509813329, 0.006080275164001775, 0.0026897796057824743, 199.99999999999997]])

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas as pd

def run_forests(vector):
    single_song_features = np.array(vector, dtype='int32')
    classifications = []
    for i in range(0, 20):
        clf = joblib.load(os.path.join(forest_path, "model_%(i)s.pk1" % locals()))
        preds = clf.predict(single_song_features)
        classifications.append(preds[0])

    return(classifications)

def run_model(vector):

    # Model Parameters
    NUM_CLASSES = 26
    AUDIO_FEATURES = 69
    hidden1_units = 30
    hidden2_units = 30

    # Input placeholder
    x = tf.placeholder(tf.float32, [None, 69])

    ## Graph
    # Hidden 1 Layer
    with tf.name_scope('hidden1'):
      weights = tf.Variable(
          tf.truncated_normal([AUDIO_FEATURES, hidden1_units],
                              stddev=1.0 / math.sqrt(float(AUDIO_FEATURES))),
          name='weights')
      biases = tf.Variable(tf.zeros([hidden1_units]),
                           name='biases')
      hidden1 = tf.nn.relu(tf.matmul(x, weights) + biases)
    # Hidden 2 Layer
    with tf.name_scope('hidden2'):
      weights = tf.Variable(
          tf.truncated_normal([hidden1_units, hidden2_units],
                              stddev=1.0 / math.sqrt(float(hidden1_units))),
          name='weights')
      biases = tf.Variable(tf.zeros([hidden2_units]),
                           name='biases')
      hidden2 = tf.nn.relu(tf.matmul(hidden1, weights) + biases)
    # Linear Layer
    with tf.name_scope('softmax_linear'):
      weights = tf.Variable(
          tf.truncated_normal([hidden2_units, NUM_CLASSES],
                              stddev=1.0 / math.sqrt(float(hidden2_units))),
          name='weights')
      biases = tf.Variable(tf.zeros([NUM_CLASSES]),
                           name='biases')
      y = tf.matmul(hidden2, weights) + biases


    # Saver object
    saver = tf.train.Saver()

    # Session
    with tf.Session() as sess:
      # Restore variables from disk
      saver.restore(sess, os.path.dirname(os.path.realpath(__file__)) + '/completed_model/model.ckpt')
      print("Model restored.")

      # Evaluate model
      a = y.eval({x: vector})
      a = np.array(a)

      # Normalize output
      amin = a[0].min()
      amax = a[0].max()
      z = (a[0]-amin)/(amax-amin)
      stddev = np.std(z)

      # Proportional distribution
      p = z/z.sum()
      p = np.round(p, 3)

      # Get top four indices and sort
      ind = np.argpartition(z, -5)[-5:]
      sort = np.flipud(ind[np.argsort(z[ind])])

    #   # Z-scores, StdDev and Prints
    #   print (p)
    #   print (stats.zscore(p))
    #   print(z[ind])
    #   print(stddev)
    #   print(ind)
    #   print (sort)
      return sort


# # Run Model
# run_model(b)
