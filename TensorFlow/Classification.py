# Linear Function

# y = Wx + b
#
# x  = list of pixel values
# y = logits, one for each digit
# W = weights

# Numpy
import numpy as np

W = np.array([[-0.5, 0.2, 0.1], [0.7, 0.8, 0.2]])
tempX = np.array([[0.2], [0.5], [0.6]])
tempB = np.array([[0.1], [0.2]])

x = tempX
b = tempB

first = np.dot(W, x)
print(np.add(first, b))

# Weights and bias in TensorFlow
# The goal of training is to modify weights/biases to best predict the labels
#
# tf.Variable class creates a tensor witha n inital value that can modified
#
# This tensor stores the state in the sessiona nd you must initialize this tensor manually

init = tf.glocal_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

# Best practices:
# Initializing with a random number
# Choosing weights from a normal distribution

n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))

# Returns a tensor with random values from a normal distribution whose magnitude is no more than 2 standard deviations from the mean

n_labels = 5
bias = tf.Variable(tf.zeros(n_labels))

# Will return a tensor with all zeros