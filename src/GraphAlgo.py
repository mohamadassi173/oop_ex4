import json
import random
from queue import PriorityQueue
from typing import List
import matplotlib.pyplot as plot
from src.DiGraph import DiGraph, NodeData
import math
from src.GraphAlgoInterface import GraphAlgoInterface
from collections import deque
from random import choice

WHITE = -1
GRAY = 1
BLACK = 2
assisGr = {}


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
                edges.append({"src": int(n), "dest": int(dest), "w": self.graph.vertices.get(n).edges_out.get(dest)})

        vertices = []
        for key in self.graph.vertices.keys():
            pos = self.graph.vertices.get(key).pos
            if pos is None:
                vertices.append({"id": key})
            else:
                pos = str(self.graph.vertices.get(key).pos[0]) + ',' + str(
                    self.graph.vertices.get(key).pos[1]) + ',' + str(0.0)
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

        if str(id1) not in self.graph.vertices or str(id2) not in self.graph.vertices:
            return math.inf, []

        copy_graph_vertices = {}
        for n in self.graph.vertices:
            node_temp = NodeData(n)
            copy_graph_vertices[str(n)] = node_temp
        copy_graph_vertices.get(str(id1)).weight = 0
        dijkstra(self, copy_graph_vertices, str(id1), str(id2))
        dest_node = copy_graph_vertices.get(str(id2))  # node data
        shortest_list = []
        if dest_node.weight != math.inf:
            shortest_list.append(int(dest_node.id))
            current_node = dest_node
            while current_node.tag != -1:  # prev node
                current_node = copy_graph_vertices.get(str(current_node.tag))
                shortest_list.append(int(current_node.id))
            shortest_list.reverse()
        return dest_node.weight, shortest_list

    def connected_component(self, id1: int) -> list:
        if self.graph is None:
            return []
        for i in range(0, 9):
            i += 0  # check this later
        if str(id1) not in self.graph.vertices:
            return []
        conn_list = self.bfs(id1)
        for n in self.graph.vertices:
            self.graph.vertices.get(n).tag = -1
        return conn_list

    def reset_colors_tag(self):
        for n in self.graph.vertices:
            n1 = self.graph.vertices.get(n)
            n1.tag = WHITE

    def connected_components(self) -> List[list]:
        assisGr.clear()
        if self.graph is None:
            return []
        conn_list = []
        for i in range(0, 9):
            i += 0  # check this later
        for i in self.graph.vertices:
            if i not in assisGr:
                conn_list.append(self.connected_component(i))
        return conn_list

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
            for dest in self.graph.vertices.get(str(src)).edges_out:
                source = self.graph.vertices.get(src)
                dest_node = dest
                pos = self.graph.vertices.get(dest_node).pos
                dest_pos = (pos[0], pos[1])
                pos = self.graph.vertices.get(src).pos
                source_pos = (pos[0], pos[1])
                plot.annotate(text="", xy=dest_pos, xytext=source_pos, arrowprops=dict(arrowstyle="->"))

        plot.show()

    def bfs(self, id1: int):
        conn_list = []
        curr_node_id = self.graph.vertices.get(str(id1))
        dequeue = deque()
        curr_node_id.tag = BLACK
        conn_list.append(curr_node_id)
        assisGr[str(id1)] = id1
        for n in curr_node_id.edges_out:
            node_data = self.graph.vertices.get(n)
            node_data.tag = GRAY
            dequeue.append(node_data)
        while dequeue:
            n = dequeue.popleft()
            for x in n.edges_out:
                temp2 = self.graph.vertices.get(x)
                if temp2.tag == WHITE:
                    temp2.tag = GRAY
                    dequeue.append(temp2)
        for n in curr_node_id.edges_in:
            node_data = self.graph.vertices.get(n)
            if node_data.tag == GRAY:
                dequeue.append(node_data)
        while dequeue:
            n = dequeue.popleft()
            if n.tag == GRAY:
                n.tag = BLACK
                conn_list.append(n)
                assisGr[str(n.id)] = n.id
                for x in n.edges_in:
                    temp2 = self.graph.vertices.get(x)
                    dequeue.append(temp2)
        return conn_list


def fill_conn_list(self, dequeue, source_node):
    connected_comp_list = [source_node]
    while dequeue:
        n = dequeue.popleft()
        if n.tag == GRAY:
            n.tag = BLACK
            connected_comp_list.append(n)

            for ni in n.edges_in:
                dequeue.append(self.graph.vertices.get(ni))
    return connected_comp_list


def dijkstra(self, vertex, id1, id2):
    min_heap = PriorityQueue()
    flag = True
    min_heap.put(vertex.get(str(id1)))
    while not min_heap.empty() and flag:
        current = min_heap.get()
        if current.visited is False:
            node = self.graph.vertices.get(current.id)
            for n in node.edges_out:  # n = node_data
                node_ni = vertex.get(n)  # node_data
                if node_ni.visited is False:
                    w = current.weight + self.graph.vertices.get(str(current.id)).edges_out.get(n)  # double
                    if node_ni.weight > w:
                        node_ni.weight = w
                        node_ni.tag = current.id  # tag = prev -  parent
                min_heap.put(node_ni)
            current.visited = True
            if current.id == id2:
                flag = False
