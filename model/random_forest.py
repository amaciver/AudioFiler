






# na_test = np.array([a,b,c])
# labels_test = np.array([[0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])


# hparams = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
#         num_trees=3, max_nodes=1000, num_classes=26, num_features=69)
# classifier = tf.contrib.learn.TensorForestEstimator(hparams)
#
# monitors = [tf.contrib.learn.TensorForestLossMonitor(10, 10)]
# classifier.fit(x=na, y=labels, steps=100, monitors=monitors)
# classifier.evaluate(x=na_, y=labels_, steps=10)



####
   # Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""A stand-alone example for tf.learn's random forest model on mnist."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
import argparse
import sys
import tempfile

# pylint: disable=g-backslash-continuation
from tensorflow.contrib.learn.python.learn\
        import metric_spec
from tensorflow.contrib.learn.python.learn.estimators\
        import estimator
from tensorflow.contrib.tensor_forest.client\
        import eval_metrics
from tensorflow.contrib.tensor_forest.client\
        import random_forest
from tensorflow.contrib.tensor_forest.python\
        import tensor_forest
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.platform import app

FLAGS = None

genres = np.loadtxt("genre_tags_not_one_hot.txt")
subset = np.loadtxt("subset_1000.txt")
# print (len(load))
na_train = np.array(subset[0:800], dtype="float32")
labels_train = np.array(genres[0:800], dtype="uint8")
na_test = np.array(subset[800:], dtype="float32")
labels_test = np.array(genres[800:], dtype="uint8")

print (len(na_test))
print (len(labels_test))
print (len(na_train))
print (len(labels_train))


def build_estimator(model_dir):
  """Build an estimator."""
  params = tensor_forest.ForestHParams(
      num_classes=26, num_features=69,
      num_trees=FLAGS.num_trees, max_nodes=FLAGS.max_nodes)
  graph_builder_class = tensor_forest.RandomForestGraphs
  if FLAGS.use_training_loss:
    graph_builder_class = tensor_forest.TrainingLossForest
  # Use the SKCompat wrapper, which gives us a convenient way to split
  # in-memory data like MNIST into batches.
  return estimator.SKCompat(random_forest.TensorForestEstimator(
      params, graph_builder_class=graph_builder_class,
      model_dir=model_dir))


def train_and_eval():
  """Train and evaluate the model."""
  model_dir = tempfile.mkdtemp() if not FLAGS.model_dir else FLAGS.model_dir
  print('model directory = %s' % model_dir)

  est = build_estimator(model_dir)

  # mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=False)
  print (est)

  est.fit(x=na_train, y=labels_train,
          batch_size=FLAGS.batch_size, steps=FLAGS.train_steps)

  metric_name = 'accuracy'
  metric = {metric_name:
            metric_spec.MetricSpec(
                eval_metrics.get_metric(metric_name),
                prediction_key=eval_metrics.get_prediction_key(metric_name))}

  results = est.score(x=na_test, y=labels_test,
                      batch_size=FLAGS.batch_size,
                      metrics=metric)
  for key in sorted(results):
    print('%s: %s' % (key, results[key]))


def main(_):
  train_and_eval()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--model_dir',
      type=str,
      default='',
      help='Base directory for output models.'
  )
  parser.add_argument(
      '--data_dir',
      type=str,
      default='/tmp/data/',
      help='Directory for storing data'
  )
  parser.add_argument(
      '--train_steps',
      type=int,
      default=10,
      help='Number of training steps.'
  )
  parser.add_argument(
      '--batch_size',
      type=str,
      default=100,
      help='Number of examples in a training batch.'
  )
  parser.add_argument(
      '--num_trees',
      type=int,
      default=3,
      help='Number of trees in the forest.'
  )
  parser.add_argument(
      '--max_nodes',
      type=int,
      default=1000,
      help='Max total nodes in a single tree.'
  )
  parser.add_argument(
      '--use_training_loss',
      type=bool,
      default=False,
      help='If true, use training loss as termination criteria.'
  )
  FLAGS, unparsed = parser.parse_known_args()
  app.run(main=main, argv=[sys.argv[0]] + unparsed)
