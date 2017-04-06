import numpy as np
import tensorflow as tf
import math

NUM_CLASSES = 26
AUDIO_FEATURES = 69
hidden1_units = 30
hidden2_units = 26

genres = np.loadtxt("genre_tags.txt")
genres_nothot = np.loadtxt("genre_tags_not_one_hot.txt")

subset = np.loadtxt("subset_1000.txt")

na_train = np.array(subset[0:800], dtype="float32")
labels_train = np.array(genres[0:800], dtype="float32")
labels_train_nothot = np.array(genres_nothot[0:800], dtype="int32")

na_test = np.array(subset[800:], dtype="float32")
labels_test = np.array(genres[800:], dtype="float32")
labels_test_nothot = np.array(genres_nothot[800:], dtype="int32")

print (len(na_train))
print (len(labels_train))

# naive model
# x = tf.placeholder(tf.float32, [None, 69]) #[num_images, dimensionality of each]
# W = tf.Variable(tf.zeros([69, 26])) #[dimensionality of input, dimensionality of output]
# b = tf.Variable(tf.zeros([26])) #[dimensionality of output]
# y = tf.matmul(x, W) + b #the model, will have dimensionality num_images, num_outputs

# y_ = tf.placeholder(tf.float32, [None, 26])
y_nothot = tf.placeholder(tf.int32, [None])
x = tf.placeholder(tf.float32, [None, 69])

# Graph
with tf.name_scope('hidden1'):
  weights = tf.Variable(
      tf.truncated_normal([AUDIO_FEATURES, hidden1_units],
                          stddev=1.0 / math.sqrt(float(AUDIO_FEATURES))),
      name='weights')
  biases = tf.Variable(tf.zeros([hidden1_units]),
                       name='biases')
  hidden1 = tf.nn.relu(tf.matmul(x, weights) + biases)
# Hidden 2
with tf.name_scope('hidden2'):
  weights = tf.Variable(
      tf.truncated_normal([hidden1_units, hidden2_units],
                          stddev=1.0 / math.sqrt(float(hidden1_units))),
      name='weights')
  biases = tf.Variable(tf.zeros([hidden2_units]),
                       name='biases')
  hidden2 = tf.nn.relu(tf.matmul(hidden1, weights) + biases)
# Linear
with tf.name_scope('softmax_linear'):
  weights = tf.Variable(
      tf.truncated_normal([hidden2_units, NUM_CLASSES],
                          stddev=1.0 / math.sqrt(float(hidden2_units))),
      name='weights')
  biases = tf.Variable(tf.zeros([NUM_CLASSES]),
                       name='biases')
  y = tf.matmul(hidden2, weights) + biases

#loss function
cross_entropy = tf.reduce_mean(
  tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.to_int64(y_nothot), logits=y))

#training step with learning rate
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

saver = tf.train.Saver()

with tf.Session() as sess:
    tf.global_variables_initializer().run()


    for _ in range(1000):
        sess.run(train_step, feed_dict={x: na_train, y_nothot: labels_train_nothot})

    # correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # print(sess.run((y, accuracy), feed_dict={x: na_test, y_: labels_test}))

    correct = tf.nn.in_top_k(y, y_nothot, 3)
    eval_correct = tf.reduce_sum(tf.cast(correct, tf.int32))
    num_examples = 200
    true_count = 0  # Counts the number of correct predictions.
    true_count += sess.run(eval_correct, feed_dict={x: na_test, y_nothot: labels_test_nothot})
    precision = float(true_count) / num_examples
    print('  Num examples: %d  Num correct: %d  Precision @ 3: %0.04f' %
    (num_examples, true_count, precision))


    # save_path = saver.save(sess, './model.ckpt')
