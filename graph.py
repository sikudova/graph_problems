import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph


# node maybe for tree
class Node:
    def __init__(self, key):
        pass


class Graph:
    def __init__(self, num_of_nodes: int, directed: bool = True):
        self.__size = num_of_nodes
        self.directed = directed
        self.__matrix = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        self.__G = nx.DiGraph(directed=True)
        self.__G_graphviz = Digraph(comment="Graph")

    @property
    def size(self):
        return self.__size

    @property
    def matrix(self):
        return self.__matrix

    @property
    def G(self):
        return self.__G

    def __add_edge_graphviz(self, from_node: str, to_node: str, weight: int = 1):
        if ("\t" + from_node + " [label=" + from_node + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=from_node, label=from_node)
        if ("\t" + to_node + " [label=" + to_node + "]\n") not in self.__G_graphviz.body:
            self.__G_graphviz.node(name=to_node, label=to_node)
        self.__G_graphviz.edge(from_node, to_node, label=weight)

    def add_edge(self, from_node: int, to_node: int, weight: int = 1) -> None:
        self.__matrix[from_node][to_node] = weight
        self.__G.add_edge(from_node, to_node, weight=weight, color="black")
        # self.__G.add_weighted_edges_from([(from_node, to_node, weight)])
        self.__add_edge_graphviz(str(from_node), str(to_node), str(weight))

        if not self.directed:
            self.__matrix[to_node][from_node] = weight

    def print_adj_matrix(self) -> None:
        for each in self.__matrix:
            print(each, end="\n")

    def get_neighbours(self, node: int) -> list[int]:
        neighbours = []
        for i in range(self.__size):
            if self.matrix[node][i]:
                neighbours.append(i)
        return neighbours

    def visualize(self):
        # pos = nx.spring_layout(self.__G)
        pos = nx.circular_layout(self.__G)
        options_node = {
            'node_color': 'deeppink',
            'node_size': 300,
        }
        options_edges = {
            'font_size': 8,
        }
        colors = [self.G[u][v]['color'] for u, v in self.G.edges()]
        nx.draw(self.__G, pos, with_labels=True, edge_color=colors)
        nx.draw_networkx_nodes(self.__G, pos, **options_node)
        nx.draw_networkx_edge_labels(self.__G, pos,
                                     edge_labels={(u, v): d for u, v, d in self.__G.edges(data="weight")},
                                     label_pos=.66, **options_edges)
        plt.show()
        print(self.__G_graphviz.source)

    def hamiltonian_path(self, node: int, visited: list[bool], path: list[int]):
        if len(path) == self.size:
            print("Hamiltonian path found: " + str(path))
            self.visualize()
            return

        print("neighbours of {}: {}".format(node, self.get_neighbours(node)))
        for each in self.get_neighbours(node):
            if visited[each]:
                print("node {} already visited".format(each))
            elif not visited[each]:
                visited[each] = True
                path.append(each)
                self.G.remove_edge(node, each)
                self.G.add_edge(node, each, color='deeppink')
                # self.__dot.edge(str(node), str(each), color="red")
                self.hamiltonian_path(each, visited, path)

                visited[each] = False
                path.pop()
                self.G.remove_edge(node, each)
                self.G.add_edge(node, each, color='black')
                # self.__dot.edge(str(node), str(each), color="black")


# graph = Graph(7)
# graph.add_edge(0, 1, 10)
# graph.add_edge(1, 2, 15)
# graph.add_edge(1, 3)
# graph.add_edge(2, 5)
# graph.add_edge(2, 6)
# graph.add_edge(3, 4)
# graph.add_edge(4, 5)
# graph.add_edge(5, 2)
# graph.add_edge(6, 1)
# graph.add_edge(6, 4)
# graph.print_adj_matrix()
# graph.visualize()


graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 2)
graph.add_edge(5, 6)
graph.add_edge(6, 0)
graph.visualize()
visited = [False for _ in range(graph.size)]
visited[0] = True
graph.hamiltonian_path(0, visited, [0])
