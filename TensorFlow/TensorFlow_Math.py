import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
p = tf.divide(x,y)
z = tf.subtract(p, tf.cast(tf.constant(1), tf.float64))

with tf.Session() as sess:
    output = sess.run(z)
    print(output)
# TODO: Print z from a session
