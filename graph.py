import itertools
import matplotlib.pyplot as plt
import networkx as nx
import os
from graphviz import Digraph


# node maybe for tree
class Node:
    def __init__(self, key):
        pass


def save_graph(dir_name: str, file_name: str) -> None:
    path = os.path.join(fr'hamiltonian_paths_graphs\{dir_name}', file_name)
    plt.savefig(path)
    plt.show()


class Graph:
    def __init__(self, num_of_nodes: int, directed: bool = True):
        self.directed = directed
        self.__ham_paths = None
        self.__size = num_of_nodes
        self.__matrix: list[list[int]] = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        self.__G = nx.DiGraph(directed=directed)
        self.__G_graphviz = Digraph(comment="Graph")

    @property
    def size(self) -> int:
        return self.__size

    @property
    def matrix(self) -> list[list[int]]:
        return self.__matrix

    @property
    def G(self) -> nx.DiGraph:
        return self.__G

    @property
    def ham_paths(self):
        return self.__ham_paths

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
            self.__G.add_edge(to_node, from_node, weight=weight, color="black")
            self.__add_edge_graphviz(str(to_node), str(from_node), str(weight))

    def print_adj_matrix(self) -> None:
        print(self.__G.adjacency())
        # for each in self.__matrix:
        #     print(each, end="\n")

    def get_neighbours(self, node: int) -> list[int]:
        neighbours = []
        for i in range(self.__size):
            # if self.matrix[node][i]:
            if self.__G.adjacency()[node][i]:
                neighbours.append(i)
        return neighbours

    def visualize(self):
        # pos = nx.spring_layout(self.__G)
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
        nx.draw(self.__G, pos, with_labels=True, edge_color=colors, width=edge_width, arrows=self.directed)
        nx.draw_networkx_nodes(self.__G, pos, **options_node)
        if self.directed:
            nx.draw_networkx_edge_labels(self.__G, pos,
                                         edge_labels={(u, v): d for u, v, d in self.__G.edges(data="weight")},
                                         label_pos=.66, **options_edges)
        else:
            edge_labels = dict([((n1, n2), d['weight']) for n1, n2, d in self.__G.edges(data=True)])
            nx.draw_networkx_edge_labels(self.__G, pos, edge_labels=edge_labels, label_pos=.66)
        # print(self.__G_graphviz.source)
        plt.show()

    def hamiltonian_path_DFS(self):
        self.__ham_paths = 0
        for i in range(self.size):
            visited = [False for _ in range(graph.size)]
            visited[i] = True
            graph.__hamiltonian_path_DFS_rec(i, visited, [i])

    def __hamiltonian_path_DFS_rec(self, node: int, visited: list[bool], path: list[int]):
        if len(path) == self.size:
            if self.__ham_paths is None:
                self.__ham_paths = 1
            else:
                self.__ham_paths += 1
            print("Hamiltonian path found: " + str(path))
            self.visualize()
            save_graph("DFS", "graph_" + str(self.__ham_paths))

            return

        print("neighbours of {}: {}".format(node, self.get_neighbours(node)))
        for each in self.get_neighbours(node):
            if not visited[each]:
                visited[each] = True
                path.append(each)
                data = self.G.get_edge_data(node, each)
                self.G.remove_edge(node, each)
                self.G.add_edge(node, each, color='deeppink', weight=data["weight"])

                self.__hamiltonian_path_DFS_rec(each, visited, path)

                visited[each] = False
                path.pop()
                data = self.G.get_edge_data(node, each)
                self.G.remove_edge(node, each)
                self.G.add_edge(node, each, color='black', weight=data["weight"])

    def __show_hamiltonian_path(self, ham_path):
        for i in range(len(ham_path) - 1):
            data = self.G.get_edge_data(ham_path[i], ham_path[i + 1])
            self.G.remove_edge(ham_path[i], ham_path[i + 1])
            self.G.add_edge(ham_path[i], ham_path[i + 1], color='deeppink', weight=data["weight"])

        self.visualize()
        save_graph("brute_force", "graph_" + str(self.__ham_paths))

        for i in range(len(ham_path) - 1):
            data = self.G.get_edge_data(ham_path[i], ham_path[i + 1])
            self.G.remove_edge(ham_path[i], ham_path[i + 1])
            self.G.add_edge(ham_path[i], ham_path[i + 1], color='black', weight=data["weight"])

    def hamiltonian_path_brute_force(self):
        self.__ham_paths = 0
        permutations = itertools.permutations([_ for _ in range(self.size)])
        hamiltonian_paths = []
        for path in permutations:
            valid_path = True
            for i in range(len(path) - 1):
                if self.matrix[path[i]][path[i + 1]] == 0:
                    # print("end of connection")
                    valid_path = False
                    break
            if valid_path:
                # print("hamiltonian path: " + str(path))
                hamiltonian_paths.append(path)
                if self.__ham_paths is None:
                    self.__ham_paths = 1
                else:
                    self.__ham_paths += 1
                self.__show_hamiltonian_path(path)
        print("all hamiltonian paths")
        print("number of paths: " + str(len(hamiltonian_paths)))
        for each in hamiltonian_paths:
            print("hamiltonian path: " + str(each), end="\n")


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


graph = Graph(4, False)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 2)
graph.add_edge(3, 3)
graph.print_adj_matrix()
graph.visualize()
graph.hamiltonian_path_brute_force()
# graph.hamiltonian_path_DFS()

# graph = Graph(7, True)
# graph.add_edge(0, 1)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(2, 4)
# graph.add_edge(2, 5)
# graph.add_edge(2, 6)
# graph.add_edge(3, 2)
# graph.add_edge(3, 4)
# graph.add_edge(4, 5)
# graph.add_edge(5, 2)
# graph.add_edge(5, 6)
# graph.add_edge(6, 0, 10)
# graph.visualize()

# graph.hamiltonian_path_DFS()
# graph.hamiltonian_path_brute_force()

# visited = [False for _ in range(graph.size)]
# visited[0] = True
# graph.hamiltonian_path_DFS(0, visited, [0])
# visited = [False for _ in range(graph.size)]
# visited[1] = True
# graph.hamiltonian_path_DFS(1, visited, [1])
# visited = [False for _ in range(graph.size)]
# visited[2] = True
# graph.hamiltonian_path_DFS(2, visited, [2])
# visited = [False for _ in range(graph.size)]
# visited[3] = True
# graph.hamiltonian_path_DFS(3, visited, [3])
# visited = [False for _ in range(graph.size)]
# visited[4] = True
# graph.hamiltonian_path_DFS(4, visited, [4])
# visited = [False for _ in range(graph.size)]
# visited[5] = True
# graph.hamiltonian_path_DFS(5, visited, [5])
# visited = [False for _ in range(graph.size)]
# visited[6] = True
# graph.hamiltonian_path_DFS(6, visited, [6])
# graph.hamiltonian_path_brute_force()
# for each in graph.matrix:
#     print(each, end="\n")
