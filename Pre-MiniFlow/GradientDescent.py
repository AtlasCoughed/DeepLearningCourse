# Lambda = (y - y^) derivative of activation functions = (y - y^) derivative ( sum ( weight of i * x of i)

# (y - y^) == the output error
# derivative of activation function == output gradient

# We shall be using sigmoid as the activation function.

def sigmoid(x):
    return 1/(1+np.exp(-x))

#Derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

#Input data
x = np.array([0.1, 0.3])
# Target
y = 0.2
# Input to output weights
weights = np.array([0.8, 0.5])

#The learning rate, eta in the weight step equation
learnrate = 0.5

# the linear combination performed by the node (h in f(h) and f'(h))
h = x[0]*weights[0] + x[1]*weights[1]
# or h = np.dot(x, weights)

# The neural network output (y-hat)
nn_output = sigmoid(h)

# Output error(y - y-hat)
error = y - nn_output

# Output gradient (f'(h))
output_grad = sigmoid_prime(h)

# Error_term (lowercase delta)
error_term = error * output_grad

# Gradient descent step
del_w = [learnrate * error_term * x[0], learnrate * error_term * x[1]]

# or del_w = learnrate * error_term * x