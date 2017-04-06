import numpy as np
import tensorflow as tf
import math

NUM_CLASSES = 26
AUDIO_FEATURES = 69
hidden1_units = 30
hidden2_units = 30

c = np.array([[0.13169837562454179, 0.03747907258948448, 3.2093567363765194, 0.20415217142414294, 0.1783023422538795, 1.2981390056554678, 0.00013002260238153973, 0.24316704459561597, -18.057689533187364, 1.0821583049391887, 0.022808529642138784, 0.1549138769242293, 0.5485543540631203, 0.24687343351752963, 0.001938394071525701, -0.029246965650714545, 0.32433651932613095, 0.5493794894195386, -0.1532108536935117, -0.15953240858525616, -0.14292504685871826, 0.001022193915855823, 0.000574248578652918, 0.003744947243702289, 0.0006085355445014114, 0.002063131254826033, 0.003100602255608477, 0.0014455207769336613, 0.003737979544046202, 0.0006869733130853256, 0.0018058484190229462, 0.0019889269642760373, 0.0013000858126485423, 0.0019709657966293925, 0.018371489884997885, 0.0038319853094609868, 0.053279939984258194, 0.012001309617731878, 0.007287461986689352, 0.1875974718744425, 4.252950874934398e-05, 0.04607723005339392, 0.2630779792539925, 0.23210117834659488, 0.17928284477236567, 0.12835441277409773, 0.3027672361440782, 0.12774041196099692, 0.14183339098145453, 0.23304445814417998, 0.2613883636021474, 0.212724386971971, 0.1524114531785372, 0.15298324799066315, 0.11769770369920446, 0.0010044220119722683, 0.00047814477640875284, 0.003668243077559693, 0.0003353471455472499, 0.0022506117030398343, 0.003720407974634264, 0.0010744772528963858, 0.003050953233744261, 0.0005532878059932616, 0.0015633060547211519, 0.001632379520800961, 0.0009701856688470633, 0.0010768320828846707, 199.99999999999997]])

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
  # tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

#training step with learning rate
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(cross_entropy)

saver = tf.train.Saver()

with tf.Session() as sess:
    tf.global_variables_initializer().run()


    for _ in range(1000):
        sess.run(train_step, feed_dict={x: na_train, y_nothot: labels_train_nothot})

    # correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # print(sess.run((y, accuracy), feed_dict={x: na_test, y_: labels_test}))

    correct = tf.nn.in_top_k(y, y_nothot, 5)
    eval_correct = tf.reduce_sum(tf.cast(correct, tf.int32))
    num_examples = 200
    true_count = 0  # Counts the number of correct predictions.
    true_count += sess.run(eval_correct, feed_dict={x: na_test, y_nothot: labels_test_nothot})
    precision = float(true_count) / num_examples
    print('  Num examples: %d  Num correct: %d  Precision @ 5: %0.04f' %
    (num_examples, true_count, precision))
    a = (sess.run(y, feed_dict={x: c, y_nothot: [13]}))
    a = np.array(a)
    amin = a[0].min()
    amax = a[0].max()

    z = (a[0]-amin)/(amax-amin)
    p = z/z.sum()
    p = np.round(p, 2)*100
    print (amin)
    print (amax)
    print (a)
    print (z)
    print (p)



    # save_path = saver.save(sess, './model.ckpt')
