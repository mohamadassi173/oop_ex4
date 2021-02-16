import unittest

from src.DiGraph import DiGraph

tester_graph = DiGraph()


"""
test all di graph class functions - add_node, remove_node, remove_edge, mc, ver_size, edges_size
"""


class TestDiGraph(unittest.TestCase):

    # add node test
    def test_add_node(self):
        tester_graph = graph_creator()
        self.assertEqual(False, tester_graph.add_node(0))
        self.assertEqual(True, tester_graph.add_node(13))
        self.assertEqual(False, tester_graph.add_node(4))

    # add edge test
    def test_add_edge(self):
        tester_graph = graph_creator()
        self.assertEqual(True, tester_graph.add_edge(4, 0, 1))
        self.assertEqual(True, tester_graph.add_edge(0, 1, 2.5))
        self.assertEqual(True, tester_graph.add_edge(2, 8, 1.7))
        self.assertEqual(False, tester_graph.add_edge(10, 16, 1))
        self.assertEqual(True, tester_graph.add_edge(5, 6, 4.2))

    # test vertices and edges size using add and remove functions
    def test_ver_edge_size(self):
        tester_graph = graph_creator()
        self.assertEqual(10, tester_graph.v_size())
        tester_graph.add_node(11)
        self.assertEqual(11, tester_graph.v_size())
        tester_graph.add_node(10)
        self.assertEqual(12, tester_graph.v_size())
        self.assertEqual(12, tester_graph.v_size())
        tester_graph.remove_edge(0, 6)
        self.assertEqual(12, tester_graph.v_size())
        #  edges size test
        tester_graph = graph_creator()
        self.assertEqual(9, tester_graph.e_size())
        tester_graph.add_edge(10, 0, 0.2)
        self.assertEqual(9, tester_graph.e_size())
        tester_graph.add_edge(1, 0, 11)
        self.assertEqual(10, tester_graph.e_size())
        tester_graph.add_edge(5, 6, 1.8)
        self.assertEqual(10, tester_graph.e_size())
        tester_graph.remove_edge(2, 3)
        self.assertEqual(10, tester_graph.e_size())

    # mc test !!
    def test_mc(self):
        tester_graph = graph_creator()
        self.assertEqual(19, tester_graph.get_mc())
        tester_graph.add_node(0)
        self.assertEqual(19, tester_graph.get_mc())
        tester_graph.add_node(12)
        self.assertEqual(20, tester_graph.get_mc())


# build graph private function..
def graph_creator():
    tester_graph: DiGraph = DiGraph()
    for i in range(10):
        tester_graph.add_node(i)
    tester_graph.add_edge(0, 1, 2.5)
    tester_graph.add_edge(1, 2, 1.7)
    tester_graph.add_edge(2, 3, 0.3)
    tester_graph.add_edge(3, 2, 7.8)
    tester_graph.add_edge(5, 1, 9.8)
    tester_graph.add_edge(4, 2, 12.1)
    tester_graph.add_edge(0, 6, 3.7)
    tester_graph.add_edge(5, 6, 4.7)
    tester_graph.add_edge(2, 8, 1.7)
    return tester_graph