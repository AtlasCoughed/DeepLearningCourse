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