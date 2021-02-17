import math

from Cython import typeof

from src.GraphInterface import GraphInterface


class NodeData:

    def __init__(self, key: int = None, edges_out=None, edges_in=None, weight=math.inf, visited: bool = False,
                 pos: tuple = None, tag: int = -1):
        self.visit = False
        if edges_in is None:
            edges_in = {}
        if edges_out is None:
            edges_out = {}
        self.id = key
        self.pos = pos
        self.tag = tag
        self.edges_out = edges_out
        self.edges_in = edges_in
        self.weight = weight
        self.visited = visited

        self.info = True
        if pos is None:
            self.info = False

    def __str__(self):
        return "(" + str(self.id) + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if typeof(self) is typeof(int):
            return self is other
        if typeof(other) is typeof(int):
            return self is other
        return self.id is other.id

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.weight < other.weight


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.vertices = {}
        self.edges = {}
        self.ed_size = 0

    def v_size(self) -> int:
        return len(self.vertices)

    def e_size(self) -> int:
        return self.ed_size

    def get_mc(self) -> int:
        return self.mc

    def get_node(self, id: int) -> NodeData:
        return self.vertices.get(str(id))

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if str(id1) + '->' + str(id2) in self.edges:
            self.ed_size -= 1
        if not (str(id1) in self.vertices and str(id2) in self.vertices):
            return False
        if id1 == id2:
            return False
        self.ed_size += 1
        self.vertices.get(str(id1)).edges_out[str(id2)] = weight
        self.vertices.get(str(id2)).edges_in[str(id1)] = weight
        self.edges[str(id1) + '->' + str(id2)] = weight
        self.mc = self.mc + 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.vertices.get(str(node_id)) is not None:
            return False
        if pos is not None:
            n1 = NodeData(key=node_id, pos=pos)
            self.vertices.update({str(node_id): n1})
            self.mc += 1
        else:
            n1 = NodeData(key=node_id)
            self.vertices.update({str(node_id): n1})
            self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        n1 = self.vertices.get(str(node_id))
        if n1 is None:
            return False
        if n1.edges_out is not None:
            for n2 in n1.edges_out:
                self.vertices.get(n2).edges_in.pop(str(n1))
                self.ed_size -= 1
        if n1.edges_in is not None:
            for n2 in n1.edges_in:
                self.vertices.get(n2).edges_out.pop(str(n1))
                self.ed_size -= 1

        self.vertices.pop(str(node_id))
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        n1 = self.vertices.get(str(node_id1))
        n2 = self.vertices.get(str(node_id2))
        if n1 is None or n2 is None:
            return False
        if n1.edges_out.get(str(n2)) is None:
            return False
        self.edges.pop(node_id1)
        n1.edges_out.pop(str(n2))
        n2.edges_in.pop(str(n1))
        self.ed_size -= 1
        self.mc += 1
        return True

    def __str__(self):
        graph_str = "Graph: Vertices size: {:d} , Edges size: {:d}\n\t".format(self.v_size(), self.e_size())
        graph_str += '   Vertices: '
        for key in self.vertices.keys():
            graph_str += '{} '.format(key)
        graph_str += "\n\t   Edges: "
        for node1 in self.vertices.keys():
            n = self.vertices.get(node1)
            for dict1 in n.edges_out.keys():
                graph_str += str(node1)
                graph_str += '->'
                graph_str += ('{}: {} \t '.format(dict1, n.edges_out[dict1]))
        return graph_str

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return sorted(self.vertices).__eq__(sorted(other.vertices)) and sorted(self.edges).__eq__(sorted(other.edges))

    def get_all_v(self) -> dict:
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for n1 in self.get_all_v().get(str(id1)).edges_in:
            ans.update({int(n1): self.get_all_v().get(str(id1)).edges_in.get(n1)})
        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for n1 in self.get_all_v().get(str(id1)).edges_out:
            ans.update({int(n1): self.get_all_v().get(str(id1)).edges_out.get(n1)})
        return ans
