import itertools
import math
from typing import Tuple, List

import graphviz
import heapq as hq
import matplotlib.pyplot as plt
import networkx as nx
import scipy as sp
import os
from queue import Queue, LifoQueue
from graphviz import Digraph

# node labels:
# → https://stackoverflow.com/questions/30791334/making-networkx-plot-where-edges-only-display-edited-numeric-value-not-field-na

# MAGIC VALUES (CONSTANTS)

WHITE = "white"
GREY = "grey"
BLACK = "black"
NODES_IN_GRAPH = 25


class Node:
    iterator = [_ for _ in range(NODES_IN_GRAPH)]
    index_iter = itertools.cycle(iterator)

    def __init__(self, value):
        self.index = next(Node.index_iter)
        self.value = value
        self.visited: bool = False
        self.color = None
        self.distance = None
        self.pi = None
        self.discovery_time = None
        self.finishing_time = None
        self.flag = None

    def __lt__(self, other):
        return self.distance < other.distance

    def initialize_values(self):
        self.visited = False
        self.color = None
        self.distance = None
        self.pi = None
        self.discovery_time = None
        self.finishing_time = None
        self.flag = None


def relax_edge(from_node, to_node, value, tree):
    to_node.distance = value
    to_node.pi = from_node
    for s, t in tree:
        if t == to_node:
            tree.remove((s, t))
    tree.append((from_node, to_node))


