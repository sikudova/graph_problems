from graph_class import Node, Graph

# 100 undirected graphs with 5 nodes, 10 edges


"""
	GRAPH 00
"""

graph_00 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_00.add_node(node_00)
graph_00.add_node(node_01)
graph_00.add_node(node_02)
graph_00.add_node(node_03)
graph_00.add_node(node_04)

graph_00.add_edge(node_04, node_04, 6)
graph_00.add_edge(node_03, node_01, 15)
graph_00.add_edge(node_04, node_02, 7)
graph_00.add_edge(node_04, node_01, 9)
graph_00.add_edge(node_01, node_02, 17)
graph_00.add_edge(node_02, node_02, 19)
graph_00.add_edge(node_04, node_03, 10)
graph_00.add_edge(node_03, node_00, 11)
graph_00.add_edge(node_01, node_00, 18)
graph_00.add_edge(node_01, node_00, 1)

"""
	GRAPH 01
"""

graph_01 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_01.add_node(node_00)
graph_01.add_node(node_01)
graph_01.add_node(node_02)
graph_01.add_node(node_03)
graph_01.add_node(node_04)

graph_01.add_edge(node_01, node_04, 1)
graph_01.add_edge(node_00, node_03, 2)
graph_01.add_edge(node_03, node_04, 7)
graph_01.add_edge(node_00, node_01, 7)
graph_01.add_edge(node_01, node_03, 2)
graph_01.add_edge(node_00, node_01, 17)
graph_01.add_edge(node_01, node_00, 15)
graph_01.add_edge(node_02, node_02, 9)
graph_01.add_edge(node_04, node_02, 12)
graph_01.add_edge(node_04, node_01, 9)

"""
	GRAPH 02
"""

graph_02 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_02.add_node(node_00)
graph_02.add_node(node_01)
graph_02.add_node(node_02)
graph_02.add_node(node_03)
graph_02.add_node(node_04)

graph_02.add_edge(node_04, node_04, 9)
graph_02.add_edge(node_00, node_00, 5)
graph_02.add_edge(node_00, node_01, 10)
graph_02.add_edge(node_00, node_04, 18)
graph_02.add_edge(node_04, node_00, 16)
graph_02.add_edge(node_03, node_01, 6)
graph_02.add_edge(node_00, node_04, 9)
graph_02.add_edge(node_02, node_00, 13)
graph_02.add_edge(node_02, node_02, 16)
graph_02.add_edge(node_02, node_01, 16)

"""
	GRAPH 03
"""

graph_03 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_03.add_node(node_00)
graph_03.add_node(node_01)
graph_03.add_node(node_02)
graph_03.add_node(node_03)
graph_03.add_node(node_04)

graph_03.add_edge(node_03, node_03, 9)
graph_03.add_edge(node_04, node_00, 3)
graph_03.add_edge(node_00, node_02, 3)
graph_03.add_edge(node_02, node_04, 16)
graph_03.add_edge(node_02, node_03, 13)
graph_03.add_edge(node_03, node_03, 13)
graph_03.add_edge(node_04, node_02, 15)
graph_03.add_edge(node_00, node_02, 8)
graph_03.add_edge(node_00, node_02, 20)
graph_03.add_edge(node_01, node_02, 9)

"""
	GRAPH 04
"""

graph_04 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_04.add_node(node_00)
graph_04.add_node(node_01)
graph_04.add_node(node_02)
graph_04.add_node(node_03)
graph_04.add_node(node_04)

graph_04.add_edge(node_01, node_03, 19)
graph_04.add_edge(node_01, node_04, 14)
graph_04.add_edge(node_04, node_04, 17)
graph_04.add_edge(node_00, node_03, 6)
graph_04.add_edge(node_01, node_00, 10)
graph_04.add_edge(node_00, node_01, 7)
graph_04.add_edge(node_02, node_03, 8)
graph_04.add_edge(node_00, node_04, 19)
graph_04.add_edge(node_04, node_02, 10)
graph_04.add_edge(node_03, node_01, 8)

"""
	GRAPH 05
"""

graph_05 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_05.add_node(node_00)
graph_05.add_node(node_01)
graph_05.add_node(node_02)
graph_05.add_node(node_03)
graph_05.add_node(node_04)

graph_05.add_edge(node_00, node_00, 16)
graph_05.add_edge(node_02, node_02, 15)
graph_05.add_edge(node_01, node_04, 13)
graph_05.add_edge(node_01, node_00, 20)
graph_05.add_edge(node_01, node_04, 18)
graph_05.add_edge(node_00, node_03, 6)
graph_05.add_edge(node_00, node_04, 10)
graph_05.add_edge(node_01, node_04, 18)
graph_05.add_edge(node_03, node_01, 17)
graph_05.add_edge(node_04, node_03, 16)

"""
	GRAPH 06
"""

graph_06 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_06.add_node(node_00)
graph_06.add_node(node_01)
graph_06.add_node(node_02)
graph_06.add_node(node_03)
graph_06.add_node(node_04)

graph_06.add_edge(node_00, node_01, 11)
graph_06.add_edge(node_03, node_02, 13)
graph_06.add_edge(node_00, node_03, 12)
graph_06.add_edge(node_02, node_02, 6)
graph_06.add_edge(node_01, node_02, 2)
graph_06.add_edge(node_03, node_04, 18)
graph_06.add_edge(node_04, node_03, 10)
graph_06.add_edge(node_01, node_01, 19)
graph_06.add_edge(node_00, node_00, 1)
graph_06.add_edge(node_00, node_02, 12)

"""
	GRAPH 07
"""

graph_07 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_07.add_node(node_00)
graph_07.add_node(node_01)
graph_07.add_node(node_02)
graph_07.add_node(node_03)
graph_07.add_node(node_04)

graph_07.add_edge(node_02, node_01, 6)
graph_07.add_edge(node_00, node_01, 20)
graph_07.add_edge(node_02, node_04, 17)
graph_07.add_edge(node_02, node_02, 16)
graph_07.add_edge(node_02, node_02, 6)
graph_07.add_edge(node_03, node_01, 19)
graph_07.add_edge(node_03, node_04, 9)
graph_07.add_edge(node_04, node_02, 14)
graph_07.add_edge(node_02, node_01, 1)
graph_07.add_edge(node_01, node_03, 17)

"""
	GRAPH 08
"""

graph_08 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_08.add_node(node_00)
graph_08.add_node(node_01)
graph_08.add_node(node_02)
graph_08.add_node(node_03)
graph_08.add_node(node_04)

graph_08.add_edge(node_01, node_02, 2)
graph_08.add_edge(node_02, node_03, 9)
graph_08.add_edge(node_02, node_02, 4)
graph_08.add_edge(node_00, node_01, 15)
graph_08.add_edge(node_03, node_00, 12)
graph_08.add_edge(node_02, node_01, 7)
graph_08.add_edge(node_02, node_03, 12)
graph_08.add_edge(node_02, node_04, 17)
graph_08.add_edge(node_03, node_01, 18)
graph_08.add_edge(node_03, node_03, 2)

"""
	GRAPH 09
"""

graph_09 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_09.add_node(node_00)
graph_09.add_node(node_01)
graph_09.add_node(node_02)
graph_09.add_node(node_03)
graph_09.add_node(node_04)

graph_09.add_edge(node_00, node_02, 13)
graph_09.add_edge(node_03, node_00, 7)
graph_09.add_edge(node_00, node_02, 9)
graph_09.add_edge(node_04, node_04, 13)
graph_09.add_edge(node_00, node_03, 12)
graph_09.add_edge(node_02, node_04, 1)
graph_09.add_edge(node_04, node_01, 9)
graph_09.add_edge(node_01, node_02, 2)
graph_09.add_edge(node_00, node_04, 5)
graph_09.add_edge(node_03, node_01, 5)

"""
	GRAPH 10
"""

graph_10 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_10.add_node(node_00)
graph_10.add_node(node_01)
graph_10.add_node(node_02)
graph_10.add_node(node_03)
graph_10.add_node(node_04)

graph_10.add_edge(node_02, node_03, 6)
graph_10.add_edge(node_01, node_01, 6)
graph_10.add_edge(node_04, node_00, 12)
graph_10.add_edge(node_03, node_01, 11)
graph_10.add_edge(node_03, node_00, 2)
graph_10.add_edge(node_01, node_01, 10)
graph_10.add_edge(node_00, node_03, 20)
graph_10.add_edge(node_01, node_03, 12)
graph_10.add_edge(node_01, node_04, 6)
graph_10.add_edge(node_00, node_01, 9)

"""
	GRAPH 11
"""

graph_11 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_11.add_node(node_00)
graph_11.add_node(node_01)
graph_11.add_node(node_02)
graph_11.add_node(node_03)
graph_11.add_node(node_04)

graph_11.add_edge(node_04, node_01, 11)
graph_11.add_edge(node_03, node_00, 8)
graph_11.add_edge(node_04, node_00, 16)
graph_11.add_edge(node_01, node_03, 1)
graph_11.add_edge(node_02, node_04, 6)
graph_11.add_edge(node_00, node_00, 17)
graph_11.add_edge(node_02, node_02, 17)
graph_11.add_edge(node_02, node_03, 19)
graph_11.add_edge(node_00, node_03, 4)
graph_11.add_edge(node_00, node_02, 9)

"""
	GRAPH 12
"""

graph_12 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_12.add_node(node_00)
graph_12.add_node(node_01)
graph_12.add_node(node_02)
graph_12.add_node(node_03)
graph_12.add_node(node_04)

