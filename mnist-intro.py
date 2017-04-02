import numpy as np
import tensorflow as tf

# # Model parameters
# W = tf.Variable([.3], tf.float32)
# b = tf.Variable([-.3], tf.float32)
# # Model input and output
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b
# y = tf.placeholder(tf.float32)
# # loss
# loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# # optimizer
# optimizer = tf.train.GradientDescentOptimizer(0.01)
# train = optimizer.minimize(loss)
# # training data
# x_train = [6,2,3,4]
# y_train = [0,-1,-2,-3]
# # training loop
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init) # reset values to wrong
# for i in range(1000):
#   sess.run(train, {x:x_train, y:y_train})
#
# # evaluate training accuracy
# curr_W, curr_b, curr_loss  = sess.run([W, b, loss], {x:x_train, y:y_train})
# print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))


#####
#####
#####
#####
#####

# # Declare list of features. We only have one real-valued feature. There are many
# # other types of columns that are more complicated and useful.
# features = [tf.contrib.layers.real_valued_column("x", dimension=1)]
#
# # An estimator is the front end to invoke training (fitting) and evaluation
# # (inference). There are many predefined types like linear regression,
# # logistic regression, linear classification, logistic classification, and
# # many neural network classifiers and regressors. The following code
# # provides an estimator that does linear regression.
# estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)
#
# # TensorFlow provides many helper methods to read and set up data sets.
# # Here we use `numpy_input_fn`. We have to tell the function how many batches
# # of data (num_epochs) we want and how big each batch should be.
# x = np.array([1., 2., 3., 4.])
# y = np.array([0., -1., -2., -3.])
# input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,
#                                               num_epochs=1000)
#
# # We can invoke 1000 training steps by invoking the `fit` method and passing the
# # training data set.
# estimator.fit(input_fn=input_fn, steps=1000)
#
# # Here we evaluate how well our model did. In a real example, we would want
# # to use a separate validation and testing data set to avoid overfitting.
# estimator.evaluate(input_fn=input_fn)


#####
#####
#####
#####


# Declare list of features, we only have one real-valued feature
def model(features, labels, mode):
  # Build a linear model and predict values
  W = tf.get_variable("W", [1], dtype=tf.float64)
  b = tf.get_variable("b", [1], dtype=tf.float64)
  y = W*features['x'] + b
  # Loss sub-graph
  loss = tf.reduce_sum(tf.square(y - labels))
  # Training sub-graph
  global_step = tf.train.get_global_step()
  optimizer = tf.train.GradientDescentOptimizer(0.01)
  train = tf.group(optimizer.minimize(loss),
                   tf.assign_add(global_step, 1))
  # ModelFnOps connects subgraphs we built to the
  # appropriate functionality.
  return tf.contrib.learn.ModelFnOps(
      mode=mode, predictions=y,
      loss=loss,
      train_op=train)

estimator = tf.contrib.learn.Estimator(model_fn=model)
# define our data set
x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x": x}, y, 4, num_epochs=1000)

# train
estimator.fit(input_fn=input_fn, steps=1000)
# evaluate our model
print(estimator.evaluate(input_fn=input_fn, steps=10))
