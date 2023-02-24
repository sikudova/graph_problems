import itertools

import graphviz
import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp
import os
from graphviz import Digraph


class Node:
    index_iter = itertools.count()

    def __init__(self, value):
        self.index = next(Node.index_iter)
        self.value = value


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
        return len(self.adj_matrix().todense())

    def adj_matrix(self):
        return nx.adjacency_matrix(self.G)

    def print_adj_matrix(self) -> None:
        print(self.adj_matrix().todense())

    """
        adding edges and nodes
    """

    def add_node(self, index: int, attr=None):
        if attr is None:
            attr = {}
        self.__G.add_node(index, **attr)
        if ("\t" + str(index) + " [label=" + str(index) + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=str(index), label=str(index))

    def add_edge(self, from_node: int, to_node: int, weight: int = 1):
        self.__G.add_edge(from_node, to_node, weight=weight, color="black")
        self.__add_edge_graphviz(str(from_node), str(to_node), str(weight))

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

    def visualize(self):
        pos = nx.circular_layout(self.__G)
        options_node = {
            'node_color': 'deeppink',
            'node_size': 400,
        }
        options_edges = {
            'font_size': 8,
        }
        colors = [self.G[u][v]['color'] for u, v in self.G.edges()]
        edge_width = [3 if (self.G[u][v]["color"] == "deeppink") else 1 for u, v in self.G.edges()]
        nx.draw(self.__G, pos, with_labels=True, edge_color=colors, width=edge_width, arrows=self.__directed)
        nx.draw_networkx_nodes(self.__G, pos, **options_node)
        if self.__directed:
            nx.draw_networkx_edge_labels(self.__G, pos,
                                         edge_labels={(u, v): d for u, v, d in self.__G.edges(data="weight")},
                                         label_pos=.66, **options_edges)
        else:
            edge_labels = dict([((n1, n2), d['weight']) for n1, n2, d in self.__G.edges(data=True)])
            nx.draw_networkx_edge_labels(self.__G, pos, edge_labels=edge_labels, label_pos=.66)
        plt.show()


graph = Graph(True)
graph.add_edge(0, 1, 10)
graph.add_edge(1, 2, 15)
graph.add_edge(1, 3)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 2)
graph.add_edge(6, 1)
graph.add_edge(6, 4)
graph.print_adj_matrix()
graph.visualize()

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