graph_12.add_edge(node_01, node_03, 18)
graph_12.add_edge(node_00, node_00, 1)
graph_12.add_edge(node_00, node_03, 19)
graph_12.add_edge(node_02, node_00, 14)
graph_12.add_edge(node_00, node_00, 6)
graph_12.add_edge(node_01, node_04, 19)
graph_12.add_edge(node_03, node_04, 11)
graph_12.add_edge(node_01, node_02, 9)
graph_12.add_edge(node_03, node_00, 9)
graph_12.add_edge(node_00, node_01, 18)

"""
	GRAPH 13
"""

graph_13 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_13.add_node(node_00)
graph_13.add_node(node_01)
graph_13.add_node(node_02)
graph_13.add_node(node_03)
graph_13.add_node(node_04)

graph_13.add_edge(node_02, node_02, 10)
graph_13.add_edge(node_02, node_03, 1)
graph_13.add_edge(node_01, node_02, 8)
graph_13.add_edge(node_04, node_03, 7)
graph_13.add_edge(node_02, node_02, 13)
graph_13.add_edge(node_02, node_03, 13)
graph_13.add_edge(node_03, node_04, 17)
graph_13.add_edge(node_00, node_04, 9)
graph_13.add_edge(node_00, node_02, 17)
graph_13.add_edge(node_00, node_02, 20)

"""
	GRAPH 14
"""

graph_14 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_14.add_node(node_00)
graph_14.add_node(node_01)
graph_14.add_node(node_02)
graph_14.add_node(node_03)
graph_14.add_node(node_04)

graph_14.add_edge(node_04, node_04, 1)
graph_14.add_edge(node_01, node_00, 15)
graph_14.add_edge(node_04, node_03, 9)
graph_14.add_edge(node_00, node_02, 8)
graph_14.add_edge(node_02, node_04, 15)
graph_14.add_edge(node_03, node_04, 3)
graph_14.add_edge(node_01, node_01, 17)
graph_14.add_edge(node_02, node_02, 5)
graph_14.add_edge(node_00, node_00, 12)
graph_14.add_edge(node_00, node_04, 14)

"""
	GRAPH 15
"""

graph_15 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_15.add_node(node_00)
graph_15.add_node(node_01)
graph_15.add_node(node_02)
graph_15.add_node(node_03)
graph_15.add_node(node_04)

graph_15.add_edge(node_04, node_03, 10)
graph_15.add_edge(node_04, node_03, 4)
graph_15.add_edge(node_03, node_01, 12)
graph_15.add_edge(node_04, node_01, 11)
graph_15.add_edge(node_03, node_01, 6)
graph_15.add_edge(node_04, node_01, 5)
graph_15.add_edge(node_04, node_03, 14)
graph_15.add_edge(node_00, node_03, 3)
graph_15.add_edge(node_01, node_00, 12)
graph_15.add_edge(node_03, node_04, 17)

"""
	GRAPH 16
"""

graph_16 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_16.add_node(node_00)
graph_16.add_node(node_01)
graph_16.add_node(node_02)
graph_16.add_node(node_03)
graph_16.add_node(node_04)

graph_16.add_edge(node_00, node_02, 9)
graph_16.add_edge(node_01, node_03, 18)
graph_16.add_edge(node_04, node_01, 14)
graph_16.add_edge(node_01, node_02, 3)
graph_16.add_edge(node_01, node_03, 3)
graph_16.add_edge(node_00, node_02, 16)
graph_16.add_edge(node_01, node_02, 9)
graph_16.add_edge(node_03, node_04, 1)
graph_16.add_edge(node_04, node_00, 20)
graph_16.add_edge(node_00, node_01, 14)

"""
	GRAPH 17
"""

graph_17 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_17.add_node(node_00)
graph_17.add_node(node_01)
graph_17.add_node(node_02)
graph_17.add_node(node_03)
graph_17.add_node(node_04)

graph_17.add_edge(node_03, node_00, 13)
graph_17.add_edge(node_00, node_00, 2)
graph_17.add_edge(node_00, node_03, 12)
graph_17.add_edge(node_01, node_00, 14)
graph_17.add_edge(node_03, node_03, 20)
graph_17.add_edge(node_03, node_03, 10)
graph_17.add_edge(node_01, node_02, 8)
graph_17.add_edge(node_03, node_02, 17)
graph_17.add_edge(node_00, node_02, 5)
graph_17.add_edge(node_00, node_00, 2)

"""
	GRAPH 18
"""

graph_18 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_18.add_node(node_00)
graph_18.add_node(node_01)
graph_18.add_node(node_02)
graph_18.add_node(node_03)
graph_18.add_node(node_04)

graph_18.add_edge(node_03, node_01, 15)
graph_18.add_edge(node_04, node_01, 10)
graph_18.add_edge(node_04, node_03, 9)
graph_18.add_edge(node_03, node_04, 1)
graph_18.add_edge(node_04, node_00, 10)
graph_18.add_edge(node_03, node_00, 2)
graph_18.add_edge(node_01, node_01, 9)
graph_18.add_edge(node_00, node_04, 12)
graph_18.add_edge(node_00, node_03, 17)
graph_18.add_edge(node_02, node_04, 18)

"""
	GRAPH 19
"""

graph_19 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_19.add_node(node_00)
graph_19.add_node(node_01)
graph_19.add_node(node_02)
graph_19.add_node(node_03)
graph_19.add_node(node_04)

graph_19.add_edge(node_04, node_00, 20)
graph_19.add_edge(node_01, node_04, 16)
graph_19.add_edge(node_00, node_03, 18)
graph_19.add_edge(node_02, node_04, 12)
graph_19.add_edge(node_02, node_04, 6)
graph_19.add_edge(node_04, node_00, 9)
graph_19.add_edge(node_04, node_03, 17)
graph_19.add_edge(node_00, node_01, 7)
graph_19.add_edge(node_03, node_01, 20)
graph_19.add_edge(node_04, node_01, 7)

"""
	GRAPH 20
"""

graph_20 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_20.add_node(node_00)
graph_20.add_node(node_01)
graph_20.add_node(node_02)
graph_20.add_node(node_03)
graph_20.add_node(node_04)

graph_20.add_edge(node_04, node_04, 6)
graph_20.add_edge(node_00, node_04, 9)
graph_20.add_edge(node_01, node_01, 12)
graph_20.add_edge(node_02, node_04, 5)
graph_20.add_edge(node_02, node_02, 4)
graph_20.add_edge(node_00, node_02, 15)
graph_20.add_edge(node_04, node_03, 7)
graph_20.add_edge(node_03, node_01, 11)
graph_20.add_edge(node_03, node_03, 5)
graph_20.add_edge(node_03, node_00, 10)

"""
	GRAPH 21
"""

graph_21 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_21.add_node(node_00)
graph_21.add_node(node_01)
graph_21.add_node(node_02)
graph_21.add_node(node_03)
graph_21.add_node(node_04)

graph_21.add_edge(node_03, node_02, 1)
graph_21.add_edge(node_00, node_03, 4)
graph_21.add_edge(node_02, node_04, 3)
graph_21.add_edge(node_03, node_03, 12)
graph_21.add_edge(node_04, node_01, 15)
graph_21.add_edge(node_00, node_01, 10)
graph_21.add_edge(node_00, node_02, 5)
graph_21.add_edge(node_02, node_00, 3)
graph_21.add_edge(node_00, node_03, 13)
graph_21.add_edge(node_03, node_01, 3)

"""
	GRAPH 22
"""

graph_22 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_22.add_node(node_00)
graph_22.add_node(node_01)
graph_22.add_node(node_02)
graph_22.add_node(node_03)
graph_22.add_node(node_04)

graph_22.add_edge(node_02, node_04, 14)
graph_22.add_edge(node_03, node_01, 14)
graph_22.add_edge(node_04, node_02, 1)
graph_22.add_edge(node_04, node_02, 12)
graph_22.add_edge(node_03, node_04, 6)
graph_22.add_edge(node_01, node_04, 4)
graph_22.add_edge(node_03, node_01, 11)
graph_22.add_edge(node_02, node_04, 18)
graph_22.add_edge(node_02, node_00, 1)
graph_22.add_edge(node_01, node_04, 12)

"""
	GRAPH 23
"""

graph_23 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_23.add_node(node_00)
graph_23.add_node(node_01)
graph_23.add_node(node_02)
graph_23.add_node(node_03)
graph_23.add_node(node_04)

graph_23.add_edge(node_04, node_04, 2)
graph_23.add_edge(node_00, node_03, 4)
graph_23.add_edge(node_02, node_00, 20)
graph_23.add_edge(node_04, node_03, 12)
graph_23.add_edge(node_02, node_01, 3)
graph_23.add_edge(node_03, node_00, 11)
graph_23.add_edge(node_02, node_00, 2)
graph_23.add_edge(node_02, node_02, 2)
graph_23.add_edge(node_01, node_01, 12)
graph_23.add_edge(node_04, node_04, 1)

"""
	GRAPH 24
"""

graph_24 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_24.add_node(node_00)
graph_24.add_node(node_01)
graph_24.add_node(node_02)
graph_24.add_node(node_03)
graph_24.add_node(node_04)

graph_24.add_edge(node_02, node_03, 20)
graph_24.add_edge(node_02, node_02, 1)
graph_24.add_edge(node_00, node_01, 3)
graph_24.add_edge(node_02, node_03, 16)
graph_24.add_edge(node_02, node_03, 7)
graph_24.add_edge(node_01, node_01, 6)
graph_24.add_edge(node_01, node_01, 5)
graph_24.add_edge(node_04, node_01, 1)
graph_24.add_edge(node_01, node_01, 10)
graph_24.add_edge(node_02, node_03, 9)

"""
	GRAPH 25
"""

graph_25 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_25.add_node(node_00)
graph_25.add_node(node_01)
graph_25.add_node(node_02)
graph_25.add_node(node_03)
graph_25.add_node(node_04)

