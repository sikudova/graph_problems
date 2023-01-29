import itertools
import matplotlib.pyplot as plt
import networkx as nx
import os
from graphviz import Digraph


class Node:
    index_iter = itertools.count()

    def __init__(self, value):
        self.index = next(Node.index_iter)
        self.value = value


class Graph:
    def __init__(self, directed):
        self.directed = directed
        self.__G = nx.DiGraph() if self.directed else nx.Graph()
        self.__G_graphviz = Digraph(comment="Graph")

    @property
    def G(self) -> nx.Graph:
        return self.__G

    def adj_matrix(self):
        return self.__G.adjacency()

    def print_adj_matrix(self) -> None:
        print(self.__G.adjacency())

    def add_edge(self, from_node: Node, to_node: Node, weight: int = 1):
        self.__G.add_edge(from_node.index, to_node.index, weight=weight, color="black")
        self.__add_edge_graphviz(str(from_node.index), str(to_node.index), str(weight))

    def __add_edge_graphviz(self, from_node: str, to_node: str, weight: int = 1):
        if ("\t" + from_node + " [label=" + from_node + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=from_node, label=from_node)
        if ("\t" + to_node + " [label=" + to_node + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=to_node, label=to_node)
        self.__G_graphviz.edge(from_node, to_node, label=weight)
