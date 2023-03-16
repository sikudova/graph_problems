import itertools
import math
from typing import Tuple, List

import graphviz
import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp
import os
from queue import Queue
from graphviz import Digraph

# node labels:
# → https://stackoverflow.com/questions/30791334/making-networkx-plot-where-edges-only-display-edited-numeric-value-not-field-na

# MAGIC VALUES (CONSTANTS)

WHITE = "white"
GREY = "grey"
BLACK = "black"


class Node:
    index_iter = itertools.count()

    def __init__(self, value):
        self.index = next(Node.index_iter)
        self.value = value
        self.visited: bool = False
        self.color = None
        self.distance = None
        self.pi = None
        self.flag = None


class Graph:
    def __init__(self, directed):
        self.__size = 0
        self.__directed = directed
        self.__G = nx.DiGraph() if self.__directed else nx.Graph()
        self.__G_graphviz = Digraph(comment="Graph") if self.__directed else graphviz.Graph(comment="Graph")
        self.__adj_matrix: list[list[int]] = [[0 for _ in range(self.__size)] for _ in range(self.__size)]

    """
        getters, setters (properties), printing methods
    """

    @property
    def G(self) -> nx.Graph:
        return self.__G

    @property
    def G_graphviz(self) -> graphviz.Graph:
        return self.__G_graphviz

    @property
    def directed(self) -> bool:
        return self.__directed

    @property
    def size(self) -> int:
        return len(self.adj_matrix())

    def adj_matrix(self):
        print(self.G.adjacency())
        # print(nx.adjacency_matrix(self.G))
        return (nx.adjacency_matrix(self.G)).todense()

    def print_adj_matrix(self) -> None:
        print(self.adj_matrix())

    """
        neighbours
    """

    def get_neighbours(self, node: Node):
        return self.G.neighbors(node)

    def get_nodes(self):
        return self.G.nodes()

    """
        adding edges and nodes
    """

    def add_node(self, node: Node, attr=None):
        if attr is None:
            attr = {}
        self.__G.add_node(node, **attr)
        if ("\t" + str(node.value) + " [label=" + str(node.value) + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=str(node.value), label=str(node.value))

    def add_edge(self, from_node: Node, to_node: Node, weight: int = 1):
        self.__G.add_edge(from_node, to_node, weight=weight, color="black")
        self.__add_edge_graphviz(str(from_node.value), str(to_node.value), str(weight))

    def __add_edge_graphviz(self, from_node: str, to_node: str, weight: int = 1):
        if ("\t" + from_node + " [label=" + from_node + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=from_node, label=from_node)
        if ("\t" + to_node + " [label=" + to_node + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=to_node, label=to_node)
        self.__G_graphviz.edge(from_node, to_node, label=weight)

    """
        visualizing graph
    """

    def visualize_graphviz(self):
        print(self.__G_graphviz.source)

    def visualize(self, node_colors=None, BFS_tree=False, BFS_edges=None):
        # layout of  the graph
        pos = nx.circular_layout(self.__G)

        # edges settings
        options_edges = {
            "font_size": 8,
        }
        edge_colors = [self.G[u][v]["color"] for u, v in self.G.edges()]
        edge_width = [3 if (self.G[u][v]["color"] == "deeppink") else 1 for u, v in self.G.edges()]

        # node settings
        node_labels = {u: u.value for u in self.G.nodes()}

        if node_colors is None:
            node_colors = ["deeppink" for _ in self.G.nodes()]

        # filter edges
        if BFS_tree:
            edges = BFS_edges
        else:
            edges = self.G.edges()

        nx.draw(self.G, pos, edgelist=edges, labels=node_labels, with_labels=True, edge_color=edge_colors,
                node_color=node_colors, font_color="black", width=edge_width, arrows=self.__directed, node_size=700)

        if self.__directed:
            nx.draw_networkx_edge_labels(self.__G, pos,
                                         edge_labels={(u, v): d for u, v, d in self.__G.edges(data="weight")},
                                         label_pos=.66, **options_edges)
        else:
            edge_labels = dict([((u, v), d["weight"]) for u, v, d in self.__G.edges(data=True)])
            nx.draw_networkx_edge_labels(self.__G, pos, edge_labels=edge_labels, label_pos=.66)
        plt.show()

    def visualize_traverse(self):
        node_colors = "deeppink"

        self.visualize(node_colors)

    def visualize_BFS_tree(self, BFS_edges):
        self.visualize(BFS_tree=True, BFS_edges=BFS_edges)

    """
        BFS -- breadth first search
    """

    def BFS_show_tree(self, BFS_tree: List[Tuple[Node, Node]]):
        """
        Changes the colour of each edge that is in the BFS tree
        (to pink colour, because pink is colour of the year 2023)

        Calls two functions for visualizing traverse of BFS algorithm and resulting BFS tree.

        :param BFS_tree: list of tuples, each tuple contains two nodes that creates edge
        :return: None
        """
        for u, v in BFS_tree:
            data = self.G.get_edge_data(u, v)
            self.G.remove_edge(u, v)
            self.G.add_edge(u, v, color="deeppink", weight=data["weight"])

        self.visualize_traverse()
        self.visualize_BFS_tree(BFS_tree)

    def BFS_basic(self, start: Node, show_tree: bool = False):
        """
        Traverse a graph with breadth first search (BFS) from starting node.
        Sets visited attribute of nodes to True or False.

        :param start: starting node
        :param show_tree: True to visualize and show BFS tree, False otherwise
        :return: BFS tree
        """
        BFS_tree: List[Tuple[Node, Node]] = []

        queue = Queue()
        queue.put(start)
        start.visited = True
        while not queue.empty():
            node = queue.get()
            for each in self.get_neighbours(node):
                if not each.visited:
                    BFS_tree.append((node, each))
                    each.visited = True
                    queue.put(each)

        for u, v in BFS_tree:
            print("{} - {}".format(u.value, v.value))

        if show_tree:
            self.BFS_show_tree(BFS_tree)

        return BFS_tree

    def BFS_attributes(self, start: Node, show_tree: bool = False):
        BFS_tree: List[Tuple[Node, Node]] = []

        # initialize attributes of each vertex
        for each in self.get_nodes():
            print(each.value)
            each.color = WHITE
            each.distance = math.inf
            each.pi = None

        # initialize attributes of starting vertex
        start.color = GREY
        start.distance = 0
        start.pi = None

        # create queue
        queue = Queue()
        queue.put(start)

        while not queue.empty():
            node = queue.get()
            for each in self.get_neighbours(node):
                if each.color == WHITE:
                    BFS_tree.append((node, each))
                    each.color = GREY
                    each.distance = node.distance + 1
                    each.pi = node
                    queue.put(each)
            node.color = BLACK

        for u, v in BFS_tree:
            print("{} - {}".format(u.value, v.value))

        if show_tree:
            self.BFS_show_tree(BFS_tree)

        return BFS_tree