graph_25.add_edge(node_04, node_04, 1)
graph_25.add_edge(node_04, node_02, 14)
graph_25.add_edge(node_00, node_03, 16)
graph_25.add_edge(node_01, node_03, 7)
graph_25.add_edge(node_04, node_04, 18)
graph_25.add_edge(node_03, node_02, 7)
graph_25.add_edge(node_02, node_00, 9)
graph_25.add_edge(node_01, node_02, 10)
graph_25.add_edge(node_00, node_00, 14)
graph_25.add_edge(node_01, node_00, 1)

"""
	GRAPH 26
"""

graph_26 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_26.add_node(node_00)
graph_26.add_node(node_01)
graph_26.add_node(node_02)
graph_26.add_node(node_03)
graph_26.add_node(node_04)

graph_26.add_edge(node_02, node_02, 2)
graph_26.add_edge(node_00, node_04, 15)
graph_26.add_edge(node_03, node_00, 20)
graph_26.add_edge(node_00, node_02, 18)
graph_26.add_edge(node_00, node_02, 1)
graph_26.add_edge(node_04, node_03, 6)
graph_26.add_edge(node_01, node_00, 6)
graph_26.add_edge(node_03, node_01, 8)
graph_26.add_edge(node_00, node_04, 2)
graph_26.add_edge(node_00, node_02, 6)

"""
	GRAPH 27
"""

graph_27 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_27.add_node(node_00)
graph_27.add_node(node_01)
graph_27.add_node(node_02)
graph_27.add_node(node_03)
graph_27.add_node(node_04)

graph_27.add_edge(node_00, node_01, 15)
graph_27.add_edge(node_04, node_04, 19)
graph_27.add_edge(node_04, node_00, 20)
graph_27.add_edge(node_01, node_04, 19)
graph_27.add_edge(node_03, node_02, 13)
graph_27.add_edge(node_00, node_04, 20)
graph_27.add_edge(node_01, node_00, 14)
graph_27.add_edge(node_01, node_00, 15)
graph_27.add_edge(node_00, node_00, 7)
graph_27.add_edge(node_00, node_00, 12)

"""
	GRAPH 28
"""

graph_28 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_28.add_node(node_00)
graph_28.add_node(node_01)
graph_28.add_node(node_02)
graph_28.add_node(node_03)
graph_28.add_node(node_04)

graph_28.add_edge(node_01, node_03, 1)
graph_28.add_edge(node_02, node_01, 17)
graph_28.add_edge(node_04, node_02, 13)
graph_28.add_edge(node_01, node_02, 2)
graph_28.add_edge(node_00, node_02, 9)
graph_28.add_edge(node_04, node_03, 14)
graph_28.add_edge(node_04, node_03, 7)
graph_28.add_edge(node_00, node_03, 18)
graph_28.add_edge(node_04, node_00, 18)
graph_28.add_edge(node_01, node_02, 5)

"""
	GRAPH 29
"""

graph_29 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_29.add_node(node_00)
graph_29.add_node(node_01)
graph_29.add_node(node_02)
graph_29.add_node(node_03)
graph_29.add_node(node_04)

graph_29.add_edge(node_02, node_02, 20)
graph_29.add_edge(node_00, node_00, 17)
graph_29.add_edge(node_01, node_01, 11)
graph_29.add_edge(node_03, node_04, 20)
graph_29.add_edge(node_03, node_04, 4)
graph_29.add_edge(node_04, node_00, 15)
graph_29.add_edge(node_01, node_02, 14)
graph_29.add_edge(node_04, node_02, 2)
graph_29.add_edge(node_00, node_02, 18)
graph_29.add_edge(node_02, node_00, 4)

"""
	GRAPH 30
"""

graph_30 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_30.add_node(node_00)
graph_30.add_node(node_01)
graph_30.add_node(node_02)
graph_30.add_node(node_03)
graph_30.add_node(node_04)

graph_30.add_edge(node_01, node_00, 2)
graph_30.add_edge(node_03, node_02, 12)
graph_30.add_edge(node_00, node_03, 16)
graph_30.add_edge(node_00, node_04, 19)
graph_30.add_edge(node_00, node_04, 8)
graph_30.add_edge(node_04, node_02, 7)
graph_30.add_edge(node_01, node_00, 15)
graph_30.add_edge(node_02, node_04, 2)
graph_30.add_edge(node_03, node_03, 3)
graph_30.add_edge(node_00, node_02, 6)

"""
	GRAPH 31
"""

graph_31 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_31.add_node(node_00)
graph_31.add_node(node_01)
graph_31.add_node(node_02)
graph_31.add_node(node_03)
graph_31.add_node(node_04)

graph_31.add_edge(node_02, node_02, 18)
graph_31.add_edge(node_04, node_03, 12)
graph_31.add_edge(node_03, node_02, 12)
graph_31.add_edge(node_04, node_00, 18)
graph_31.add_edge(node_04, node_01, 12)
graph_31.add_edge(node_00, node_02, 10)
graph_31.add_edge(node_04, node_04, 13)
graph_31.add_edge(node_01, node_01, 18)
graph_31.add_edge(node_00, node_04, 20)
graph_31.add_edge(node_02, node_01, 1)

"""
	GRAPH 32
"""

graph_32 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_32.add_node(node_00)
graph_32.add_node(node_01)
graph_32.add_node(node_02)
graph_32.add_node(node_03)
graph_32.add_node(node_04)

graph_32.add_edge(node_00, node_00, 11)
graph_32.add_edge(node_02, node_04, 2)
graph_32.add_edge(node_00, node_00, 13)
graph_32.add_edge(node_00, node_02, 14)
graph_32.add_edge(node_00, node_03, 12)
graph_32.add_edge(node_03, node_01, 19)
graph_32.add_edge(node_02, node_03, 18)
graph_32.add_edge(node_03, node_04, 7)
graph_32.add_edge(node_04, node_03, 11)
graph_32.add_edge(node_04, node_00, 6)

"""
	GRAPH 33
"""

graph_33 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_33.add_node(node_00)
graph_33.add_node(node_01)
graph_33.add_node(node_02)
graph_33.add_node(node_03)
graph_33.add_node(node_04)

graph_33.add_edge(node_02, node_04, 17)
graph_33.add_edge(node_02, node_00, 8)
graph_33.add_edge(node_04, node_03, 15)
graph_33.add_edge(node_02, node_04, 9)
graph_33.add_edge(node_03, node_01, 9)
graph_33.add_edge(node_03, node_00, 2)
graph_33.add_edge(node_00, node_02, 19)
graph_33.add_edge(node_00, node_01, 17)
graph_33.add_edge(node_04, node_01, 18)
graph_33.add_edge(node_03, node_03, 19)

"""
	GRAPH 34
"""

graph_34 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_34.add_node(node_00)
graph_34.add_node(node_01)
graph_34.add_node(node_02)
graph_34.add_node(node_03)
graph_34.add_node(node_04)

graph_34.add_edge(node_04, node_00, 8)
graph_34.add_edge(node_02, node_00, 9)
graph_34.add_edge(node_01, node_00, 16)
graph_34.add_edge(node_02, node_03, 8)
graph_34.add_edge(node_04, node_03, 14)
graph_34.add_edge(node_01, node_02, 13)
graph_34.add_edge(node_02, node_00, 20)
graph_34.add_edge(node_04, node_02, 13)
graph_34.add_edge(node_02, node_02, 4)
graph_34.add_edge(node_00, node_04, 12)

"""
	GRAPH 35
"""

graph_35 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_35.add_node(node_00)
graph_35.add_node(node_01)
graph_35.add_node(node_02)
graph_35.add_node(node_03)
graph_35.add_node(node_04)

graph_35.add_edge(node_01, node_01, 7)
graph_35.add_edge(node_00, node_02, 2)
graph_35.add_edge(node_02, node_02, 1)
graph_35.add_edge(node_03, node_03, 5)
graph_35.add_edge(node_01, node_02, 9)
graph_35.add_edge(node_01, node_00, 19)
graph_35.add_edge(node_01, node_03, 10)
graph_35.add_edge(node_01, node_02, 17)
graph_35.add_edge(node_04, node_02, 3)
graph_35.add_edge(node_02, node_01, 5)

"""
	GRAPH 36
"""

graph_36 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_36.add_node(node_00)
graph_36.add_node(node_01)
graph_36.add_node(node_02)
graph_36.add_node(node_03)
graph_36.add_node(node_04)

graph_36.add_edge(node_03, node_00, 10)
graph_36.add_edge(node_00, node_01, 20)
graph_36.add_edge(node_04, node_01, 4)
graph_36.add_edge(node_02, node_04, 1)
graph_36.add_edge(node_00, node_02, 9)
graph_36.add_edge(node_02, node_04, 18)
graph_36.add_edge(node_03, node_01, 10)
graph_36.add_edge(node_02, node_03, 14)
graph_36.add_edge(node_02, node_00, 13)
graph_36.add_edge(node_04, node_03, 4)

"""
	GRAPH 37
"""

graph_37 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_37.add_node(node_00)
graph_37.add_node(node_01)
graph_37.add_node(node_02)
graph_37.add_node(node_03)
graph_37.add_node(node_04)

graph_37.add_edge(node_01, node_00, 19)
graph_37.add_edge(node_01, node_04, 16)
graph_37.add_edge(node_02, node_02, 17)
graph_37.add_edge(node_01, node_04, 3)
graph_37.add_edge(node_01, node_02, 19)
graph_37.add_edge(node_03, node_00, 13)
graph_37.add_edge(node_04, node_04, 1)
graph_37.add_edge(node_02, node_03, 18)
graph_37.add_edge(node_01, node_04, 7)
graph_37.add_edge(node_03, node_01, 2)

"""
	GRAPH 38
"""

