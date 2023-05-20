from random import randint

VALUE = 15
GRAPH_AMOUNT = 10
FILE_NAME = "graphs_15_undirected.py"

with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
    print("from graph_class import Node, Graph", file=f)

for i in range(GRAPH_AMOUNT):

    # create graph
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        print('\n"""\n\tGRAPH {:02d}\n"""\n'.format(i), file=f)
        print("graph_{:02d} = Graph(False)\n".format(i), file=f)

    # create nodes
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        for j in range(VALUE):
            print("node_{:02d} = Node({})".format(j, j), end="\n", file=f)
        print("", file=f)

    # add nodes
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        for j in range(VALUE):
            print("graph_{:02d}.add_node(node_{:02d})".format(i, j), end="\n", file=f)
        print("", file=f)

    # add edges
    with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
        for j in range(2 * VALUE):
            print("graph_{:02d}.add_edge(node_{:02d}, node_{:02d}, {})".format(i, randint(0, VALUE - 1),
                                                                               randint(0, VALUE - 1), randint(1, 20)),
                  end="\n", file=f)
        print("", file=f)
        print("graph_{:02d}.visualize()".format(i), file=f)
        print("", file=f)
        print("graph_{:02d}.BFS_basic(start=node_00, show_tree=True)".format(i), file=f)
        print("graph_{:02d}.BFS_attributes(start=node_00, show_tree=True)".format(i), file=f)
        print("graph_{:02d}.DFS_iterative_basic(start=node_00, show_tree=True)".format(i), file=f)
        print("graph_{:02d}.dijkstra_algorithm(start=node_00, show_tree=True)".format(i), file=f)

with open('graphs_files/{}'.format(FILE_NAME), 'a') as f:
    print("graphs = [", end="", file=f)
    for i in range(GRAPH_AMOUNT - 1):
        print("graph_{:02d}, ".format(i), end="", file=f)
    print("graph_{:02d}]".format(GRAPH_AMOUNT - 1), end="", file=f)

# graph.add_node(node_00)

# import numpy as np
#
# with open('integer_files/lattices_10_1.py', 'a') as f:
#     print("import numpy as np\n", file=f)
#
# for i in range(1, 11):
#     matrix = np.random.randint(-50, 51, size=(20, 20))
#     with open('integer_files/lattices_10_1.py', 'a') as f:
#         print("lattice_" + str(i) + " = np.", end="", file=f)
#         print(repr(matrix), file=f)
#         print("\n", file=f)
#
# with open('integer_files/lattices_10_1.py', 'a') as f:
#     print("array = [", file=f)
#     for i in range(1, 11):
#         print(", lattice_" + str(i), end="", file=f)
#     print("]", file=f)
