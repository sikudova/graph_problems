from random import randint

NODE_VALUE = 25
EDGE_VALUE = 50
GRAPH_AMOUNT = 100
FILE_NAME = "graphs_25_undirected_50.py"

with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
    print("from graph_class import Node, Graph", file=f)
    print('\n# {} undirected graphs with {} nodes, {} edges\n'.format(GRAPH_AMOUNT, NODE_VALUE, EDGE_VALUE), file=f)

for i in range(GRAPH_AMOUNT):

    # create graph
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        print('\n"""\n\tGRAPH {:02d}\n"""\n'.format(i), file=f)
        print("graph_{:02d} = Graph(False)\n".format(i), file=f)

    # create nodes
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        for j in range(NODE_VALUE):
            print("node_{:02d} = Node({})".format(j, j), end="\n", file=f)
        print("", file=f)

    # add nodes
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        for j in range(NODE_VALUE):
            print("graph_{:02d}.add_node(node_{:02d})".format(i, j), end="\n", file=f)
        print("", file=f)

    # add edges
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        for j in range(EDGE_VALUE):
            print("graph_{:02d}.add_edge(node_{:02d}, node_{:02d}, {})".format(i, randint(0, NODE_VALUE - 1),
                                                                               randint(0, NODE_VALUE - 1),
                                                                               randint(1, 20)),
                  end="\n", file=f)
        print("", file=f)
        # print("graph_{:02d}.visualize()".format(i), file=f)
        # print("", file=f)
        # print("graph_{:02d}.BFS_basic(start=node_00, show_tree=True)".format(i), file=f)
        # print("graph_{:02d}.BFS_attributes(start=node_00, show_tree=True)".format(i), file=f)
        # print("graph_{:02d}.DFS_iterative_basic(start=node_00, show_tree=True)".format(i), file=f)
        # print("graph_{:02d}.DFS_iterative_attributes(start=node_00, show_tree=True)".format(i), file=f)
        # print("graph_{:02d}.dijkstra_algorithm(start=node_00, show_tree=True)".format(i), file=f)
        # print("print(graph_{:02d}.hamiltonian_path_brute_force_decision())".format(i), file=f)
        # print("print(graph_{:02d}.hamiltonian_path_DFS_decision())".format(i), file=f)

with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
    print("graphs = [", end="", file=f)
    for i in range(GRAPH_AMOUNT - 1):
        print("graph_{:02d}, ".format(i), end="", file=f)
    print("graph_{:02d}]".format(GRAPH_AMOUNT - 1), end="", file=f)