graph_38 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_38.add_node(node_00)
graph_38.add_node(node_01)
graph_38.add_node(node_02)
graph_38.add_node(node_03)
graph_38.add_node(node_04)

graph_38.add_edge(node_04, node_04, 6)
graph_38.add_edge(node_00, node_01, 5)
graph_38.add_edge(node_02, node_01, 5)
graph_38.add_edge(node_01, node_00, 4)
graph_38.add_edge(node_04, node_00, 13)
graph_38.add_edge(node_01, node_00, 2)
graph_38.add_edge(node_00, node_01, 13)
graph_38.add_edge(node_01, node_04, 11)
graph_38.add_edge(node_00, node_04, 2)
graph_38.add_edge(node_03, node_02, 18)

"""
	GRAPH 39
"""

graph_39 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_39.add_node(node_00)
graph_39.add_node(node_01)
graph_39.add_node(node_02)
graph_39.add_node(node_03)
graph_39.add_node(node_04)

graph_39.add_edge(node_02, node_03, 7)
graph_39.add_edge(node_04, node_04, 6)
graph_39.add_edge(node_00, node_03, 8)
graph_39.add_edge(node_00, node_02, 13)
graph_39.add_edge(node_04, node_00, 20)
graph_39.add_edge(node_02, node_02, 14)
graph_39.add_edge(node_03, node_03, 19)
graph_39.add_edge(node_00, node_01, 1)
graph_39.add_edge(node_01, node_00, 7)
graph_39.add_edge(node_00, node_01, 18)

"""
	GRAPH 40
"""

graph_40 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_40.add_node(node_00)
graph_40.add_node(node_01)
graph_40.add_node(node_02)
graph_40.add_node(node_03)
graph_40.add_node(node_04)

graph_40.add_edge(node_02, node_01, 9)
graph_40.add_edge(node_01, node_01, 13)
graph_40.add_edge(node_01, node_03, 10)
graph_40.add_edge(node_02, node_03, 11)
graph_40.add_edge(node_02, node_01, 7)
graph_40.add_edge(node_04, node_00, 3)
graph_40.add_edge(node_01, node_02, 8)
graph_40.add_edge(node_04, node_02, 19)
graph_40.add_edge(node_00, node_04, 3)
graph_40.add_edge(node_00, node_03, 18)

"""
	GRAPH 41
"""

graph_41 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_41.add_node(node_00)
graph_41.add_node(node_01)
graph_41.add_node(node_02)
graph_41.add_node(node_03)
graph_41.add_node(node_04)

graph_41.add_edge(node_01, node_04, 16)
graph_41.add_edge(node_01, node_01, 8)
graph_41.add_edge(node_01, node_01, 1)
graph_41.add_edge(node_03, node_03, 19)
graph_41.add_edge(node_01, node_03, 8)
graph_41.add_edge(node_01, node_03, 5)
graph_41.add_edge(node_03, node_02, 1)
graph_41.add_edge(node_01, node_01, 3)
graph_41.add_edge(node_01, node_02, 2)
graph_41.add_edge(node_02, node_01, 20)

"""
	GRAPH 42
"""

graph_42 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_42.add_node(node_00)
graph_42.add_node(node_01)
graph_42.add_node(node_02)
graph_42.add_node(node_03)
graph_42.add_node(node_04)

graph_42.add_edge(node_01, node_00, 18)
graph_42.add_edge(node_02, node_00, 15)
graph_42.add_edge(node_02, node_00, 17)
graph_42.add_edge(node_02, node_01, 17)
graph_42.add_edge(node_00, node_02, 14)
graph_42.add_edge(node_01, node_00, 12)
graph_42.add_edge(node_02, node_01, 7)
graph_42.add_edge(node_00, node_03, 11)
graph_42.add_edge(node_00, node_04, 16)
graph_42.add_edge(node_01, node_00, 7)

"""
	GRAPH 43
"""

graph_43 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_43.add_node(node_00)
graph_43.add_node(node_01)
graph_43.add_node(node_02)
graph_43.add_node(node_03)
graph_43.add_node(node_04)

graph_43.add_edge(node_03, node_04, 20)
graph_43.add_edge(node_03, node_00, 13)
graph_43.add_edge(node_03, node_00, 20)
graph_43.add_edge(node_03, node_01, 1)
graph_43.add_edge(node_04, node_03, 8)
graph_43.add_edge(node_03, node_04, 11)
graph_43.add_edge(node_00, node_02, 16)
graph_43.add_edge(node_01, node_02, 8)
graph_43.add_edge(node_04, node_01, 11)
graph_43.add_edge(node_03, node_03, 9)

"""
	GRAPH 44
"""

graph_44 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_44.add_node(node_00)
graph_44.add_node(node_01)
graph_44.add_node(node_02)
graph_44.add_node(node_03)
graph_44.add_node(node_04)

graph_44.add_edge(node_00, node_02, 13)
graph_44.add_edge(node_02, node_01, 13)
graph_44.add_edge(node_04, node_00, 17)
graph_44.add_edge(node_03, node_00, 10)
graph_44.add_edge(node_02, node_00, 15)
graph_44.add_edge(node_04, node_00, 12)
graph_44.add_edge(node_01, node_01, 2)
graph_44.add_edge(node_02, node_04, 8)
graph_44.add_edge(node_01, node_01, 19)
graph_44.add_edge(node_04, node_01, 7)

"""
	GRAPH 45
"""

graph_45 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_45.add_node(node_00)
graph_45.add_node(node_01)
graph_45.add_node(node_02)
graph_45.add_node(node_03)
graph_45.add_node(node_04)

graph_45.add_edge(node_03, node_03, 19)
graph_45.add_edge(node_01, node_04, 7)
graph_45.add_edge(node_03, node_04, 3)
graph_45.add_edge(node_01, node_02, 11)
graph_45.add_edge(node_01, node_04, 6)
graph_45.add_edge(node_04, node_01, 2)
graph_45.add_edge(node_00, node_02, 1)
graph_45.add_edge(node_03, node_02, 9)
graph_45.add_edge(node_00, node_00, 20)
graph_45.add_edge(node_01, node_02, 2)

"""
	GRAPH 46
"""

graph_46 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_46.add_node(node_00)
graph_46.add_node(node_01)
graph_46.add_node(node_02)
graph_46.add_node(node_03)
graph_46.add_node(node_04)

graph_46.add_edge(node_04, node_01, 7)
graph_46.add_edge(node_02, node_04, 3)
graph_46.add_edge(node_01, node_04, 3)
graph_46.add_edge(node_04, node_01, 14)
graph_46.add_edge(node_02, node_02, 2)
graph_46.add_edge(node_04, node_03, 6)
graph_46.add_edge(node_02, node_04, 1)
graph_46.add_edge(node_03, node_03, 20)
graph_46.add_edge(node_01, node_00, 8)
graph_46.add_edge(node_04, node_04, 12)

"""
	GRAPH 47
"""

graph_47 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_47.add_node(node_00)
graph_47.add_node(node_01)
graph_47.add_node(node_02)
graph_47.add_node(node_03)
graph_47.add_node(node_04)

graph_47.add_edge(node_02, node_01, 3)
graph_47.add_edge(node_04, node_01, 18)
graph_47.add_edge(node_03, node_02, 8)
graph_47.add_edge(node_02, node_04, 16)
graph_47.add_edge(node_03, node_03, 1)
graph_47.add_edge(node_03, node_02, 19)
graph_47.add_edge(node_01, node_04, 18)
graph_47.add_edge(node_03, node_01, 12)
graph_47.add_edge(node_01, node_01, 4)
graph_47.add_edge(node_04, node_02, 12)

"""
	GRAPH 48
"""

graph_48 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_48.add_node(node_00)
graph_48.add_node(node_01)
graph_48.add_node(node_02)
graph_48.add_node(node_03)
graph_48.add_node(node_04)

graph_48.add_edge(node_03, node_02, 20)
graph_48.add_edge(node_04, node_03, 13)
graph_48.add_edge(node_01, node_01, 18)
graph_48.add_edge(node_04, node_03, 16)
graph_48.add_edge(node_04, node_03, 20)
graph_48.add_edge(node_04, node_02, 14)
graph_48.add_edge(node_01, node_01, 2)
graph_48.add_edge(node_03, node_01, 19)
graph_48.add_edge(node_01, node_02, 9)
graph_48.add_edge(node_03, node_02, 18)

"""
	GRAPH 49
"""

graph_49 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_49.add_node(node_00)
graph_49.add_node(node_01)
graph_49.add_node(node_02)
graph_49.add_node(node_03)
graph_49.add_node(node_04)

graph_49.add_edge(node_01, node_01, 11)
graph_49.add_edge(node_02, node_04, 17)
graph_49.add_edge(node_04, node_02, 17)
graph_49.add_edge(node_00, node_00, 6)
graph_49.add_edge(node_04, node_01, 20)
graph_49.add_edge(node_02, node_04, 16)
graph_49.add_edge(node_01, node_03, 19)
graph_49.add_edge(node_01, node_02, 7)
graph_49.add_edge(node_03, node_04, 16)
graph_49.add_edge(node_00, node_01, 13)

"""
	GRAPH 50
"""

graph_50 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_50.add_node(node_00)
graph_50.add_node(node_01)
graph_50.add_node(node_02)
graph_50.add_node(node_03)
graph_50.add_node(node_04)

graph_50.add_edge(node_04, node_01, 12)
graph_50.add_edge(node_01, node_04, 8)
graph_50.add_edge(node_01, node_03, 11)
graph_50.add_edge(node_01, node_02, 12)
graph_50.add_edge(node_02, node_02, 14)
graph_50.add_edge(node_01, node_01, 15)
graph_50.add_edge(node_03, node_03, 8)
graph_50.add_edge(node_03, node_00, 20)
graph_50.add_edge(node_01, node_00, 10)
graph_50.add_edge(node_00, node_00, 1)

