import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph


# node maybe for tree
class Node:
    def __init__(self, key):
        pass


class Graph:
    def __init__(self, num_of_nodes: int, directed: bool = True):
        self.size = num_of_nodes
        self.directed = directed
        self.__matrix = [[0 for _ in range(num_of_nodes)] for _ in range(num_of_nodes)]
        self.__G = nx.DiGraph(directed=True)
        self.__dot = Digraph(comment="Graph")

    def __add_edge_graphviz(self, from_node: str, to_node: str, weight: int = 1):
        if ("\t" + from_node + " [label=" + from_node + "]\n") not in self.__dot.body:
            self.__dot.node(name=from_node, label=from_node)
        if ("\t" + to_node + " [label=" + to_node + "]\n") not in self.__dot.body:
            self.__dot.node(name=to_node, label=to_node)
        self.__dot.edge(from_node, to_node, label=weight)

    def add_edge(self, from_node: int, to_node: int, weight: int = 1):
        self.__matrix[from_node][to_node] = weight
        self.__G.add_weighted_edges_from([(from_node, to_node, weight)])
        self.__add_edge_graphviz(str(from_node), str(to_node), str(weight))

        if not self.directed:
            self.__matrix[to_node][from_node] = weight

    def print_adj_matrix(self):
        for each in self.__matrix:
            print(each, end="\n")

    def visualize(self):
        pos = nx.spring_layout(self.__G)
        options_node = {
            'node_color': 'magenta',
            'node_size': 300,
        }
        options_edges = {
            'font_size': 8,
        }
        nx.draw(self.__G, pos, with_labels=True)
        nx.draw_networkx_nodes(self.__G, pos, **options_node)
        nx.draw_networkx_edge_labels(self.__G, pos,
                                     edge_labels={(u, v): d for u, v, d in self.__G.edges(data="weight")},
                                     label_pos=.66, **options_edges)
        plt.show()
        print(self.__dot.source)


graph = Graph(7)
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