class Graph:
    def __init__(self, directed):
        self.__size = 0
        self.__directed = directed
        self.__G = nx.DiGraph() if self.__directed else nx.Graph()
        self.__G_graphviz = Digraph(comment="Graph") if self.__directed else graphviz.Graph(comment="Graph")
        self.__adj_matrix: list[list[int]] = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        self.__DFS_step = 0
        self.__ham_paths = 0

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

    def get_edges(self):
        return self.G.edges()

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
        initialize node values
    """

    def initialize_node_values(self):
        for each in self.get_nodes():
            each.initialize_values()

    """
        visualizing graph
    """

    def visualize_graphviz(self) -> None:
        print(self.__G_graphviz.source)

    def visualize(self, node_colors=None, traverse_tree=False, traverse_edges=None, title: str = "Graph") -> None:
        # layout of the graph
        pos = nx.circular_layout(self.__G)
        # pos = nx.tight_layout(self.__G)

        plt.title(title)

        # filter edges
        if traverse_tree:
            edges = traverse_edges
        else:
            edges = self.G.edges()

        # edges settings
        options_edges = {
            "font_size": 8,
        }
        edge_colors = [self.G[u][v]["color"] for u, v in edges]
        edge_width = [3 if (self.G[u][v]["color"] == "deeppink") else 1 for u, v in edges]

        # node settings
        node_labels = {u: (u.value, u.distance) if u.distance else u.value for u in self.G.nodes()}

        if node_colors is None:
            # node_colors = ["deeppink" if u.visited else "white" for u in self.G.nodes()]
            node_colors = ["white" for u in self.G.nodes()]

        # draw
        nx.draw(self.G, pos, edgelist=edges, labels=node_labels, with_labels=True, edge_color=edge_colors,
                node_color=node_colors, edgecolors='black', font_color="black", width=edge_width,
                arrows=self.__directed, node_size=700)

        if self.__directed:
            nx.draw_networkx_edge_labels(self.__G, pos,
                                         edge_labels={(u, v): d if (u, v) in edges else "" for u, v, d in
                                                      self.__G.edges(data="weight")}, label_pos=.66, **options_edges)
        else:
            edge_labels = {
                (u, v): d if (u, v) in edges else "" for u, v, d in self.__G.edges(data="weight")}
            nx.draw_networkx_edge_labels(self.__G, pos, edge_labels=edge_labels, label_pos=.66)

        plt.tight_layout()
        plt.show()

    def get_node_colors_based_on_alg(self, flag: int):
        match flag:
            case 1:  # visited
                return ["deeppink" if u.visited else "white" for u in self.G.nodes()]
            case 2:  # attributes color
                return [
                    "gray" if u.color == BLACK else "white" if u.color == WHITE else "lightgray" if u.color == GREY else "deeppink"
                    for u in self.G.nodes()]
        return ["deeppink" if u.visited else "white" for u in self.G.nodes()]

    def show_traverse_step_by_step_during(self, from_node: Node, to_node: Node, title: str, flag: int) -> None:
        self.G[from_node][to_node]["color"] = "deeppink"
        self.visualize(node_colors=self.get_node_colors_based_on_alg(flag), title=title)

    def show_traverse_tree(self, tree_traverse: List[Tuple[Node, Node]], title, flag: int) -> None:
        """
        Changes the colour of each edge that is in the BFS tree
        (to pink colour, because pink (viva magenta) is the colour of the year 2023)

        Calls two functions for visualizing traverse of algorithm and resulting traverse with important edges.

        :param title: title of the graph
        :param tree_traverse: list of tuples, each tuple contains two nodes that creates edge
        :param flag: 1 for algorithms only with visited attributes, 2 for coloured algorithms
        :return: None
        """
        for u, v in tree_traverse:
            self.G[u][v]["color"] = "deeppink"

        self.visualize(node_colors=self.get_node_colors_based_on_alg(flag), title=title)
        self.visualize(self.get_node_colors_based_on_alg(flag), traverse_tree=True, traverse_edges=tree_traverse,
                       title=title)

        for u, v in tree_traverse:
            self.G[u][v]["color"] = "black"

    def __show_hamiltonian_path(self, ham_path):
        for i in range(1, len(ham_path)):
            self.G[ham_path[i - 1]][ham_path[i]]["color"] = "deeppink"

        self.visualize(title="Hamiltonian path - brute force")

        for i in range(1, len(ham_path)):
            self.G[ham_path[i - 1]][ham_path[i]]["color"] = "black"

    """
        BFS -- breadth first search
    """

    def BFS_basic(self, start: Node, show_tree: bool = False, step_by_step: bool = False) -> None:
        """
        Traverse a graph with breadth first search (BFS) from starting node.
        Sets visited attribute of nodes to True or False.

        :param start: starting node
        :param show_tree: True to visualize and show BFS tree, False otherwise
        :param step_by_step: True to show step by step traverse (in more images - one image for one step), False otherwise
        :return: none
        """

        self.initialize_node_values()

        BFS_tree: List[Tuple[Node, Node]] = []

        # create queue
        queue = Queue()
        queue.put(start)

        start.visited = True

        # main loop
        while not queue.empty():
            node = queue.get()
            for each in self.get_neighbours(node):
                if not each.visited:
                    BFS_tree.append((node, each))
                    each.visited = True
                    # show step by step traverse
                    if step_by_step:
                        self.show_traverse_step_by_step_during(node, each, "BFS - basic", 1)
                    queue.put(each)

        # show tree
        if show_tree:
            self.show_traverse_tree(BFS_tree, "BFS - basic (tree)", 1)

    def BFS_attributes(self, start: Node, show_tree: bool = False, step_by_step: bool = False) -> None:
        """
        Traverse a graph with breadth first search (BFS) from starting node.

        Both for directed and undirected graphs.
        On weighted graphs counts number of edges from starting node to the actual node, not the shortest path.
        On unweighted graphs computes the shortest path from starting node to all other nodes that are reachable.

        Works with 3 attributes:
            -  color (status of exploring),
            -  distance (number of edges from starting node),
            -  pi (predecessor).

        :param start: starting node
        :param show_tree: True to visualize and show BFS tree, False otherwise
        :param step_by_step: True to show step by step traverse (in more images - one image for one step), False otherwise
        :return: none
        """
        self.initialize_node_values()

        BFS_tree: List[Tuple[Node, Node]] = []

        # initialize attributes of each vertex
        for each in self.get_nodes():
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

        # main loop
        while not queue.empty():
            node = queue.get()
            for each in self.get_neighbours(node):
                if each.color == WHITE:
                    BFS_tree.append((node, each))
                    each.color = GREY
                    each.distance = node.distance + 1
                    each.pi = node
                    queue.put(each)
                # show step by step traverse
                if step_by_step:
                    self.show_traverse_step_by_step_during(node, each, "BFS - attributes", 2)
            node.color = BLACK

        # show BFS tree
        if show_tree:
            self.show_traverse_tree(BFS_tree, "BFS - attributes (tree)", 2)

    """
        DFS -- depth first search
    """

    def DFS_iterative_basic(self, start: Node, show_tree: bool = False, step_by_step: bool = False) -> None:
        """
        Traverses graph with depth first search (DFS) from starting node.

        Both for directed and undirected graphs.
        Both for weighted and unweighted graphs.

        Basic iterative version of DFS, uses only attribute visited (state of exploring nodes).

        :param start: starting node
        :param show_tree: True to visualize and show DFS tree, False otherwise
        :param step_by_step: True to show step by step traverse (in more images - one image for one step), False otherwise
        :return: none
        """

        self.initialize_node_values()

        DFS_tree: List[Tuple[Node, Node]] = []

        # initialization
        for each in self.get_nodes():
            each.visited = False
            each.pi = None

        # create stack
        stack = LifoQueue()
        stack.put(start)

        # main loop
        while not stack.empty():

            node = stack.get()

            if not node.visited:
                if node != start:
                    DFS_tree.append((node.pi, node))
                node.visited = True
                # show step by step traverse
                if step_by_step and node != start:
                    self.show_traverse_step_by_step_during(node.pi, node, "DFS - basic", flag=1)
                for each in self.get_neighbours(node):
                    if not each.visited:
                        each.pi = node  # set predecessor
                        stack.put(each)

        # show DFS tree
        if show_tree:
            self.show_traverse_tree(DFS_tree, "DFS - basic (tree)", 1)

    def get_white_neighbour(self, node):
        for each in self.get_neighbours(node):
            if each.color == WHITE:
                return each
        return None

    def DFS_iterative_attributes(self, start: Node, show_tree: bool = False, step_by_step: bool = False) -> None:
        """
        Traverses graph with depth first search (DFS) from starting node.

        Both for directed and undirected graphs.
        Both for weighted and unweighted graphs.

        Works with 3 attributes:
            -  color (status of exploring),
            -  pi (predecessor),
            -  discovery_time (when the node is first discovered),
            -  finishing_time (when the search on the node finishes).

        :param start: starting node
        :param show_tree: True to visualize and show DFS tree, False otherwise
        :param step_by_step: True to show step by step traverse (in more images - one image for one step), False otherwise
        :return: none
        """

        self.initialize_node_values()

        DFS_tree: List[Tuple[Node, Node]] = []

        # initialization
        time = 0
        for each in self.get_nodes():
            each.pi = None
            each.color = WHITE
            each.discovery_time = math.inf
            each.finishing_time = math.inf

        # create stack
        stack = LifoQueue()
        stack.put(start)

        # time start
        time += 1
        start.color = GREY
        start.discovery_time = time

        # main loop
        while not stack.empty():

            node = stack.get()

            if node != start:
                DFS_tree.append((node.pi, node))

            neighbour = self.get_white_neighbour(node)
            # if exists edge (node, neighbour) where neighbour.color=white
            # that means neighbour has not been visited yet
            if neighbour is not None:
                stack.put(node)
                stack.put(neighbour)
                neighbour.color = GREY
                neighbour.pi = node
                time += 1
                neighbour.discovery_time = time
            else:
                node.color = BLACK
                time += 1
                node.finishing_time = time

                # show step by step traverse
            if step_by_step and neighbour:  # and node != start:
                self.show_traverse_step_by_step_during(node, neighbour, "DFS - attributes", 2)

        # show DFS tree
        if show_tree:
            self.show_traverse_tree(DFS_tree, "DFS - attributes (tree)", 2)

    def DFS_recursive_basic(self):
        pass

    def DFS_recursive_attributes(self):
        pass

    """
        Dijkstra´s algorithm
    """

    def dijkstra_algorithm(self, start: Node, show_tree: bool = False, step_by_step: bool = False) -> None:
        """
        Solves shortest path problem from given starting node to all other vertices.
        Uses priority queue (heap).

        :param start: starting node
        :param show_tree: True to visualize and show dijkstra tree, False otherwise
        :param step_by_step: True to show step by step traverse (in more images - one image for one step), False otherwise
        :return: none
        """

        self.initialize_node_values()

        dijkstra_tree: List[Tuple[Node, Node]] = []

        # queue
        q = []

        # set of visited nodes
        S = []

        # initialization
        for each in self.get_nodes():
            each.distance = math.inf
            each.pi = None

        start.distance = 0
        hq.heappush(q, (start.distance, start))

        # main loop
        while q:
            # extract min & add to visited nodes
            prio, node = hq.heappop(q)
            S.append(node)
            node.visited = True

            # all neighbours
            for each in self.get_neighbours(node):
                # if neighbour was visited - skip
                if each in S:
                    continue

                # relax edge condition
                if node.distance + self.adj_matrix()[node.index, each.index] < each.distance:
                    relax_edge(node, each, node.distance + self.adj_matrix()[node.index, each.index],
                               dijkstra_tree)
                    hq.heappush(q, (each.distance, each))
                # show step by step traverse
                if step_by_step:
                    self.show_traverse_step_by_step_during(node, each, "Dijkstra", 1)

        # show Dijkstra traverse
        if show_tree:
            self.show_traverse_tree(dijkstra_tree, "Dijkstra (traverse)", 1)

    """
        Bellman-Ford algorithm
    """

    def delete_colours_visualize(self, title: str):
        for u, v in self.get_edges():
            self.G[u][v]["color"] = "black"
        self.visualize(title=title)

    def bellman_ford(self, start: Node, step_by_step: bool = False) -> bool:
        """
        Solves shortest path problem from given starting node to all other vertices.
        Can be used for graph both with negative and non-negative edge weights.

        :param start:
        :param step_by_step:
        :return: True if and only if the graph contains no negative-weight cycles that are
                 reachable from the source, False otherwise
        """
        # initialization
        self.initialize_node_values()
        for each in self.get_nodes():
            each.distance = math.inf
            each.pi = None

        start.distance = 0

        # repeatedly relaxing edges
        for i in range(self.size - 1):
            if step_by_step:
                self.delete_colours_visualize("Bellman Ford")
                print(f"i: {i}")
            for u, v in self.get_edges():
                if v.distance > u.distance + self.adj_matrix()[u.index, v.index]:
                    v.distance = u.distance + self.adj_matrix()[u.index, v.index]
                    v.pi = u
                if step_by_step:
                    self.show_traverse_step_by_step_during(u, v, "Bellman Ford", 3)

        # checking for negative weighted cycles
        for u, v in self.get_edges():
            if v.distance > u.distance + self.adj_matrix()[u.index, v.index]:
                return False

        return True

    """
        Hamiltonian path problem
    """

    def hamiltonian_path_brute_force_decision(self):
        permutations = itertools.permutations([_ for _ in self.get_nodes()])
        for path in permutations:
            valid_path = True
            for i in range(1, len(path)):
                if self.adj_matrix()[path[i - 1].index, path[i].index] == 0:
                    valid_path = False
                    break
            if valid_path:
                return True
        return False

    def hamiltonian_path_brute_force_all(self, show_ham_paths: bool = True):
        self.__ham_paths = 0
        permutations = itertools.permutations([_ for _ in self.get_nodes()])
        hamiltonian_paths = []
        for path in permutations:
            valid_path = True
            for i in range(1, len(path)):
                if self.adj_matrix()[path[i - 1].index, path[i].index] == 0:
                    valid_path = False
                    break
            if valid_path:
                hamiltonian_paths.append(path)
                self.__ham_paths += 1
                if show_ham_paths:
                    self.__show_hamiltonian_path(path)
        print("number of paths: " + str(self.__ham_paths))
        return self.__ham_paths > 0

    def hamiltonian_path_DFS_decision(self):
        self.__ham_paths = 0
        for node in self.get_nodes():
            visited = [False for _ in range(self.size)]
            visited[node.index] = True
            if self.__hamiltonian_path_DFS_rec_decision(node, visited, [node]):
                return True
        return False

    def __hamiltonian_path_DFS_rec_decision(self, node: Node, visited: list[bool], path: list[Node]):
        if len(path) == self.size:
            self.__ham_paths += 1
            # print("Hamiltonian path found: " + str([node.value for node in path]))
            # self.visualize(title="Hamiltonian path - backtracking")
            return

        for each in self.get_neighbours(node):
            if not visited[each.index]:
                visited[each.index] = True
                path.append(each)

                self.G[node][each]["color"] = "deeppink"

                self.__hamiltonian_path_DFS_rec_decision(each, visited, path)
                if self.__ham_paths > 0:
                    return True
                visited[each.index] = False
                path.pop()

                self.G[node][each]["color"] = "black"

        return False

    def hamiltonian_path_DFS_all(self):
        self.__ham_paths = 0
        for node in self.get_nodes():
            visited = [False for _ in range(self.size)]
            visited[node.index] = True
            self.__hamiltonian_path_DFS_rec_all(node, visited, [node])

        print("number of paths: " + str(self.__ham_paths))
        return self.__ham_paths > 0

    def __hamiltonian_path_DFS_rec_all(self, node: Node, visited: list[bool], path: list[Node]):
        if len(path) == self.size:
            self.__ham_paths += 1
            # print("Hamiltonian path found: " + str([node.value for node in path]))
            self.visualize(title="Hamiltonian path - backtracking")
            return

        for each in self.get_neighbours(node):
            if not visited[each.index]:
                visited[each.index] = True
                path.append(each)

                self.G[node][each]["color"] = "deeppink"

                self.__hamiltonian_path_DFS_rec_all(each, visited, path)
                visited[each.index] = False
                path.pop()

                self.G[node][each]["color"] = "black"

    """
        Travelling salesman problem
    """

    def TSP_brute_force(self, show_tsp: bool = False) -> Tuple[bool, int]:
        """
        Brute force naive algorithm to solve travelling salesman problem.
        Loops through all possible paths in the graphs and checks if the path can be extended to a cycle.
        If yes, checks if the cycle´s length is shorter than the length of the so far found shortest hamiltonian path.

        :param show_tsp: True to show the cycle, False otherwise
        :return: (bool, int) - (True, number): there is a hamiltonian cycle in the graph, the shortest has length of number units
                             - (False, math.int): there is no hamiltonian cycle in the graph
        """

        tsp_cycle = False
        shortest_ham_cycle_length = math.inf
        permutations = itertools.permutations([_ for _ in self.get_nodes()])

        # loop through all paths
        for path in permutations:
            current_length = 0
            valid_path = True
            # loop through all nodes in path
            for i in range(1, len(path)):
                if self.adj_matrix()[path[i - 1].index, path[i].index] == 0:
                    valid_path = False
                    break
                current_length += self.adj_matrix()[path[i - 1].index, path[i].index]

            if valid_path and self.adj_matrix()[path[len(path) - 1].index, path[0].index] != 0:
                # checking for shorter hamiltonian path
                if current_length + self.adj_matrix()[
                    path[len(path) - 1].index, path[0].index] < shortest_ham_cycle_length:
                    shortest_ham_cycle_length = current_length + self.adj_matrix()[
                        path[len(path) - 1].index, path[0].index]  # new shortest hamiltonian path
                    cycle = list(path) + [path[0]]
                    tsp_cycle = True
                    if show_tsp:
                        self.__show_hamiltonian_path(cycle)
        return tsp_cycle, shortest_ham_cycle_length

    def TSP_DFS(self):
        visited = [False for _ in range(self.size)]
        visited[0] = True
        node = list(self.get_nodes())[0]

        shortest_ham_cycle_length = math.inf
        tsp_result = self.__TSP_DFS_rec(node, visited, [node], shortest_ham_cycle_length, 0)
        return tsp_result != math.inf, tsp_result

    def __TSP_DFS_rec(self, node: Node, visited: list[bool], path: list[Node], shortest_ham_cycle_length: int,
                      current_length: int):

        if len(path) == self.size and self.adj_matrix()[path[len(path) - 1].index, path[0].index] != 0:

            # checking for shorter hamiltonian path
            if current_length + self.adj_matrix()[
                path[len(path) - 1].index, path[0].index] < shortest_ham_cycle_length:
                shortest_ham_cycle_length = current_length + self.adj_matrix()[
                    path[len(path) - 1].index, path[0].index]  # new shortest hamiltonian path

                # pink for visualization
                # self.G[path[len(path) - 1]][path[0]]["color"] = "deeppink"
                # self.visualize(title="TSP - backtracking")
                # self.G[path[len(path) - 1]][path[0]]["color"] = "black"

            return shortest_ham_cycle_length

        for each in self.get_neighbours(node):
            if not visited[each.index]:
                visited[each.index] = True
                path.append(each)

                self.G[node][each]["color"] = "deeppink"

                current_length += self.adj_matrix()[node.index, each.index]
                shortest_ham_cycle_length = self.__TSP_DFS_rec(each, visited, path, shortest_ham_cycle_length,
                                                               current_length)
                visited[each.index] = False
                path.pop()
                current_length -= self.adj_matrix()[node.index, each.index]

                self.G[node][each]["color"] = "black"

        return shortest_ham_cycle_length

    def TSP_DFS_cut(self):
        visited = [False for _ in range(self.size)]
        visited[0] = True
        node = list(self.get_nodes())[0]

        shortest_ham_cycle_length = math.inf
        tsp_result = self.__TSP_DFS_cut_rec(node, visited, [node], shortest_ham_cycle_length, 0)
        return tsp_result != math.inf, tsp_result

    def __TSP_DFS_cut_rec(self, node: Node, visited: list[bool], path: list[Node], shortest_ham_cycle_length: int,
                          current_length: int):

        if len(path) == self.size and self.adj_matrix()[path[len(path) - 1].index, path[0].index] != 0:

            # checking for shorter hamiltonian path
            if current_length + self.adj_matrix()[
                path[len(path) - 1].index, path[0].index] < shortest_ham_cycle_length:
                shortest_ham_cycle_length = current_length + self.adj_matrix()[
                    path[len(path) - 1].index, path[0].index]  # new shortest hamiltonian path

                # pink for visualization
                # self.G[path[len(path) - 1]][path[0]]["color"] = "deeppink"
                # self.visualize(title="TSP - backtracking with cut")
                # self.G[path[len(path) - 1]][path[0]]["color"] = "black"

            return shortest_ham_cycle_length

        for each in self.get_neighbours(node):
            if not visited[each.index]:
                visited[each.index] = True
                path.append(each)

                current_length += self.adj_matrix()[node.index, each.index]
                if current_length < shortest_ham_cycle_length:
                    self.G[node][each]["color"] = "deeppink"

                    shortest_ham_cycle_length = self.__TSP_DFS_cut_rec(each, visited, path, shortest_ham_cycle_length,
                                                                       current_length)
                visited[each.index] = False
                path.pop()
                current_length -= self.adj_matrix()[node.index, each.index]

                self.G[node][each]["color"] = "black"

        return shortest_ham_cycle_length

# graph = Graph(False)
# node_00 = Node("Zlin")
# node_01 = Node("Prague")
# node_02 = Node("Brno")
# node_03 = Node(3)
# node_04 = Node(4)
# node_05 = Node(5)
# node_06 = Node(6)
#
# graph.add_node(node_00)
# graph.add_node(node_01)
# graph.add_node(node_02)
# graph.add_node(node_03)
# graph.add_node(node_04)
# graph.add_node(node_05)
# graph.add_node(node_06)
#
# graph.add_edge(node_00, node_01, 10)
# graph.add_edge(node_01, node_02, 20)
# graph.add_edge(node_01, node_03, 1)
# graph.add_edge(node_02, node_05, 5)
# graph.add_edge(node_02, node_03, 1)
# graph.add_edge(node_02, node_06, 12)
# graph.add_edge(node_03, node_04, 1)
# graph.add_edge(node_03, node_00, 1)
# graph.add_edge(node_04, node_05, 6)
# graph.add_edge(node_05, node_02, 2)
# graph.add_edge(node_05, node_06, 2)
# graph.add_edge(node_06, node_01, 3)
# graph.add_edge(node_06, node_04, 7)
# graph.add_edge(node_06, node_00, 1)
# graph.visualize()
# print(graph.TSP_brute_force(show_tsp=True))
# print(graph.TSP_DFS())
# print(graph.TSP_DFS_cut())
# print(graph.hamiltonian_path_brute_force_all())
# print(graph.hamiltonian_path_DFS_all())
# print(graph.hamiltonian_path_DFS_decision())
# print(graph.get_neighbours(node_01))
# print(graph.get_neighbours(node_06))
# print(graph.get_neighbours(node_00))

# graph.BFS_basic(node_01, True, True)
# graph.BFS_attributes(node_02, True)
# graph.DFS_iterative_basic(node_01, True)
# graph.DFS_iterative_attributes(node_01, True)

# graph.dijkstra_algorithm(node_02, True)
# for node in graph.get_nodes():
#     print("{} with {}".format(node.value, node.distance))

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