"""
	GRAPH 51
"""

graph_51 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_51.add_node(node_00)
graph_51.add_node(node_01)
graph_51.add_node(node_02)
graph_51.add_node(node_03)
graph_51.add_node(node_04)

graph_51.add_edge(node_04, node_01, 2)
graph_51.add_edge(node_00, node_01, 3)
graph_51.add_edge(node_00, node_01, 8)
graph_51.add_edge(node_03, node_04, 2)
graph_51.add_edge(node_02, node_04, 8)
graph_51.add_edge(node_01, node_04, 11)
graph_51.add_edge(node_00, node_02, 13)
graph_51.add_edge(node_00, node_04, 14)
graph_51.add_edge(node_01, node_04, 16)
graph_51.add_edge(node_04, node_00, 11)

"""
	GRAPH 52
"""

graph_52 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_52.add_node(node_00)
graph_52.add_node(node_01)
graph_52.add_node(node_02)
graph_52.add_node(node_03)
graph_52.add_node(node_04)

graph_52.add_edge(node_00, node_02, 19)
graph_52.add_edge(node_04, node_01, 10)
graph_52.add_edge(node_03, node_04, 5)
graph_52.add_edge(node_01, node_01, 2)
graph_52.add_edge(node_00, node_04, 6)
graph_52.add_edge(node_02, node_03, 7)
graph_52.add_edge(node_04, node_00, 10)
graph_52.add_edge(node_01, node_03, 11)
graph_52.add_edge(node_04, node_04, 3)
graph_52.add_edge(node_04, node_04, 20)

"""
	GRAPH 53
"""

graph_53 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_53.add_node(node_00)
graph_53.add_node(node_01)
graph_53.add_node(node_02)
graph_53.add_node(node_03)
graph_53.add_node(node_04)

graph_53.add_edge(node_03, node_00, 10)
graph_53.add_edge(node_03, node_01, 3)
graph_53.add_edge(node_02, node_00, 2)
graph_53.add_edge(node_04, node_04, 1)
graph_53.add_edge(node_04, node_03, 10)
graph_53.add_edge(node_02, node_00, 13)
graph_53.add_edge(node_02, node_04, 10)
graph_53.add_edge(node_01, node_04, 7)
graph_53.add_edge(node_01, node_04, 3)
graph_53.add_edge(node_02, node_04, 18)

"""
	GRAPH 54
"""

graph_54 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_54.add_node(node_00)
graph_54.add_node(node_01)
graph_54.add_node(node_02)
graph_54.add_node(node_03)
graph_54.add_node(node_04)

graph_54.add_edge(node_03, node_01, 3)
graph_54.add_edge(node_01, node_01, 16)
graph_54.add_edge(node_00, node_02, 11)
graph_54.add_edge(node_03, node_01, 19)
graph_54.add_edge(node_02, node_01, 3)
graph_54.add_edge(node_04, node_02, 6)
graph_54.add_edge(node_04, node_01, 18)
graph_54.add_edge(node_00, node_04, 8)
graph_54.add_edge(node_00, node_04, 10)
graph_54.add_edge(node_01, node_01, 17)

"""
	GRAPH 55
"""

graph_55 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_55.add_node(node_00)
graph_55.add_node(node_01)
graph_55.add_node(node_02)
graph_55.add_node(node_03)
graph_55.add_node(node_04)

graph_55.add_edge(node_04, node_04, 20)
graph_55.add_edge(node_00, node_04, 12)
graph_55.add_edge(node_03, node_04, 18)
graph_55.add_edge(node_00, node_00, 14)
graph_55.add_edge(node_03, node_04, 12)
graph_55.add_edge(node_03, node_03, 6)
graph_55.add_edge(node_02, node_03, 11)
graph_55.add_edge(node_02, node_00, 8)
graph_55.add_edge(node_04, node_00, 10)
graph_55.add_edge(node_03, node_01, 8)

"""
	GRAPH 56
"""

graph_56 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_56.add_node(node_00)
graph_56.add_node(node_01)
graph_56.add_node(node_02)
graph_56.add_node(node_03)
graph_56.add_node(node_04)

graph_56.add_edge(node_03, node_02, 10)
graph_56.add_edge(node_01, node_00, 20)
graph_56.add_edge(node_01, node_03, 2)
graph_56.add_edge(node_01, node_02, 10)
graph_56.add_edge(node_03, node_01, 2)
graph_56.add_edge(node_04, node_02, 15)
graph_56.add_edge(node_02, node_02, 8)
graph_56.add_edge(node_00, node_01, 3)
graph_56.add_edge(node_01, node_04, 8)
graph_56.add_edge(node_03, node_03, 9)

"""
	GRAPH 57
"""

graph_57 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_57.add_node(node_00)
graph_57.add_node(node_01)
graph_57.add_node(node_02)
graph_57.add_node(node_03)
graph_57.add_node(node_04)

graph_57.add_edge(node_02, node_00, 13)
graph_57.add_edge(node_03, node_04, 12)
graph_57.add_edge(node_03, node_03, 13)
graph_57.add_edge(node_00, node_04, 16)
graph_57.add_edge(node_00, node_03, 16)
graph_57.add_edge(node_01, node_00, 19)
graph_57.add_edge(node_04, node_04, 5)
graph_57.add_edge(node_00, node_01, 3)
graph_57.add_edge(node_00, node_03, 3)
graph_57.add_edge(node_00, node_02, 20)

"""
	GRAPH 58
"""

graph_58 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_58.add_node(node_00)
graph_58.add_node(node_01)
graph_58.add_node(node_02)
graph_58.add_node(node_03)
graph_58.add_node(node_04)

graph_58.add_edge(node_00, node_03, 1)
graph_58.add_edge(node_00, node_03, 19)
graph_58.add_edge(node_02, node_03, 18)
graph_58.add_edge(node_03, node_02, 18)
graph_58.add_edge(node_01, node_03, 18)
graph_58.add_edge(node_04, node_04, 1)
graph_58.add_edge(node_00, node_02, 12)
graph_58.add_edge(node_02, node_02, 17)
graph_58.add_edge(node_03, node_04, 7)
graph_58.add_edge(node_03, node_00, 17)

"""
	GRAPH 59
"""

graph_59 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_59.add_node(node_00)
graph_59.add_node(node_01)
graph_59.add_node(node_02)
graph_59.add_node(node_03)
graph_59.add_node(node_04)

graph_59.add_edge(node_00, node_02, 8)
graph_59.add_edge(node_00, node_01, 18)
graph_59.add_edge(node_03, node_04, 1)
graph_59.add_edge(node_04, node_02, 3)
graph_59.add_edge(node_01, node_02, 10)
graph_59.add_edge(node_03, node_03, 15)
graph_59.add_edge(node_03, node_00, 4)
graph_59.add_edge(node_02, node_00, 15)
graph_59.add_edge(node_02, node_04, 9)
graph_59.add_edge(node_01, node_04, 6)

"""
	GRAPH 60
"""

graph_60 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_60.add_node(node_00)
graph_60.add_node(node_01)
graph_60.add_node(node_02)
graph_60.add_node(node_03)
graph_60.add_node(node_04)

graph_60.add_edge(node_01, node_02, 1)
graph_60.add_edge(node_04, node_01, 20)
graph_60.add_edge(node_00, node_03, 11)
graph_60.add_edge(node_00, node_02, 9)
graph_60.add_edge(node_03, node_00, 18)
graph_60.add_edge(node_01, node_03, 3)
graph_60.add_edge(node_02, node_01, 12)
graph_60.add_edge(node_02, node_02, 4)
graph_60.add_edge(node_03, node_02, 11)
graph_60.add_edge(node_04, node_04, 2)

"""
	GRAPH 61
"""

graph_61 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_61.add_node(node_00)
graph_61.add_node(node_01)
graph_61.add_node(node_02)
graph_61.add_node(node_03)
graph_61.add_node(node_04)

graph_61.add_edge(node_04, node_03, 10)
graph_61.add_edge(node_02, node_00, 18)
graph_61.add_edge(node_00, node_01, 6)
graph_61.add_edge(node_00, node_03, 3)
graph_61.add_edge(node_00, node_03, 7)
graph_61.add_edge(node_02, node_02, 10)
graph_61.add_edge(node_03, node_03, 5)
graph_61.add_edge(node_00, node_01, 18)
graph_61.add_edge(node_01, node_03, 17)
graph_61.add_edge(node_02, node_02, 14)

"""
	GRAPH 62
"""

graph_62 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_62.add_node(node_00)
graph_62.add_node(node_01)
graph_62.add_node(node_02)
graph_62.add_node(node_03)
graph_62.add_node(node_04)

graph_62.add_edge(node_04, node_02, 18)
graph_62.add_edge(node_04, node_03, 11)
graph_62.add_edge(node_04, node_03, 17)
graph_62.add_edge(node_00, node_00, 12)
graph_62.add_edge(node_02, node_00, 5)
graph_62.add_edge(node_00, node_00, 13)
graph_62.add_edge(node_01, node_03, 5)
graph_62.add_edge(node_02, node_03, 18)
graph_62.add_edge(node_03, node_00, 16)
graph_62.add_edge(node_01, node_01, 11)

"""
	GRAPH 63
"""

graph_63 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_63.add_node(node_00)
graph_63.add_node(node_01)
graph_63.add_node(node_02)
graph_63.add_node(node_03)
graph_63.add_node(node_04)

