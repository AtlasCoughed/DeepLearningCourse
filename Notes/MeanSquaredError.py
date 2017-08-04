from numpy import *

weights = np.random.normal(scale=1/n_features**.5, size=n_features)

# Numpy provides a function that calculates the dot product of two arrays which conveniently calculates h for us.

# The dot product multoples two arrays element wise, first eleent in array 1 is multiplied by the first element in array2
# Each product is then summed

#output to the outer layer
output_in = np.dot(weights, inputs)