graph = Graph(True)
node_00 = Node("Zlin")
node_01 = Node("Prague")
node_02 = Node("Brno")
node_03 = Node(3)
node_04 = Node(4)
node_05 = Node(5)
node_06 = Node(6)

graph.add_node(node_01)
graph.add_node(node_02)
graph.add_node(node_03)
graph.add_node(node_04)
graph.add_node(node_05)
graph.add_node(node_06)

graph.add_edge(node_00, node_01, 10)
graph.add_edge(node_01, node_02, 15)
graph.add_edge(node_01, node_03)
graph.add_edge(node_02, node_05)
graph.add_edge(node_02, node_06)
graph.add_edge(node_03, node_04)
graph.add_edge(node_04, node_05)
graph.add_edge(node_05, node_02)
graph.add_edge(node_06, node_01)
graph.add_edge(node_06, node_04)
# graph.print_adj_matrix()
graph.visualize()
# print(graph.get_neighbours(node_01))
# print(graph.get_neighbours(node_06))
# print(graph.get_neighbours(node_00))

graph.BFS_basic(node_01, True)
# graph.BFS_attributes(node_01, True)

# graph = Graph(False)
# graph.add_node(1)
# graph.add_node(2)
# graph.add_node(3)
# graph.add_node(4)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(1, 4)
# graph.add_edge(1, 5)
# graph.print_adj_matrix()
# print(graph.size)
# graph.visualize_graphviz()
# graph.visualize()