graph_63.add_edge(node_03, node_02, 3)
graph_63.add_edge(node_01, node_00, 10)
graph_63.add_edge(node_02, node_04, 19)
graph_63.add_edge(node_01, node_03, 14)
graph_63.add_edge(node_04, node_04, 11)
graph_63.add_edge(node_00, node_01, 14)
graph_63.add_edge(node_04, node_02, 3)
graph_63.add_edge(node_04, node_02, 1)
graph_63.add_edge(node_00, node_01, 3)
graph_63.add_edge(node_01, node_02, 2)

"""
	GRAPH 64
"""

graph_64 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_64.add_node(node_00)
graph_64.add_node(node_01)
graph_64.add_node(node_02)
graph_64.add_node(node_03)
graph_64.add_node(node_04)

graph_64.add_edge(node_03, node_02, 19)
graph_64.add_edge(node_00, node_03, 4)
graph_64.add_edge(node_01, node_04, 19)
graph_64.add_edge(node_04, node_03, 15)
graph_64.add_edge(node_00, node_00, 18)
graph_64.add_edge(node_01, node_02, 17)
graph_64.add_edge(node_03, node_03, 15)
graph_64.add_edge(node_03, node_01, 17)
graph_64.add_edge(node_00, node_02, 4)
graph_64.add_edge(node_04, node_02, 9)

"""
	GRAPH 65
"""

graph_65 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_65.add_node(node_00)
graph_65.add_node(node_01)
graph_65.add_node(node_02)
graph_65.add_node(node_03)
graph_65.add_node(node_04)

graph_65.add_edge(node_00, node_02, 3)
graph_65.add_edge(node_00, node_00, 4)
graph_65.add_edge(node_03, node_02, 1)
graph_65.add_edge(node_00, node_00, 7)
graph_65.add_edge(node_03, node_00, 1)
graph_65.add_edge(node_01, node_03, 13)
graph_65.add_edge(node_02, node_04, 19)
graph_65.add_edge(node_03, node_04, 11)
graph_65.add_edge(node_03, node_04, 8)
graph_65.add_edge(node_03, node_02, 14)

"""
	GRAPH 66
"""

graph_66 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_66.add_node(node_00)
graph_66.add_node(node_01)
graph_66.add_node(node_02)
graph_66.add_node(node_03)
graph_66.add_node(node_04)

graph_66.add_edge(node_01, node_01, 4)
graph_66.add_edge(node_04, node_00, 7)
graph_66.add_edge(node_00, node_02, 19)
graph_66.add_edge(node_02, node_00, 12)
graph_66.add_edge(node_01, node_04, 18)
graph_66.add_edge(node_02, node_01, 7)
graph_66.add_edge(node_00, node_03, 15)
graph_66.add_edge(node_04, node_02, 20)
graph_66.add_edge(node_00, node_02, 5)
graph_66.add_edge(node_00, node_03, 17)

"""
	GRAPH 67
"""

graph_67 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_67.add_node(node_00)
graph_67.add_node(node_01)
graph_67.add_node(node_02)
graph_67.add_node(node_03)
graph_67.add_node(node_04)

graph_67.add_edge(node_01, node_02, 3)
graph_67.add_edge(node_01, node_02, 19)
graph_67.add_edge(node_03, node_03, 9)
graph_67.add_edge(node_03, node_02, 14)
graph_67.add_edge(node_01, node_04, 16)
graph_67.add_edge(node_02, node_02, 13)
graph_67.add_edge(node_01, node_03, 11)
graph_67.add_edge(node_04, node_01, 6)
graph_67.add_edge(node_03, node_03, 6)
graph_67.add_edge(node_03, node_00, 18)

"""
	GRAPH 68
"""

graph_68 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_68.add_node(node_00)
graph_68.add_node(node_01)
graph_68.add_node(node_02)
graph_68.add_node(node_03)
graph_68.add_node(node_04)

graph_68.add_edge(node_01, node_04, 13)
graph_68.add_edge(node_00, node_01, 4)
graph_68.add_edge(node_00, node_04, 8)
graph_68.add_edge(node_02, node_00, 3)
graph_68.add_edge(node_04, node_00, 4)
graph_68.add_edge(node_02, node_04, 19)
graph_68.add_edge(node_03, node_04, 17)
graph_68.add_edge(node_04, node_02, 7)
graph_68.add_edge(node_01, node_03, 5)
graph_68.add_edge(node_00, node_02, 8)

"""
	GRAPH 69
"""

graph_69 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_69.add_node(node_00)
graph_69.add_node(node_01)
graph_69.add_node(node_02)
graph_69.add_node(node_03)
graph_69.add_node(node_04)

graph_69.add_edge(node_04, node_04, 4)
graph_69.add_edge(node_03, node_04, 2)
graph_69.add_edge(node_04, node_04, 19)
graph_69.add_edge(node_00, node_01, 14)
graph_69.add_edge(node_03, node_02, 4)
graph_69.add_edge(node_01, node_03, 13)
graph_69.add_edge(node_02, node_04, 18)
graph_69.add_edge(node_00, node_04, 19)
graph_69.add_edge(node_04, node_02, 19)
graph_69.add_edge(node_03, node_01, 16)

"""
	GRAPH 70
"""

graph_70 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_70.add_node(node_00)
graph_70.add_node(node_01)
graph_70.add_node(node_02)
graph_70.add_node(node_03)
graph_70.add_node(node_04)

graph_70.add_edge(node_00, node_00, 13)
graph_70.add_edge(node_00, node_04, 3)
graph_70.add_edge(node_02, node_04, 10)
graph_70.add_edge(node_01, node_00, 20)
graph_70.add_edge(node_01, node_02, 4)
graph_70.add_edge(node_01, node_01, 19)
graph_70.add_edge(node_00, node_00, 3)
graph_70.add_edge(node_04, node_02, 5)
graph_70.add_edge(node_02, node_00, 18)
graph_70.add_edge(node_04, node_01, 19)

"""
	GRAPH 71
"""

graph_71 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_71.add_node(node_00)
graph_71.add_node(node_01)
graph_71.add_node(node_02)
graph_71.add_node(node_03)
graph_71.add_node(node_04)

graph_71.add_edge(node_03, node_03, 5)
graph_71.add_edge(node_03, node_03, 19)
graph_71.add_edge(node_02, node_04, 19)
graph_71.add_edge(node_01, node_01, 19)
graph_71.add_edge(node_04, node_01, 6)
graph_71.add_edge(node_02, node_00, 20)
graph_71.add_edge(node_00, node_00, 11)
graph_71.add_edge(node_00, node_03, 17)
graph_71.add_edge(node_03, node_04, 18)
graph_71.add_edge(node_03, node_00, 1)

"""
	GRAPH 72
"""

graph_72 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_72.add_node(node_00)
graph_72.add_node(node_01)
graph_72.add_node(node_02)
graph_72.add_node(node_03)
graph_72.add_node(node_04)

graph_72.add_edge(node_02, node_02, 17)
graph_72.add_edge(node_03, node_03, 9)
graph_72.add_edge(node_03, node_01, 18)
graph_72.add_edge(node_01, node_02, 1)
graph_72.add_edge(node_03, node_01, 9)
graph_72.add_edge(node_01, node_01, 5)
graph_72.add_edge(node_04, node_02, 8)
graph_72.add_edge(node_04, node_04, 7)
graph_72.add_edge(node_01, node_04, 4)
graph_72.add_edge(node_03, node_02, 12)

"""
	GRAPH 73
"""

graph_73 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_73.add_node(node_00)
graph_73.add_node(node_01)
graph_73.add_node(node_02)
graph_73.add_node(node_03)
graph_73.add_node(node_04)

graph_73.add_edge(node_01, node_04, 15)
graph_73.add_edge(node_00, node_02, 6)
graph_73.add_edge(node_02, node_02, 15)
graph_73.add_edge(node_01, node_03, 18)
graph_73.add_edge(node_02, node_03, 3)
graph_73.add_edge(node_02, node_04, 14)
graph_73.add_edge(node_01, node_03, 6)
graph_73.add_edge(node_04, node_00, 4)
graph_73.add_edge(node_02, node_02, 1)
graph_73.add_edge(node_03, node_00, 6)

"""
	GRAPH 74
"""

graph_74 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_74.add_node(node_00)
graph_74.add_node(node_01)
graph_74.add_node(node_02)
graph_74.add_node(node_03)
graph_74.add_node(node_04)

graph_74.add_edge(node_02, node_01, 4)
graph_74.add_edge(node_04, node_03, 3)
graph_74.add_edge(node_01, node_00, 4)
graph_74.add_edge(node_04, node_00, 15)
graph_74.add_edge(node_00, node_03, 19)
graph_74.add_edge(node_04, node_02, 3)
graph_74.add_edge(node_01, node_00, 8)
graph_74.add_edge(node_02, node_03, 14)
graph_74.add_edge(node_04, node_03, 20)
graph_74.add_edge(node_01, node_03, 19)

"""
	GRAPH 75
"""

graph_75 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_75.add_node(node_00)
graph_75.add_node(node_01)
graph_75.add_node(node_02)
graph_75.add_node(node_03)
graph_75.add_node(node_04)

graph_75.add_edge(node_01, node_00, 14)
graph_75.add_edge(node_02, node_02, 11)
graph_75.add_edge(node_03, node_02, 6)
graph_75.add_edge(node_02, node_02, 3)
graph_75.add_edge(node_03, node_01, 18)
graph_75.add_edge(node_04, node_04, 10)
graph_75.add_edge(node_00, node_00, 18)
graph_75.add_edge(node_04, node_03, 12)
graph_75.add_edge(node_04, node_02, 17)
graph_75.add_edge(node_03, node_04, 9)

"""
	GRAPH 76
"""

graph_76 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_76.add_node(node_00)
graph_76.add_node(node_01)
graph_76.add_node(node_02)
graph_76.add_node(node_03)
graph_76.add_node(node_04)

