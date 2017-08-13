class Node(object):
    def __init__(self, inbound_nodes = []):
        # Inbound node(s) from which this node will receive values.
        self.inbound_nodes = inbound_nodes

        # Outbound node(s) from which this Node will pass values.
        self.outbound_nodes = []

        # For each outbound node, add this Node as an outbound_Node
        # to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)

        # A calculated value.
        self.value = None

    def forward(self):
        """
        Forward Propogation

        Compute the output values based on 'inbound_nodes'Nodes and store the results as self.value
        :return:
        """
        raise NotImplemented

# Nodes that Calculate
# Input class just holds a value, no calculations
class Input(Node):
    def __init__(self):
        # An Input node has no inbound nodes,
        # so no need to pass anything to the Node instantiator.
        Node.__init__(self)

        # NOTE: Input node is the only node where the value
        # may be passed as an argument to forward().
        #
        # All other node implementations should get the value
        # of the previous node from self.inbound_nodes
        #
        # Example:
        # val0 = self.inbound_nodes[0].value
        def forward(self, value=None):
        # Overwrite the value if one is passed in.
            if value is not None:
                self.value = value

class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self, [x, y])

    def forward(self):
        """

        :return:
        """
        x_value = self.inbound_nodes[0].value
        y_value = self.inbound_nodes[1].value
        self.value = x_value + y_value


# Forward Propogation has two methods:  topological_sort() and forward_pass()

# Topological Sort = flattening a graph. Inputs of some nodes rely on the outputs of others.
#       Order of operations.

# Function - topological_sort()
# Use of Kahn's algorithm
#   Returns sorted nodes ready for operations
#   feed_dict => parameter for Input()

x, y = Input(), Input()

add = Add(x, y)

feed_dict = {x: 10, y: 20}

sorted_nodes = topological_sort(feed_dict=feed_dict)

# forward_pass()
# Actually runs the network and outputs a value

def forward_pass(output_node, sorted_nodes):
    """
    Performs a forward pass through a list of sorted nodes.

    Arguments:

        `output_nodes`: The output node of the graph (no outgoing edges).
        `sorted_nodes`: a topologically sorted list of nodes.

    Returns the output node's value
    :param output_node:
    :param sorted_nodes:
    :return:
    """
    for n in sorted_nodes:
        n.forward()

    return output_node.value

"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""

from miniflow import *

x, y = Input(), Input()

f = Add(x, y)

feed_dict = {x: 10, y: 5}

sorted_nodes = topological_sort(feed_dict)
output = forward_pass(f, sorted_nodes)

# NOTE: because topological_sort set the values for the `Input` nodes we could also access
# the value for x with x.value (same goes for y).
print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))
