import json
import time
import unittest
import networkx
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class CompareNetwork(unittest.TestCase):

    def test_shortest_path(self):

        # G_10_80_1
        self.get_from_json('../data/G_10_80_1.json')
        st = time.time()
        networkx.dijkstra_path_length(self.gx, 0, 5)
        et = time.time()
        print('shortest path(G_10_80_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.shortest_path(0, 5)
        et = time.time()
        print('shortest path(G_10_80_1) - our-plot: ', et - st)

        # G_100_800_1
        self.get_from_json('../data/G_100_800_1.json')
        st = time.time()
        networkx.dijkstra_path_length(self.gx, 1, 5)
        et = time.time()
        print('shortest path(G_100_800_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.shortest_path(1, 5)
        et = time.time()
        print('shortest path(G_100_800_1) - our-plot: ', et - st)

        # G_1000_8000
        self.get_from_json('../data/G_1000_8000_1.json')
        st = time.time()
        networkx.dijkstra_path_length(self.gx, 0, 120)
        et = time.time()
        print('shortest path(G_1000_8000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.shortest_path(0, 120)
        et = time.time()
        print('shortest path(G_1000_8000_1) - our-plot: ', et - st)

        # G_10000_80000
        self.get_from_json('../data/G_10000_80000_1.json')
        st = time.time()
        networkx.dijkstra_path_length(self.gx, 0, 9)
        et = time.time()
        print('shortest path(G_10000_80000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.shortest_path(0, 9)
        et = time.time()
        print('shortest path(G_10000_80000_1) - our-plot: ', et - st)

        # # G_20000_160000
        # self.get_from_json('../data/G_20000_160000_1.json')
        # st = time.time()
        # networkx.dijkstra_path_length(self.gx, 0, 20)
        # et = time.time()
        # print('shortest path(G_20000_160000_1) - networkX: ', et - st)
        # st = time.time()
        # self.graph_algo.shortest_path(0, 20)
        # et = time.time()
        # print('shortest path(G_20000_160000_1) - our-plot: ', et - st)
        #
        # # G_30000_240000
        # self.get_from_json('../data/G_30000_240000_1.json')
        # st = time.time()
        # networkx.dijkstra_path_length(self.gx, 12, 40)
        # et = time.time()
        # print('shortest path(G_30000_240000_1) - networkX: ', et - st)
        # st = time.time()
        # self.graph_algo.shortest_path(12, 40)
        # et = time.time()
        # print('shortest path(G_30000_240000_1) - our-plot: ', et - st)

    def test_connected_component(self):
        # G_10_80_1
        self.get_from_json('../data/G_10_80_1.json')
        st = time.time()
        self.strongly_conn(self.gx, 0)
        et = time.time()
        print('connected component(G_10_80_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_component(5)
        et = time.time()
        print('connected component(G_10_80_1) - our-plot: ', et - st)

        # G_100_800_1
        self.get_from_json('../data/G_100_800_1.json')
        st = time.time()
        self.strongly_conn(self.gx, 0)
        et = time.time()
        print('connected component(G_100_800_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_component(5)
        et = time.time()
        print('connected component(G_100_800_1) - our-plot: ', et - st)

        # G_1000_8000_1
        self.get_from_json('../data/G_1000_8000_1.json')
        st = time.time()
        self.strongly_conn(self.gx, 0)
        et = time.time()
        print('connected component(G_1000_8000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_component(5)
        et = time.time()
        print('connected component(G_1000_8000_1) - our-plot: ', et - st)

        # G_10000_80000_1
        self.get_from_json('../data/G_10000_80000_1.json')
        st = time.time()
        self.strongly_conn(self.gx, 0)
        et = time.time()
        print('connected component(G_10000_80000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_component(5)
        et = time.time()
        print('connected component(G_10000_80000_1) - our-plot: ', et - st)

        # G_20000_160000_1
        self.get_from_json('../data/G_20000_160000_1.json')
        st = time.time()
        self.strongly_conn(self.gx, 0)
        et = time.time()
        print('connected component(G_20000_160000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_component(5)
        et = time.time()
        print('connected component(G_20000_160000_1) - our-plot: ', et - st)

        # G_30000_240000_1
        self.get_from_json('../data/G_30000_240000_1.json')
        st = time.time()
        self.strongly_conn(self.gx, 0)
        et = time.time()
        print('connected component(G_30000_240000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_component(5)
        et = time.time()
        print('connected component(G_30000_240000_1) - our-plot: ', et - st)

    def test_connected_components(self):
        # G_10_80_1
        self.get_from_json('../data/G_10_80_1.json')
        st = time.time()
        networkx.strongly_connected_components
        et = time.time()
        print('connected components(G_10_80_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_components()
        et = time.time()
        print('connected components(G_10_80_1) - our-plot: ', et - st)

        # G_100_800_1
        self.get_from_json('../data/G_100_800_1.json')
        st = time.time()
        networkx.strongly_connected_components
        et = time.time()
        print('connected components(G_100_800_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_components()
        et = time.time()
        print('connected components(G_100_800_1) - our-plot: ', et - st)

        # G_1000_8000_1
        self.get_from_json('../data/G_1000_8000_1.json')
        st = time.time()
        networkx.strongly_connected_components
        et = time.time()
        print('connected components(G_1000_8000_1) - networkX: ', et - st)
        st = time.time()
        self.graph_algo.connected_components()
        et = time.time()
        print('connected components(G_1000_8000_1) - our-plot: ', et - st)

        # # G_10000_80000_1
        # self.get_from_json('../data/G_10000_80000_1.json')
        # st = time.time()
        # networkx.strongly_connected_components
        # et = time.time()
        # print('connected components(G_10000_80000_1) - networkX: ', et - st)
        # st = time.time()
        # self.graph_algo.connected_components()
        # et = time.time()
        # print('connected components(G_10000_80000_1) - our-plot: ', et - st)
        #
        # # G_20000_160000_1
        # self.get_from_json('../data/G_20000_160000_1.json')
        # st = time.time()
        # networkx.strongly_connected_components
        # et = time.time()
        # print('connected components(G_20000_160000_1) - networkX: ', et - st)
        # st = time.time()
        # self.graph_algo.connected_components()
        # et = time.time()
        # print('connected components(G_20000_160000_1) - our-plot: ', et - st)
        #
        # # G_30000_240000_1
        # self.get_from_json('../data/G_30000_240000_1.json')
        # st = time.time()
        # networkx.strongly_connected_components
        # et = time.time()
        # print('connected components(G_30000_240000_1) - networkX: ', et - st)
        # st = time.time()
        # self.graph_algo.connected_components()
        # et = time.time()
        # print('connected components(G_30000_240000_1) - our-plot: ', et - st)

    def nx_from_json(self, data_file_js):
        file_graph = open(data_file_js)
        self.graph = DiGraph()
        json_graph = json.load(file_graph)
        self.gx = networkx.DiGraph()
        vertices = json_graph.get('Nodes')
        edges = json_graph.get('Edges')
        location_w = {}
        for v in vertices:
            key = v.get("id")
            if v.get('pos') is not None:
                pos_arr = str(v.get('pos')).split(",")
                full_pos = (float(pos_arr.__getitem__(0)), float(pos_arr.__getitem__(1)), 0.0)
                location_w[key] = full_pos
                self.gx.add_node(key)
        for e in edges:
            w = e.get('w')
            self.gx.add_edge(e.get('src'), e.get('dest'), weight=w)
        file_graph.close()
        return location_w

    @staticmethod
    def strongly_conn(graph_netx, n1):
        for c_ls in networkx.strongly_connected_components(graph_netx):
            if n1 in c_ls:
                return c_ls
        return set()

    def get_from_json(self, json_file):
        self.nx_from_json(json_file)
        self.graph_algo = GraphAlgo()
        self.graph_algo.load_from_json(json_file)


