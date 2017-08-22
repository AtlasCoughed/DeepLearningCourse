# # Softmax
# Assign a probability to each label
# Then you can classify the data
# Turn the logits into probabilities

# Softmax Function:
# Parameter: input of y values
# By taking e to the power of any real number => positive number
# Helps us scale when we have negative y values
# Add together the e^ (input y value) => calculated proability outputs

# Solution is available in the other "solution.py" tab

import numpy as np


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    return np.exp(x)/ np.sum(np.exp(x), axis=0)

logits = [3.0, 1.0, 0.2]
print(softmax(logits))
# $ [ 0.66524096  0.24472847  0.]