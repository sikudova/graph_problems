from graph import Graph


def hamiltonian_path(graph, node, path) -> bool:
    print('hamiltonian_path called on node={}, current path={}'.format(node, path))
    path.append(node)
    for each in graph.__matrix[node]:
        pass


graph = Graph(7)
graph.add_edge(0, 1, 10)
graph.add_edge(1, 2, 15)
graph.add_edge(1, 3)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 2)
