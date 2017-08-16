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