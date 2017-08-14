from functools import reduce

class ConstNode(object):
    def __init__(self,layer_index,node_index):
        self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.output = 1
        self.delta = 0

    def append_downstream_connection(self, conn):
        self.downstream.append(conn)

    def calc_hidden_layer_delta(self):
        downstream_delta = (lambda ret, conn: ret + conn.downstream.output * conn.weight, self.downstream, 0)
        self.delta = self.output * (1 - self.output) * downstream_delta

    def __str__(self):
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn, self.downstream, ''))
        return node_str + '\n\tdownstream:' + downstream_str
