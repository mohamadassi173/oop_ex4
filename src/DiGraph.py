import math

from src.GraphInterface import GraphInterface


class NodeData:

    def __init__(self, id: int = None, tag: int = -1, weight=math.inf, visited: bool = False, info=None,
                 pos: tuple = None, edges_out=None, edges_in=None):
        self.id = id
        self.tag = tag
        self.weight = weight
        self.visited = visited
        self.info = info
        self.pos = pos
        if edges_out is None:
            edges_out = {}
        if edges_in is None:
            edges_in = {}
        self.edges_out = edges_out
        self.edges_in = edges_in

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "(" + str(self.id) + ")"

    def __eq__(self, other):
        return self.id is other.id

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.weight < other.weight


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.vertices = {}
        self.ed_size = 0

    def v_size(self) -> int:
        return len(self.vertices)

    def e_size(self) -> int:
        return self.ed_size

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (not (id1 in self.vertices)) or (not (id2 in self.vertices)):
            return False

        if id1 == id2:
            return False

        n1 = self.vertices.get(id1)
        n2 = self.vertices.get(id2)

        if n1.edges_out.get(n2) is None:
            self.ed_size += 1
            self.mc += 1

        elif n1.edges_out.get(n2) is not weight:
            self.mc += 1
        elif n1.edges_out.get(n2) == weight:
            return False

        n1.edges_out.update({n2: weight})
        n2.edges_in.update({n1: weight})
        return True

    def get_all_v(self) -> dict:
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.get_all_v().get(id1).edges_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.vertices.get(id1).edges_out

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.vertices.get(node_id) is not None:
            return False
        if pos is not None:
            n1 = NodeData(id=node_id, pos=pos)
            self.vertices.update({node_id: n1})
            self.mc += 1
        else:
            n1 = NodeData(id=node_id)
            self.vertices.update({node_id: n1})
            self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        n1 = self.vertices.get(node_id)
        if n1 is None:
            return False

        if n1.edges_out is not None:
            for n2 in n1.edges_out:
                n2.edges_in.pop(n1)
                self.ed_size -= 1
        if n1.edges_in is not None:
            for n2 in n1.edges_in:
                n2.edges_out.pop(n1)
                self.ed_size -= 1

        self.vertices.pop(node_id)
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        n1 = self.vertices.get(node_id1)
        n2 = self.vertices.get(node_id2)
        if n1 is None or n2 is None:
            return False
        if n1.edges_out.get(n2) is None:
            return False

        n1.edges_out.pop(n2)
        n2.edges_in.pop(n1)
        self.ed_size -= 1
        self.mc += 1
        return True

    def __eq__(self, other):
        sorted(self.vertices)
        sorted(other.vertices)
        return self.vertices.__eq__(other.vertices)

    def __repr__(self):
        return str(self)

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
