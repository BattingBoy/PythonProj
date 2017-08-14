from functools import reduce
import numpy

class Node(object):
    def __init__(self, layer_index, node_index):
        '''
        :param layer_index: 节点所属层的编号
        :param node_index: 节点的编号
        '''
        self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.upstream = []
        self.output = 0
        self.delta = 0

    def set_output(self, output):
        self.output = output

    def append_downstream_connection(self, conn):
        self.downstream.append(conn)

    def append_upstream_connection(self, conn):
        self.upstream.append(conn)

    def calc_output(self):
        output = reduce(lambda ret, conn: ret + conn.upstream_node.output * conn.weight, self.upstream, 0)
        self.output = self.sigmoid(output)

    def calc_hidden_layer_delta(self):
        downstream_delta = reduce(lambda ret, conn: ret + conn.upstream_node.output * conn.weight, self.downstream, 0)
        self.delta = self.output * (1 - self.output) * downstream_delta

    def calc_output_layer_delta(self, label):
        self.delta = self.output * (1 - self.output) * (label - self.output)

    def __str__(self):
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn, self.downstream, ''))
        upstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn, self.upstream, ''))
        return node_str + '\n\tdownstream:' + downstream_str + '\nupsteam:' + upstream_str

    def sigmoid(self,x):
        return 1 / (1 + numpy.exp(-x))