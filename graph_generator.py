from random import randint

VALUE = 10

with open('graphs_files/graphs_01.py', 'a') as f:
    print("from graph_class import Node, Graph\n", file=f)
    print("graph = Graph(True)\n", file=f)

for i in range(VALUE):
    with open('graphs_files/graphs_01.py', 'a') as f:
        print("node_{:02d} = Node({})".format(i, i), end="\n", file=f)

with open('graphs_files/graphs_01.py', 'a') as f:
    print("", file=f)

for i in range(VALUE):
    with open('graphs_files/graphs_01.py', 'a') as f:
        print("graph.add_node(node_{:02d})".format(i), end="\n", file=f)

with open('graphs_files/graphs_01.py', 'a') as f:
    print("", file=f)

for i in range(2 * VALUE):
    with open('graphs_files/graphs_01.py', 'a') as f:
        print(
            "graph.add_edge(node_{:02d}, node_{:02d}, {})".format(randint(0, VALUE - 1), randint(0, VALUE - 1),
                                                                  randint(1, 20)), end="\n", file=f)

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