graph_76.add_edge(node_00, node_04, 18)
graph_76.add_edge(node_04, node_02, 2)
graph_76.add_edge(node_03, node_00, 16)
graph_76.add_edge(node_01, node_03, 12)
graph_76.add_edge(node_00, node_00, 11)
graph_76.add_edge(node_02, node_04, 13)
graph_76.add_edge(node_03, node_02, 2)
graph_76.add_edge(node_04, node_04, 3)
graph_76.add_edge(node_02, node_03, 3)
graph_76.add_edge(node_04, node_00, 12)

"""
	GRAPH 77
"""

graph_77 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_77.add_node(node_00)
graph_77.add_node(node_01)
graph_77.add_node(node_02)
graph_77.add_node(node_03)
graph_77.add_node(node_04)

graph_77.add_edge(node_03, node_02, 2)
graph_77.add_edge(node_03, node_04, 6)
graph_77.add_edge(node_01, node_00, 7)
graph_77.add_edge(node_02, node_03, 2)
graph_77.add_edge(node_02, node_04, 14)
graph_77.add_edge(node_04, node_02, 14)
graph_77.add_edge(node_01, node_00, 10)
graph_77.add_edge(node_02, node_03, 16)
graph_77.add_edge(node_03, node_01, 5)
graph_77.add_edge(node_01, node_00, 10)

"""
	GRAPH 78
"""

graph_78 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_78.add_node(node_00)
graph_78.add_node(node_01)
graph_78.add_node(node_02)
graph_78.add_node(node_03)
graph_78.add_node(node_04)

graph_78.add_edge(node_02, node_00, 1)
graph_78.add_edge(node_00, node_00, 5)
graph_78.add_edge(node_03, node_01, 20)
graph_78.add_edge(node_00, node_01, 7)
graph_78.add_edge(node_00, node_00, 10)
graph_78.add_edge(node_00, node_04, 20)
graph_78.add_edge(node_03, node_01, 4)
graph_78.add_edge(node_03, node_04, 3)
graph_78.add_edge(node_01, node_03, 2)
graph_78.add_edge(node_00, node_04, 16)

"""
	GRAPH 79
"""

graph_79 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_79.add_node(node_00)
graph_79.add_node(node_01)
graph_79.add_node(node_02)
graph_79.add_node(node_03)
graph_79.add_node(node_04)

graph_79.add_edge(node_02, node_04, 4)
graph_79.add_edge(node_03, node_01, 18)
graph_79.add_edge(node_00, node_02, 19)
graph_79.add_edge(node_03, node_02, 4)
graph_79.add_edge(node_00, node_04, 13)
graph_79.add_edge(node_04, node_00, 7)
graph_79.add_edge(node_04, node_00, 17)
graph_79.add_edge(node_01, node_01, 10)
graph_79.add_edge(node_01, node_01, 1)
graph_79.add_edge(node_01, node_01, 8)

"""
	GRAPH 80
"""

graph_80 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_80.add_node(node_00)
graph_80.add_node(node_01)
graph_80.add_node(node_02)
graph_80.add_node(node_03)
graph_80.add_node(node_04)

graph_80.add_edge(node_00, node_04, 6)
graph_80.add_edge(node_01, node_04, 9)
graph_80.add_edge(node_00, node_02, 8)
graph_80.add_edge(node_04, node_03, 11)
graph_80.add_edge(node_01, node_03, 13)
graph_80.add_edge(node_03, node_00, 8)
graph_80.add_edge(node_02, node_04, 3)
graph_80.add_edge(node_03, node_00, 7)
graph_80.add_edge(node_01, node_03, 17)
graph_80.add_edge(node_03, node_01, 15)

"""
	GRAPH 81
"""

graph_81 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_81.add_node(node_00)
graph_81.add_node(node_01)
graph_81.add_node(node_02)
graph_81.add_node(node_03)
graph_81.add_node(node_04)

graph_81.add_edge(node_04, node_03, 10)
graph_81.add_edge(node_04, node_01, 17)
graph_81.add_edge(node_00, node_04, 16)
graph_81.add_edge(node_02, node_01, 12)
graph_81.add_edge(node_00, node_03, 9)
graph_81.add_edge(node_02, node_04, 1)
graph_81.add_edge(node_04, node_01, 16)
graph_81.add_edge(node_02, node_03, 7)
graph_81.add_edge(node_04, node_04, 9)
graph_81.add_edge(node_01, node_03, 15)

"""
	GRAPH 82
"""

graph_82 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_82.add_node(node_00)
graph_82.add_node(node_01)
graph_82.add_node(node_02)
graph_82.add_node(node_03)
graph_82.add_node(node_04)

graph_82.add_edge(node_04, node_00, 18)
graph_82.add_edge(node_04, node_02, 17)
graph_82.add_edge(node_02, node_02, 6)
graph_82.add_edge(node_02, node_03, 15)
graph_82.add_edge(node_02, node_03, 5)
graph_82.add_edge(node_03, node_04, 14)
graph_82.add_edge(node_02, node_03, 6)
graph_82.add_edge(node_01, node_00, 8)
graph_82.add_edge(node_01, node_04, 16)
graph_82.add_edge(node_02, node_03, 3)

"""
	GRAPH 83
"""

graph_83 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_83.add_node(node_00)
graph_83.add_node(node_01)
graph_83.add_node(node_02)
graph_83.add_node(node_03)
graph_83.add_node(node_04)

graph_83.add_edge(node_00, node_04, 12)
graph_83.add_edge(node_00, node_00, 3)
graph_83.add_edge(node_04, node_00, 2)
graph_83.add_edge(node_01, node_02, 9)
graph_83.add_edge(node_04, node_03, 19)
graph_83.add_edge(node_04, node_01, 8)
graph_83.add_edge(node_00, node_04, 4)
graph_83.add_edge(node_03, node_00, 2)
graph_83.add_edge(node_03, node_01, 6)
graph_83.add_edge(node_02, node_03, 16)

"""
	GRAPH 84
"""

graph_84 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_84.add_node(node_00)
graph_84.add_node(node_01)
graph_84.add_node(node_02)
graph_84.add_node(node_03)
graph_84.add_node(node_04)

graph_84.add_edge(node_00, node_04, 11)
graph_84.add_edge(node_02, node_02, 16)
graph_84.add_edge(node_02, node_04, 2)
graph_84.add_edge(node_01, node_01, 18)
graph_84.add_edge(node_04, node_00, 12)
graph_84.add_edge(node_04, node_02, 15)
graph_84.add_edge(node_03, node_00, 11)
graph_84.add_edge(node_00, node_01, 15)
graph_84.add_edge(node_04, node_04, 13)
graph_84.add_edge(node_02, node_04, 1)

"""
	GRAPH 85
"""

graph_85 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_85.add_node(node_00)
graph_85.add_node(node_01)
graph_85.add_node(node_02)
graph_85.add_node(node_03)
graph_85.add_node(node_04)

graph_85.add_edge(node_02, node_00, 3)
graph_85.add_edge(node_04, node_03, 10)
graph_85.add_edge(node_00, node_01, 20)
graph_85.add_edge(node_02, node_02, 2)
graph_85.add_edge(node_00, node_02, 12)
graph_85.add_edge(node_00, node_03, 16)
graph_85.add_edge(node_03, node_00, 13)
graph_85.add_edge(node_03, node_03, 8)
graph_85.add_edge(node_03, node_03, 15)
graph_85.add_edge(node_03, node_04, 19)

"""
	GRAPH 86
"""

graph_86 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_86.add_node(node_00)
graph_86.add_node(node_01)
graph_86.add_node(node_02)
graph_86.add_node(node_03)
graph_86.add_node(node_04)

graph_86.add_edge(node_00, node_04, 5)
graph_86.add_edge(node_02, node_02, 3)
graph_86.add_edge(node_04, node_00, 12)
graph_86.add_edge(node_02, node_03, 5)
graph_86.add_edge(node_04, node_01, 5)
graph_86.add_edge(node_02, node_03, 1)
graph_86.add_edge(node_03, node_01, 17)
graph_86.add_edge(node_02, node_03, 14)
graph_86.add_edge(node_04, node_00, 7)
graph_86.add_edge(node_01, node_01, 10)

"""
	GRAPH 87
"""

graph_87 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_87.add_node(node_00)
graph_87.add_node(node_01)
graph_87.add_node(node_02)
graph_87.add_node(node_03)
graph_87.add_node(node_04)

graph_87.add_edge(node_04, node_03, 17)
graph_87.add_edge(node_01, node_00, 3)
graph_87.add_edge(node_01, node_02, 5)
graph_87.add_edge(node_00, node_04, 18)
graph_87.add_edge(node_00, node_01, 10)
graph_87.add_edge(node_04, node_00, 7)
graph_87.add_edge(node_00, node_02, 7)
graph_87.add_edge(node_01, node_01, 18)
graph_87.add_edge(node_02, node_03, 3)
graph_87.add_edge(node_01, node_00, 18)

"""
	GRAPH 88
"""

graph_88 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_88.add_node(node_00)
graph_88.add_node(node_01)
graph_88.add_node(node_02)
graph_88.add_node(node_03)
graph_88.add_node(node_04)

graph_88.add_edge(node_00, node_04, 18)
graph_88.add_edge(node_04, node_01, 3)
graph_88.add_edge(node_02, node_00, 12)
graph_88.add_edge(node_01, node_01, 4)
graph_88.add_edge(node_04, node_01, 16)
graph_88.add_edge(node_03, node_04, 7)
graph_88.add_edge(node_04, node_02, 19)
graph_88.add_edge(node_03, node_03, 12)
graph_88.add_edge(node_00, node_03, 17)
graph_88.add_edge(node_01, node_02, 7)

"""
	GRAPH 89
"""

