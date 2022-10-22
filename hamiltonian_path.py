from graph import Graph


# TODO: color edges if contained in the path
# TODO: add to class as public function?

def hamiltonian_path(graph: "Graph", node: int, path: list[int]):  # -> bool:
    print("hamiltonian_path called on node={}, current path={}".format(node, path))
    if node not in path:
        path.append(node)

        if len(path) == graph.size:
            print("Hamiltonian path found: " + str(path))
            return True

        print("neighbours: " + str(graph.get_neighbours(node)))
        for each in graph.get_neighbours(node):
            if not hamiltonian_path(graph, each, path):
                print("not found with node {}".format(each))

        path.pop()
    else:
        print("the node {} is already in the path, the condition for the hamiltonian path can not be fulfilled".format(
            node))
        return False


graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 2)
graph.add_edge(6, 0)
graph.visualize()
hamiltonian_path(graph, 0, [])
# print(graph.get_neighbours(6))
