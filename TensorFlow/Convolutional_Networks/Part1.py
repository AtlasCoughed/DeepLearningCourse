# We have an input of shape 32x32x3 (HxWxD)
# 20 filters of shape 8x8x3 (HxWxD)
# A stride of 2 for both the height and width (S)
# With padding of size 1 (P)
input_height = 32
input_width = 32
filter_height = 8
filter_width = 8

P = 1
S = 2


new_height = ((input_height - filter_height + 2 * P)/S) + 1
new_width = ((input_width - filter_width + 2 * P)/S) + 1

print(new_height, "!!", new_width)

# REAL SOLUTION
input = tf.placeholder(tf.float32, (None, 32, 32, 3))
filter_weights = tf.Variable(tf.truncated_normal((8, 8, 3, 20))) # (height, width, input_depth, output_depth)

filter_bias = tf.Variable(tf.zeros(20))
strides = [1, 2, 2, 1] # (batch, height, width, depth)

padding = 'SAME'

conv = tf.nn.conv2d(input, filter_weights, strides, padding) + filter_bias

###############################################################################
# SAME Padding, the output height and width are computed as:
#
# out_height = ceil(float(in_height) / float(strides[1]))
#
# out_width = ceil(float(in_width) / float(strides[2]))
#
# VALID Padding, the output height and width are computed as:
#
# out_height = ceil(float(in_height - filter_height + 1) / float(strides[1]))
#
# out_width = ceil(float(in_width - filter_width + 1) / float(strides[2]))