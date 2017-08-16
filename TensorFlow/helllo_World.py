import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)


# Add

from __future__ import print_function

import tensorflow as tf

with tf.Session():
    input1 = tf.constant([1.0, 1.0, 1.0, 1.0])
    input2 = tf.constant([2.0, 2.0, 2.0, 2.0])
    output = tf.add(input1, input2)
    result = output.eval()
    print("result: ", result)

#  Raw Python
print([x + y for x, y in zip([1.0] * 4, [2.0] * 4)])

# Numpy
import numpy as np
x, y = np.full(4, 1.0), np.full(4, 2.0)
print("{} + {} = {}".format(x, y, x + y))

# Adding two matrices

with tf.Session():
    input1 = tf.constant(1.0, shape=[2, 3])
    input2 = tf.constant(np.reshape(np.arange(1.0, 7.0, dtype=np.float32), (2, 3)))
    output = tf.add(input1, input2)
    print(output.eval())

# Multiplying

with tf.Session():
    input_features = tf.constant(np.reshape([1, 0, 0, 1], (1, 4)).astype(np.float32))
    weights = tf.constant(np.random.randn(4, 2).astype(np.float32))
    output = tf.matmul(input_features, weights)

    print("Input:")
    print(input_features.eval())
    print("Weights:")
    print(weights.eval())
    print("Output:")
    print(output.eval())

# Use of variables
# Let's look at adding two small matrices in a loop, not by creating new tensors every time,' \
#    ' but by updating the existing values and then re-running the computation graph on the new data.' \
#    ' This happens a lot with machine learning models, where we change some parameters each time such as' \
#    ' gradient descent on some weights and then perform the same computations over and over again.

with tf.Session() as sess:
    # Set up two variables, total and weights, that we'll change repeatedly.
    total = tf.Variable(tf.zeros([1, 2]))
    weights = tf.Variable(tf.random_uniform([1, 2]))

    # Initialize the variables we defined above.
    tf.global_variables_initializer().run()

    # This only adds the operators to the graph right now. The assignment
    # and addition operations are not performed yet.
    update_weights = tf.assign(weights, tf.random_uniform([1, 2], -1.0, 1.0))
    update_total = tf.assign(total, tf.add(total, weights))

    for _ in range(5):
        # Actually run the operation graph, so randomly generate weights and then
        # add them into the total. Order does matter here. We need to update
        # the weights before updating the total.
        sess.run(update_weights)
        sess.run(update_total)

        print(weights.eval(), total.eval())