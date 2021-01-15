import math
import unittest
from unittest import TestCase

from op_ex4.src.DiGraph import DiGraph
from op_ex4.src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    # save load from json function test
    def test_save_load_json(self):
        algo = GraphAlgo()
        graph = graph_creator()
        self.assertEqual(False, algo.save_to_json("saved_graph"))
        algo.__init__(graph)
        self.assertEqual(True, algo.save_to_json("saved_graph"))
        self.assertEqual(True, algo.load_from_json("saved_graph"))
        self.assertEqual(graph, algo.get_graph())

    # shortest path function test
    def test_shortest_path(self):
        algo = GraphAlgo()
        graph = graph_creator()
        algo.__init__(graph)
        self.assertEqual((2.5, [0, 1, 2, 3]), algo.shortest_path(0, 3))
        self.assertEqual((math.inf, []), algo.shortest_path(2, 10))
        graph.remove_edge(1, 3)
        self.assertEqual((math.inf, []), algo.shortest_path(0, 11))
        self.assertEqual((0, [4]), algo.shortest_path(4, 4))

    # connected component function test
    def test_connected_component(self):
        algo = GraphAlgo()
        graph = graph_creator()
        algo.__init__(graph)
        # conn_list - excepted list
        conn_list = [graph.vertices.get(0), graph.vertices.get(1)]
        self.assertEqual(conn_list, algo.connected_component(0))
        graph.add_edge(2, 1, 0.5)
        self.assertEqual(algo.connected_component(2), algo.connected_component(1))

    # connected components function test
    def test_connected_components(self):
        algo = GraphAlgo()
        graph = graph_creator()
        algo.__init__(graph)
        # conn_list - excepted list
        conn_list = [[graph.vertices.get(0), graph.vertices.get(1)], algo.connected_component(2),
                     [graph.vertices.get(3)], [graph.vertices.get(4)], [graph.vertices.get(5)], [graph.vertices.get(6)],
                     [graph.vertices.get(7)], [graph.vertices.get(8)], [graph.vertices.get(9)]]
        self.assertEqual(conn_list, algo.connected_components())


# build graph private function..
def graph_creator():
    tester_graph: DiGraph = DiGraph()
    for i in range(10):
        tester_graph.add_node(i)
    tester_graph.add_edge(0, 1, 0.5)
    tester_graph.add_edge(1, 2, 1.7)
    tester_graph.add_edge(2, 3, 0.3)
    tester_graph.add_edge(0, 3, 7.8)
    tester_graph.add_edge(5, 1, 9.8)
    tester_graph.add_edge(4, 2, 12.1)
    tester_graph.add_edge(0, 6, 3.7)
    tester_graph.add_edge(5, 6, 4.7)
    tester_graph.add_edge(2, 8, 1.7)
    tester_graph.add_edge(1, 0, 1.7)
    return tester_graph
