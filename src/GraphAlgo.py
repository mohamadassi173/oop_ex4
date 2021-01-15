import json
import heapq
import random
from typing import List
import math
from collections import deque
from random import choice, seed
import matplotlib.pyplot as plot

from src.DiGraph import NodeData
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface

WHITE = 0
GRAY = 1
BLACK = 2

""" 
    @author Mohamad assi, Oday Mahamid
    
"""


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> DiGraph:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            file_graph = open(file_name)
            ver_size = 0
            self.graph = DiGraph()
            json_graph = json.load(file_graph)
            vertices = json_graph.get('Nodes')
            edges = json_graph.get('Edges')

            for v in vertices:
                key = v.get("id")
                if v.get('pos') is None:
                    ver_size += 1
                    self.graph.add_node(node_id=key)
                else:
                    pos_arr = str(v.get('pos')).split(",")
                    full_pos = (float(pos_arr.__getitem__(0)), float(pos_arr.__getitem__(1)), 0.0)
                    ver_size += 1
                    self.graph.add_node(node_id=key, pos=full_pos)

            for e in edges:
                w = e.get('w')
                self.graph.add_edge(e.get('src'), e.get('dest'), w)
                file_graph.close()
        except FileExistsError:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        if self.graph is None:
            return False

        edges = []
        for n in self.graph.vertices:
            for dest in self.graph.vertices.get(n).edges_out:
                edges.append({"src": int(n), "dest": int(dest.id), "w": self.graph.vertices.get(n).edges_out.get(dest)})

        vertices = []
        for key in self.graph.vertices.keys():
            pos = self.graph.vertices.get(key).pos
            if pos is None:
                vertices.append({"id": key})
            else:
                pos = str(self.graph.vertices.get(key).pos[0]) + ',' + str(self.graph.vertices.get(key).pos[1]) + ',' + str(0.0)
                vertices.append({"pos": pos, "id": key})

        saved_graph = {"Nodes": vertices, "Edges": edges}

        with open(file_name, 'w') as json_file:
            json.dump(saved_graph, json_file)

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            return 0, [id1]

        if self.graph is None:
            return math.inf, []

        if id1 not in self.graph.vertices or id2 not in self.graph.vertices:
            return math.inf, []

        copy_graph_vertices = {}
        for n in self.graph.vertices:
            node_temp = NodeData(n)
            copy_graph_vertices[n] = node_temp

        copy_graph_vertices.get(id1).weight = 0
        dijkstra(self, copy_graph_vertices, id1, id2)

        dest_node = copy_graph_vertices.get(id2)  # node data

        shortest_list = []
        if dest_node.weight != math.inf:
            shortest_list.append(dest_node.id)
            current_node = dest_node
            while current_node.tag != -1:  # prev node
                current_node = copy_graph_vertices.get(current_node.tag)
                shortest_list.append(current_node.id)
            shortest_list.reverse()
        return dest_node.weight, shortest_list

    def connected_component(self, id1: int) -> list:
        if id1 not in self.graph.vertices:
            return []

        if self.graph is None:
            return []
        reset_colors_tag(self)

        return sorted(set(self.bfs(id1)))

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []

        conn_list = []
        conn_ans = []

        for n in self.graph.vertices:
            conn_list.append(self.connected_component(n))

        for n1 in conn_list:  # sort and remove duplicated lists
            if n1 not in conn_ans:
                conn_ans.append(n1)

        return conn_ans

    def plot_graph(self) -> None:
        x_pos_list = []
        y_pos_list = []

        if self.graph is None:
            return

        # graph title
        plot.title("Graph GUI")

        random.seed(1)
        curr_range = [i for i in range(2 * self.graph.v_size())]
        # paint the vertices
        for n in self.graph.vertices:
            pos = self.graph.vertices.get(n).pos
            if pos is None:
                x = choice(curr_range)
                curr_range.remove(x)
                y = choice(curr_range)
                curr_range.remove(y)
                self.graph.vertices.get(n).pos = (x, y)
                pos = self.graph.vertices.get(n).pos
            x_pos_list.append(pos[0])
            y_pos_list.append(pos[1])

            label = "{:}".format(int(n))
            plot.annotate(label, (pos[0], pos[1]), textcoords="offset points", xytext=(-1, 3), ha='center',
                          color='green')

        plot.plot(x_pos_list, y_pos_list, 'o', color='blue')

        # draw the edges
        for src in self.graph.vertices:
            for dest in self.graph.vertices.get(src).edges_out:
                source = self.graph.vertices.get(src)
                dest_node = dest
                pos = self.graph.vertices.get(dest_node.id).pos
                dest_pos = (pos[0], pos[1])
                pos = self.graph.vertices.get(source.id).pos
                source_pos = (pos[0], pos[1])
                plot.annotate(text="", xy=dest_pos, xytext=source_pos, arrowprops=dict(arrowstyle="->"))

        plot.show()

    def bfs(self, id1: int) -> (list, dict):
        source_node = self.graph.vertices.get(id1)

        dequeue = deque()

        dequeue.append(source_node)
        while dequeue:
            n = dequeue.popleft()
            for ni in n.edges_out:
                node_ni = self.graph.vertices.get(ni.id)
                if node_ni.tag == WHITE:
                    node_ni.tag = GRAY
                    dequeue.append(node_ni)
        source_node.tag = BLACK

        for n in source_node.edges_in:
            node_ni = self.graph.vertices.get(n.id)
            if node_ni.tag == GRAY:
                dequeue.append(node_ni)

        return fill_conn_list(self, dequeue, source_node)


def fill_conn_list(self, dequeue, source_node):
    connected_comp_list = [source_node]
    while dequeue:
        n = dequeue.popleft()
        if n.tag == GRAY:
            n.tag = BLACK
            connected_comp_list.append(n)

            for ni in n.edges_in:
                dequeue.append(self.graph.vertices.get(ni.id))
    return connected_comp_list


def dijkstra(self, vertex, id1, id2):
    min_heap = []
    heapq.heappush(min_heap, vertex.get(id1))
    flag = True
    while min_heap and flag:
        heapq.heapify(min_heap)
        current = heapq.heappop(min_heap)
        if current.visited is False:
            node = self.graph.vertices.get(current.id)
            for n in node.edges_out:  # n = node_data
                node_ni = vertex.get(n.id)  # node_data
                if node_ni.visited is False:
                    w = current.weight + self.graph.vertices.get(current.id).edges_out.get(n)  # double
                    if node_ni.weight > w:
                        node_ni.weight = w
                        node_ni.tag = current.id  # tag = prev -  parent
                heapq.heappush(min_heap, node_ni)
            current.visited = True
            if current.id == id2:
                flag = False


def reset_colors_tag(self):
    for n in self.graph.vertices:
        n1 = self.graph.vertices.get(n)
        n1.tag = WHITE