graph_89 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_89.add_node(node_00)
graph_89.add_node(node_01)
graph_89.add_node(node_02)
graph_89.add_node(node_03)
graph_89.add_node(node_04)

graph_89.add_edge(node_02, node_01, 14)
graph_89.add_edge(node_04, node_03, 18)
graph_89.add_edge(node_01, node_00, 18)
graph_89.add_edge(node_04, node_01, 9)
graph_89.add_edge(node_03, node_04, 7)
graph_89.add_edge(node_00, node_04, 17)
graph_89.add_edge(node_04, node_00, 13)
graph_89.add_edge(node_02, node_01, 5)
graph_89.add_edge(node_00, node_01, 5)
graph_89.add_edge(node_02, node_02, 14)

"""
	GRAPH 90
"""

graph_90 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_90.add_node(node_00)
graph_90.add_node(node_01)
graph_90.add_node(node_02)
graph_90.add_node(node_03)
graph_90.add_node(node_04)

graph_90.add_edge(node_02, node_01, 7)
graph_90.add_edge(node_00, node_03, 2)
graph_90.add_edge(node_04, node_00, 6)
graph_90.add_edge(node_02, node_03, 3)
graph_90.add_edge(node_03, node_02, 2)
graph_90.add_edge(node_03, node_04, 9)
graph_90.add_edge(node_04, node_02, 5)
graph_90.add_edge(node_00, node_00, 9)
graph_90.add_edge(node_04, node_04, 18)
graph_90.add_edge(node_04, node_02, 9)

"""
	GRAPH 91
"""

graph_91 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_91.add_node(node_00)
graph_91.add_node(node_01)
graph_91.add_node(node_02)
graph_91.add_node(node_03)
graph_91.add_node(node_04)

graph_91.add_edge(node_03, node_02, 16)
graph_91.add_edge(node_00, node_00, 18)
graph_91.add_edge(node_00, node_04, 4)
graph_91.add_edge(node_02, node_02, 3)
graph_91.add_edge(node_03, node_02, 20)
graph_91.add_edge(node_03, node_00, 10)
graph_91.add_edge(node_02, node_01, 18)
graph_91.add_edge(node_04, node_02, 2)
graph_91.add_edge(node_01, node_03, 18)
graph_91.add_edge(node_04, node_04, 10)

"""
	GRAPH 92
"""

graph_92 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_92.add_node(node_00)
graph_92.add_node(node_01)
graph_92.add_node(node_02)
graph_92.add_node(node_03)
graph_92.add_node(node_04)

graph_92.add_edge(node_01, node_00, 3)
graph_92.add_edge(node_02, node_02, 4)
graph_92.add_edge(node_00, node_00, 5)
graph_92.add_edge(node_01, node_04, 8)
graph_92.add_edge(node_04, node_01, 13)
graph_92.add_edge(node_02, node_00, 13)
graph_92.add_edge(node_01, node_00, 13)
graph_92.add_edge(node_04, node_00, 8)
graph_92.add_edge(node_01, node_02, 13)
graph_92.add_edge(node_04, node_01, 9)

"""
	GRAPH 93
"""

graph_93 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_93.add_node(node_00)
graph_93.add_node(node_01)
graph_93.add_node(node_02)
graph_93.add_node(node_03)
graph_93.add_node(node_04)

graph_93.add_edge(node_01, node_02, 8)
graph_93.add_edge(node_03, node_00, 2)
graph_93.add_edge(node_03, node_04, 9)
graph_93.add_edge(node_02, node_04, 4)
graph_93.add_edge(node_02, node_02, 4)
graph_93.add_edge(node_01, node_00, 10)
graph_93.add_edge(node_00, node_02, 3)
graph_93.add_edge(node_04, node_01, 13)
graph_93.add_edge(node_00, node_03, 1)
graph_93.add_edge(node_02, node_00, 7)

"""
	GRAPH 94
"""

graph_94 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_94.add_node(node_00)
graph_94.add_node(node_01)
graph_94.add_node(node_02)
graph_94.add_node(node_03)
graph_94.add_node(node_04)

graph_94.add_edge(node_00, node_01, 1)
graph_94.add_edge(node_02, node_04, 8)
graph_94.add_edge(node_00, node_00, 7)
graph_94.add_edge(node_01, node_01, 10)
graph_94.add_edge(node_01, node_04, 14)
graph_94.add_edge(node_00, node_02, 8)
graph_94.add_edge(node_02, node_01, 6)
graph_94.add_edge(node_03, node_04, 16)
graph_94.add_edge(node_01, node_02, 2)
graph_94.add_edge(node_03, node_04, 20)

"""
	GRAPH 95
"""

graph_95 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_95.add_node(node_00)
graph_95.add_node(node_01)
graph_95.add_node(node_02)
graph_95.add_node(node_03)
graph_95.add_node(node_04)

graph_95.add_edge(node_00, node_04, 18)
graph_95.add_edge(node_01, node_02, 7)
graph_95.add_edge(node_04, node_00, 2)
graph_95.add_edge(node_00, node_02, 2)
graph_95.add_edge(node_04, node_02, 18)
graph_95.add_edge(node_02, node_00, 1)
graph_95.add_edge(node_02, node_04, 7)
graph_95.add_edge(node_04, node_04, 5)
graph_95.add_edge(node_03, node_00, 15)
graph_95.add_edge(node_01, node_00, 14)

"""
	GRAPH 96
"""

graph_96 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_96.add_node(node_00)
graph_96.add_node(node_01)
graph_96.add_node(node_02)
graph_96.add_node(node_03)
graph_96.add_node(node_04)

graph_96.add_edge(node_04, node_02, 14)
graph_96.add_edge(node_00, node_00, 16)
graph_96.add_edge(node_00, node_02, 1)
graph_96.add_edge(node_01, node_03, 6)
graph_96.add_edge(node_03, node_00, 16)
graph_96.add_edge(node_02, node_02, 11)
graph_96.add_edge(node_02, node_00, 12)
graph_96.add_edge(node_04, node_00, 3)
graph_96.add_edge(node_04, node_00, 2)
graph_96.add_edge(node_01, node_01, 13)

"""
	GRAPH 97
"""

graph_97 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_97.add_node(node_00)
graph_97.add_node(node_01)
graph_97.add_node(node_02)
graph_97.add_node(node_03)
graph_97.add_node(node_04)

graph_97.add_edge(node_02, node_01, 18)
graph_97.add_edge(node_04, node_04, 3)
graph_97.add_edge(node_04, node_02, 17)
graph_97.add_edge(node_02, node_01, 2)
graph_97.add_edge(node_00, node_02, 15)
graph_97.add_edge(node_00, node_01, 13)
graph_97.add_edge(node_04, node_03, 13)
graph_97.add_edge(node_01, node_02, 11)
graph_97.add_edge(node_03, node_01, 8)
graph_97.add_edge(node_03, node_01, 16)

"""
	GRAPH 98
"""

graph_98 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_98.add_node(node_00)
graph_98.add_node(node_01)
graph_98.add_node(node_02)
graph_98.add_node(node_03)
graph_98.add_node(node_04)

graph_98.add_edge(node_02, node_03, 2)
graph_98.add_edge(node_00, node_04, 11)
graph_98.add_edge(node_03, node_04, 4)
graph_98.add_edge(node_03, node_00, 2)
graph_98.add_edge(node_00, node_01, 5)
graph_98.add_edge(node_03, node_02, 6)
graph_98.add_edge(node_01, node_04, 13)
graph_98.add_edge(node_01, node_02, 3)
graph_98.add_edge(node_03, node_02, 16)
graph_98.add_edge(node_03, node_03, 7)

"""
	GRAPH 99
"""

graph_99 = Graph(False)

node_00 = Node(0)
node_01 = Node(1)
node_02 = Node(2)
node_03 = Node(3)
node_04 = Node(4)

graph_99.add_node(node_00)
graph_99.add_node(node_01)
graph_99.add_node(node_02)
graph_99.add_node(node_03)
graph_99.add_node(node_04)

graph_99.add_edge(node_04, node_02, 17)
graph_99.add_edge(node_03, node_00, 18)
graph_99.add_edge(node_01, node_01, 6)
graph_99.add_edge(node_03, node_04, 12)
graph_99.add_edge(node_03, node_03, 7)
graph_99.add_edge(node_00, node_02, 15)
graph_99.add_edge(node_00, node_02, 2)
graph_99.add_edge(node_04, node_00, 7)
graph_99.add_edge(node_00, node_04, 13)
graph_99.add_edge(node_04, node_01, 5)

graphs = [graph_00, graph_01, graph_02, graph_03, graph_04, graph_05, graph_06, graph_07, graph_08, graph_09, graph_10,
          graph_11, graph_12, graph_13, graph_14, graph_15, graph_16, graph_17, graph_18, graph_19, graph_20, graph_21,
          graph_22, graph_23, graph_24, graph_25, graph_26, graph_27, graph_28, graph_29, graph_30, graph_31, graph_32,
          graph_33, graph_34, graph_35, graph_36, graph_37, graph_38, graph_39, graph_40, graph_41, graph_42, graph_43,
          graph_44, graph_45, graph_46, graph_47, graph_48, graph_49, graph_50, graph_51, graph_52, graph_53, graph_54,
          graph_55, graph_56, graph_57, graph_58, graph_59, graph_60, graph_61, graph_62, graph_63, graph_64, graph_65,
          graph_66, graph_67, graph_68, graph_69, graph_70, graph_71, graph_72, graph_73, graph_74, graph_75, graph_76,
          graph_77, graph_78, graph_79, graph_80, graph_81, graph_82, graph_83, graph_84, graph_85, graph_86, graph_87,
          graph_88, graph_89, graph_90, graph_91, graph_92, graph_93, graph_94, graph_95, graph_96, graph_97, graph_98,
          graph_99]
