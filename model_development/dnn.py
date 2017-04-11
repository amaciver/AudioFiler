from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np
import tensorflow as tf

# Data sets
# IRIS_TRAINING = "iris_training.csv"
# IRIS_TRAINING_URL = "http://download.tensorflow.org/data/iris_training.csv"
#
# IRIS_TEST = "iris_test.csv"
# IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"


genres_nothot = np.loadtxt("genre_tags_not_one_hot.txt")

subset = np.loadtxt("subset_1000.txt")


def main():
  # If the training and test sets aren't stored locally, download them.
  # if not os.path.exists(IRIS_TRAINING):
  #   raw = urllib.urlopen(IRIS_TRAINING_URL).read()
  #   with open(IRIS_TRAINING, "w") as f:
  #     f.write(raw)
  #
  # if not os.path.exists(IRIS_TEST):
  #   raw = urllib.urlopen(IRIS_TEST_URL).read()
  #   with open(IRIS_TEST, "w") as f:
  #     f.write(raw)

  # Load datasets.
  # training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
  #     filename=IRIS_TRAINING,
  #     target_dtype=np.int,
  #     features_dtype=np.float32)
  # test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
  #     filename=IRIS_TEST,
  #     target_dtype=np.int,
  #     features_dtype=np.float32)

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=69)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[30, 20, 10],
                                              n_classes=26,
                                              model_dir="./dnn_model")
  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(np.array(subset[0:800], dtype="float32"))
    y = tf.constant(np.array(genres_nothot[0:800], dtype="int32"))

    return x, y

  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=4000)

  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(np.array(subset[800:], dtype="float32"))
    y = tf.constant(np.array(genres_nothot[800:], dtype="int32"))

    return x, y

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                       steps=1)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # Classify two new flower samples.
  # def new_samples():
  #   return np.array(
  #     [[6.4, 3.2, 4.5, 1.5],
  #      [5.8, 3.1, 5.0, 1.7]], dtype=np.float32)
  #
  # predictions = list(classifier.predict(input_fn=new_samples))
  #
  # print(
  #     "New Samples, Class Predictions:    {}\n"
  #     .format(predictions))

if __name__ == "__main__":
    main()
