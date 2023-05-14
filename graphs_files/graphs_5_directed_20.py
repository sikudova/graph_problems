from graph_class import Node, Graph

# 100 directed graphs with 5 nodes, 20 edges


"""
	GRAPH 00
"""

graph_00 = Graph(True)

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

graph_00.add_edge(node_04, node_02, 18)
graph_00.add_edge(node_01, node_02, 2)
graph_00.add_edge(node_03, node_01, 2)
graph_00.add_edge(node_00, node_02, 11)
graph_00.add_edge(node_02, node_01, 16)
graph_00.add_edge(node_01, node_01, 9)
graph_00.add_edge(node_02, node_04, 10)
graph_00.add_edge(node_03, node_02, 7)
graph_00.add_edge(node_01, node_02, 16)
graph_00.add_edge(node_00, node_02, 9)
graph_00.add_edge(node_04, node_03, 17)
graph_00.add_edge(node_03, node_01, 16)
graph_00.add_edge(node_04, node_04, 8)
graph_00.add_edge(node_02, node_04, 13)
graph_00.add_edge(node_03, node_01, 15)
graph_00.add_edge(node_02, node_04, 12)
graph_00.add_edge(node_02, node_02, 1)
graph_00.add_edge(node_04, node_01, 20)
graph_00.add_edge(node_03, node_01, 6)
graph_00.add_edge(node_00, node_02, 13)

"""
	GRAPH 01
"""

graph_01 = Graph(True)

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

graph_01.add_edge(node_03, node_02, 2)
graph_01.add_edge(node_02, node_03, 4)
graph_01.add_edge(node_04, node_03, 2)
graph_01.add_edge(node_00, node_04, 10)
graph_01.add_edge(node_01, node_02, 7)
graph_01.add_edge(node_01, node_00, 11)
graph_01.add_edge(node_03, node_01, 18)
graph_01.add_edge(node_02, node_03, 16)
graph_01.add_edge(node_01, node_00, 9)
graph_01.add_edge(node_01, node_01, 12)
graph_01.add_edge(node_04, node_03, 17)
graph_01.add_edge(node_00, node_01, 8)
graph_01.add_edge(node_03, node_04, 3)
graph_01.add_edge(node_03, node_00, 13)
graph_01.add_edge(node_01, node_01, 13)
graph_01.add_edge(node_00, node_02, 18)
graph_01.add_edge(node_04, node_03, 7)
graph_01.add_edge(node_04, node_02, 6)
graph_01.add_edge(node_02, node_00, 5)
graph_01.add_edge(node_03, node_03, 6)

"""
	GRAPH 02
"""

graph_02 = Graph(True)

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

graph_02.add_edge(node_02, node_01, 13)
graph_02.add_edge(node_00, node_04, 16)
graph_02.add_edge(node_01, node_00, 12)
graph_02.add_edge(node_03, node_03, 5)
graph_02.add_edge(node_00, node_00, 2)
graph_02.add_edge(node_02, node_00, 14)
graph_02.add_edge(node_04, node_02, 5)
graph_02.add_edge(node_03, node_00, 3)
graph_02.add_edge(node_00, node_02, 17)
graph_02.add_edge(node_00, node_04, 19)
graph_02.add_edge(node_04, node_00, 13)
graph_02.add_edge(node_01, node_02, 15)
graph_02.add_edge(node_03, node_03, 12)
graph_02.add_edge(node_04, node_02, 11)
graph_02.add_edge(node_00, node_00, 14)
graph_02.add_edge(node_04, node_03, 6)
graph_02.add_edge(node_00, node_01, 13)
graph_02.add_edge(node_00, node_01, 17)
graph_02.add_edge(node_02, node_02, 12)
graph_02.add_edge(node_03, node_01, 5)

"""
	GRAPH 03
"""

graph_03 = Graph(True)

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

graph_03.add_edge(node_04, node_00, 7)
graph_03.add_edge(node_03, node_02, 4)
graph_03.add_edge(node_02, node_00, 4)
graph_03.add_edge(node_03, node_01, 19)
graph_03.add_edge(node_04, node_03, 4)
graph_03.add_edge(node_03, node_01, 14)
graph_03.add_edge(node_02, node_03, 11)
graph_03.add_edge(node_04, node_00, 18)
graph_03.add_edge(node_02, node_02, 10)
graph_03.add_edge(node_03, node_00, 15)
graph_03.add_edge(node_00, node_04, 13)
graph_03.add_edge(node_04, node_02, 7)
graph_03.add_edge(node_04, node_04, 19)
graph_03.add_edge(node_02, node_00, 7)
graph_03.add_edge(node_01, node_01, 11)
graph_03.add_edge(node_03, node_03, 8)
graph_03.add_edge(node_03, node_01, 15)
graph_03.add_edge(node_00, node_03, 11)
graph_03.add_edge(node_04, node_04, 13)
graph_03.add_edge(node_01, node_00, 4)

"""
	GRAPH 04
"""

graph_04 = Graph(True)

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

graph_04.add_edge(node_01, node_03, 12)
graph_04.add_edge(node_01, node_01, 11)
graph_04.add_edge(node_01, node_04, 4)
graph_04.add_edge(node_03, node_04, 16)
graph_04.add_edge(node_01, node_00, 7)
graph_04.add_edge(node_01, node_00, 15)
graph_04.add_edge(node_02, node_03, 17)
graph_04.add_edge(node_02, node_04, 17)
graph_04.add_edge(node_04, node_01, 7)
graph_04.add_edge(node_03, node_00, 4)
graph_04.add_edge(node_00, node_01, 5)
graph_04.add_edge(node_03, node_04, 1)
graph_04.add_edge(node_02, node_03, 18)
graph_04.add_edge(node_04, node_04, 8)
graph_04.add_edge(node_02, node_00, 10)
graph_04.add_edge(node_02, node_03, 9)
graph_04.add_edge(node_00, node_00, 11)
graph_04.add_edge(node_00, node_03, 16)
graph_04.add_edge(node_02, node_02, 14)
graph_04.add_edge(node_00, node_04, 16)

"""
	GRAPH 05
"""

graph_05 = Graph(True)

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

graph_05.add_edge(node_04, node_01, 6)
graph_05.add_edge(node_03, node_04, 6)
graph_05.add_edge(node_01, node_00, 4)
graph_05.add_edge(node_01, node_01, 12)
graph_05.add_edge(node_02, node_02, 10)
graph_05.add_edge(node_00, node_03, 20)
graph_05.add_edge(node_00, node_00, 2)
graph_05.add_edge(node_03, node_02, 18)
graph_05.add_edge(node_03, node_04, 4)
graph_05.add_edge(node_03, node_03, 15)
graph_05.add_edge(node_00, node_04, 5)
graph_05.add_edge(node_01, node_02, 2)
graph_05.add_edge(node_03, node_03, 16)
graph_05.add_edge(node_01, node_04, 8)
graph_05.add_edge(node_04, node_00, 20)
graph_05.add_edge(node_02, node_01, 3)
graph_05.add_edge(node_01, node_03, 8)
graph_05.add_edge(node_02, node_00, 15)
graph_05.add_edge(node_01, node_00, 19)
graph_05.add_edge(node_04, node_03, 9)

"""
	GRAPH 06
"""

graph_06 = Graph(True)

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

graph_06.add_edge(node_02, node_02, 1)
graph_06.add_edge(node_02, node_01, 20)
graph_06.add_edge(node_03, node_00, 8)
graph_06.add_edge(node_03, node_02, 1)
graph_06.add_edge(node_02, node_03, 14)
graph_06.add_edge(node_01, node_00, 19)
graph_06.add_edge(node_04, node_02, 19)
graph_06.add_edge(node_03, node_04, 9)
graph_06.add_edge(node_01, node_00, 2)
graph_06.add_edge(node_02, node_04, 15)
graph_06.add_edge(node_03, node_01, 16)
graph_06.add_edge(node_04, node_04, 14)
graph_06.add_edge(node_01, node_00, 11)
graph_06.add_edge(node_00, node_04, 7)
graph_06.add_edge(node_01, node_00, 12)
graph_06.add_edge(node_04, node_01, 5)
graph_06.add_edge(node_00, node_01, 16)
graph_06.add_edge(node_04, node_03, 7)
graph_06.add_edge(node_02, node_01, 1)
graph_06.add_edge(node_03, node_02, 6)

"""
	GRAPH 07
"""

graph_07 = Graph(True)

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

graph_07.add_edge(node_02, node_02, 11)
graph_07.add_edge(node_00, node_00, 7)
graph_07.add_edge(node_04, node_01, 10)
graph_07.add_edge(node_02, node_04, 17)
graph_07.add_edge(node_04, node_00, 15)
graph_07.add_edge(node_01, node_04, 7)
graph_07.add_edge(node_01, node_03, 8)
graph_07.add_edge(node_03, node_02, 6)
graph_07.add_edge(node_02, node_02, 8)
graph_07.add_edge(node_04, node_04, 19)
graph_07.add_edge(node_02, node_04, 9)
graph_07.add_edge(node_02, node_03, 10)
graph_07.add_edge(node_04, node_03, 9)
graph_07.add_edge(node_00, node_04, 15)
graph_07.add_edge(node_01, node_00, 12)
graph_07.add_edge(node_01, node_04, 5)
graph_07.add_edge(node_02, node_04, 8)
graph_07.add_edge(node_04, node_00, 12)
graph_07.add_edge(node_02, node_02, 19)
graph_07.add_edge(node_04, node_00, 2)

"""
	GRAPH 08
"""

graph_08 = Graph(True)

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

graph_08.add_edge(node_00, node_03, 1)
graph_08.add_edge(node_02, node_04, 10)
graph_08.add_edge(node_04, node_01, 3)
graph_08.add_edge(node_00, node_03, 18)
graph_08.add_edge(node_01, node_02, 14)
graph_08.add_edge(node_03, node_03, 9)
graph_08.add_edge(node_01, node_03, 15)
graph_08.add_edge(node_04, node_01, 5)
graph_08.add_edge(node_03, node_02, 11)
graph_08.add_edge(node_03, node_03, 1)
graph_08.add_edge(node_00, node_03, 4)
graph_08.add_edge(node_04, node_02, 19)
graph_08.add_edge(node_03, node_02, 9)
graph_08.add_edge(node_04, node_01, 17)
graph_08.add_edge(node_01, node_04, 4)
graph_08.add_edge(node_01, node_01, 7)
graph_08.add_edge(node_00, node_01, 13)
graph_08.add_edge(node_00, node_01, 17)
graph_08.add_edge(node_01, node_03, 5)
graph_08.add_edge(node_03, node_03, 13)

"""
	GRAPH 09
"""

graph_09 = Graph(True)

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

graph_09.add_edge(node_00, node_02, 5)
graph_09.add_edge(node_02, node_00, 15)
graph_09.add_edge(node_00, node_03, 5)
graph_09.add_edge(node_03, node_04, 17)
graph_09.add_edge(node_01, node_00, 18)
graph_09.add_edge(node_01, node_01, 3)
graph_09.add_edge(node_01, node_03, 5)
graph_09.add_edge(node_04, node_02, 5)
graph_09.add_edge(node_03, node_02, 16)
graph_09.add_edge(node_04, node_00, 18)
graph_09.add_edge(node_01, node_04, 7)
graph_09.add_edge(node_00, node_04, 14)
graph_09.add_edge(node_01, node_03, 19)
graph_09.add_edge(node_04, node_02, 16)
graph_09.add_edge(node_03, node_03, 19)
graph_09.add_edge(node_03, node_04, 10)
graph_09.add_edge(node_03, node_04, 16)
graph_09.add_edge(node_01, node_01, 2)
graph_09.add_edge(node_02, node_02, 12)
graph_09.add_edge(node_02, node_03, 14)

"""
	GRAPH 10
"""

graph_10 = Graph(True)

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

graph_10.add_edge(node_00, node_04, 13)
graph_10.add_edge(node_02, node_03, 7)
graph_10.add_edge(node_01, node_03, 3)
graph_10.add_edge(node_01, node_03, 20)
graph_10.add_edge(node_04, node_04, 13)
graph_10.add_edge(node_03, node_02, 5)
graph_10.add_edge(node_02, node_00, 11)
graph_10.add_edge(node_04, node_04, 15)
graph_10.add_edge(node_00, node_04, 1)
graph_10.add_edge(node_04, node_04, 11)
graph_10.add_edge(node_03, node_01, 1)
graph_10.add_edge(node_03, node_03, 20)
graph_10.add_edge(node_01, node_03, 18)
graph_10.add_edge(node_03, node_04, 5)
graph_10.add_edge(node_00, node_02, 9)
graph_10.add_edge(node_00, node_01, 9)
graph_10.add_edge(node_00, node_01, 16)
graph_10.add_edge(node_04, node_00, 5)
graph_10.add_edge(node_02, node_00, 20)
graph_10.add_edge(node_01, node_03, 13)

"""
	GRAPH 11
"""

graph_11 = Graph(True)

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

graph_11.add_edge(node_00, node_02, 10)
graph_11.add_edge(node_04, node_00, 15)
graph_11.add_edge(node_04, node_04, 16)
graph_11.add_edge(node_01, node_01, 4)
graph_11.add_edge(node_04, node_03, 17)
graph_11.add_edge(node_04, node_04, 5)
graph_11.add_edge(node_01, node_00, 9)
graph_11.add_edge(node_02, node_01, 12)
graph_11.add_edge(node_03, node_03, 4)
graph_11.add_edge(node_01, node_03, 15)
graph_11.add_edge(node_00, node_04, 1)
graph_11.add_edge(node_04, node_00, 13)
graph_11.add_edge(node_04, node_01, 3)
graph_11.add_edge(node_01, node_02, 12)
graph_11.add_edge(node_03, node_01, 4)
graph_11.add_edge(node_04, node_02, 12)
graph_11.add_edge(node_00, node_03, 11)
graph_11.add_edge(node_04, node_04, 2)
graph_11.add_edge(node_02, node_04, 18)
graph_11.add_edge(node_01, node_00, 9)

"""
	GRAPH 12
"""

graph_12 = Graph(True)

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

graph_12.add_edge(node_03, node_02, 1)
graph_12.add_edge(node_03, node_00, 17)
graph_12.add_edge(node_04, node_03, 7)
graph_12.add_edge(node_04, node_02, 15)
graph_12.add_edge(node_02, node_02, 17)
graph_12.add_edge(node_02, node_01, 11)
graph_12.add_edge(node_00, node_02, 10)
graph_12.add_edge(node_01, node_04, 15)
graph_12.add_edge(node_01, node_03, 5)
graph_12.add_edge(node_03, node_03, 4)
graph_12.add_edge(node_03, node_04, 10)
graph_12.add_edge(node_01, node_00, 12)
graph_12.add_edge(node_03, node_00, 6)
graph_12.add_edge(node_02, node_01, 10)
graph_12.add_edge(node_04, node_03, 14)
graph_12.add_edge(node_02, node_00, 1)
graph_12.add_edge(node_03, node_00, 12)
graph_12.add_edge(node_03, node_03, 20)
graph_12.add_edge(node_00, node_01, 9)
graph_12.add_edge(node_00, node_00, 10)

"""
	GRAPH 13
"""

graph_13 = Graph(True)

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

graph_13.add_edge(node_00, node_03, 3)
graph_13.add_edge(node_03, node_02, 16)
graph_13.add_edge(node_03, node_00, 7)
graph_13.add_edge(node_01, node_01, 4)
graph_13.add_edge(node_04, node_00, 3)
graph_13.add_edge(node_01, node_00, 13)
graph_13.add_edge(node_02, node_01, 1)
graph_13.add_edge(node_02, node_02, 11)
graph_13.add_edge(node_03, node_01, 17)
graph_13.add_edge(node_04, node_04, 18)
graph_13.add_edge(node_04, node_01, 19)
graph_13.add_edge(node_01, node_03, 1)
graph_13.add_edge(node_01, node_00, 11)
graph_13.add_edge(node_03, node_02, 19)
graph_13.add_edge(node_02, node_00, 4)
graph_13.add_edge(node_02, node_01, 8)
graph_13.add_edge(node_04, node_03, 9)
graph_13.add_edge(node_01, node_01, 6)
graph_13.add_edge(node_01, node_02, 5)
graph_13.add_edge(node_00, node_00, 1)

"""
	GRAPH 14
"""

graph_14 = Graph(True)

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

graph_14.add_edge(node_03, node_00, 2)
graph_14.add_edge(node_00, node_03, 7)
graph_14.add_edge(node_02, node_03, 14)
graph_14.add_edge(node_03, node_00, 14)
graph_14.add_edge(node_00, node_02, 1)
graph_14.add_edge(node_04, node_04, 7)
graph_14.add_edge(node_00, node_02, 1)
graph_14.add_edge(node_01, node_03, 11)
graph_14.add_edge(node_02, node_00, 12)
graph_14.add_edge(node_01, node_03, 7)
graph_14.add_edge(node_03, node_03, 15)
graph_14.add_edge(node_02, node_01, 15)
graph_14.add_edge(node_01, node_04, 12)
graph_14.add_edge(node_01, node_01, 8)
graph_14.add_edge(node_01, node_03, 6)
graph_14.add_edge(node_00, node_00, 16)
graph_14.add_edge(node_03, node_04, 18)
graph_14.add_edge(node_02, node_02, 8)
graph_14.add_edge(node_03, node_04, 8)
graph_14.add_edge(node_02, node_00, 16)

"""
	GRAPH 15
"""

graph_15 = Graph(True)

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

graph_15.add_edge(node_00, node_00, 13)
graph_15.add_edge(node_01, node_03, 10)
graph_15.add_edge(node_02, node_02, 11)
graph_15.add_edge(node_03, node_02, 4)
graph_15.add_edge(node_01, node_00, 6)
graph_15.add_edge(node_00, node_01, 15)
graph_15.add_edge(node_03, node_02, 13)
graph_15.add_edge(node_00, node_03, 18)
graph_15.add_edge(node_02, node_00, 15)
graph_15.add_edge(node_03, node_03, 17)
graph_15.add_edge(node_00, node_04, 15)
graph_15.add_edge(node_01, node_00, 12)
graph_15.add_edge(node_01, node_01, 7)
graph_15.add_edge(node_02, node_01, 17)
graph_15.add_edge(node_02, node_01, 18)
graph_15.add_edge(node_04, node_00, 17)
graph_15.add_edge(node_01, node_01, 16)
graph_15.add_edge(node_02, node_00, 14)
graph_15.add_edge(node_04, node_03, 19)
graph_15.add_edge(node_04, node_00, 8)

"""
	GRAPH 16
"""

graph_16 = Graph(True)

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

graph_16.add_edge(node_01, node_01, 5)
graph_16.add_edge(node_04, node_02, 18)
graph_16.add_edge(node_01, node_02, 14)
graph_16.add_edge(node_01, node_02, 12)
graph_16.add_edge(node_04, node_00, 4)
graph_16.add_edge(node_00, node_02, 6)
graph_16.add_edge(node_00, node_02, 6)
graph_16.add_edge(node_03, node_03, 9)
graph_16.add_edge(node_02, node_01, 14)
graph_16.add_edge(node_04, node_04, 5)
graph_16.add_edge(node_04, node_02, 4)
graph_16.add_edge(node_01, node_03, 13)
graph_16.add_edge(node_01, node_02, 4)
graph_16.add_edge(node_03, node_02, 17)
graph_16.add_edge(node_00, node_02, 5)
graph_16.add_edge(node_02, node_04, 2)
graph_16.add_edge(node_04, node_01, 7)
graph_16.add_edge(node_01, node_04, 16)
graph_16.add_edge(node_02, node_02, 11)
graph_16.add_edge(node_04, node_01, 8)

"""
	GRAPH 17
"""

graph_17 = Graph(True)

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

graph_17.add_edge(node_03, node_03, 14)
graph_17.add_edge(node_00, node_01, 3)
graph_17.add_edge(node_04, node_02, 2)
graph_17.add_edge(node_03, node_00, 4)
graph_17.add_edge(node_02, node_01, 2)
graph_17.add_edge(node_02, node_03, 12)
graph_17.add_edge(node_04, node_04, 19)
graph_17.add_edge(node_00, node_04, 15)
graph_17.add_edge(node_01, node_03, 1)
graph_17.add_edge(node_02, node_00, 15)
graph_17.add_edge(node_01, node_04, 5)
graph_17.add_edge(node_00, node_03, 7)
graph_17.add_edge(node_00, node_04, 18)
graph_17.add_edge(node_04, node_04, 1)
graph_17.add_edge(node_02, node_01, 6)
graph_17.add_edge(node_01, node_00, 14)
graph_17.add_edge(node_01, node_02, 9)
graph_17.add_edge(node_03, node_03, 18)
graph_17.add_edge(node_02, node_01, 15)
graph_17.add_edge(node_03, node_01, 2)

"""
	GRAPH 18
"""

graph_18 = Graph(True)

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

graph_18.add_edge(node_00, node_04, 14)
graph_18.add_edge(node_02, node_00, 6)
graph_18.add_edge(node_04, node_03, 6)
graph_18.add_edge(node_01, node_02, 4)
graph_18.add_edge(node_02, node_04, 6)
graph_18.add_edge(node_01, node_04, 2)
graph_18.add_edge(node_00, node_02, 14)
graph_18.add_edge(node_04, node_00, 10)
graph_18.add_edge(node_04, node_04, 11)
graph_18.add_edge(node_03, node_01, 6)
graph_18.add_edge(node_01, node_03, 16)
graph_18.add_edge(node_00, node_00, 1)
graph_18.add_edge(node_04, node_00, 7)
graph_18.add_edge(node_01, node_03, 3)
graph_18.add_edge(node_04, node_03, 12)
graph_18.add_edge(node_02, node_04, 14)
graph_18.add_edge(node_01, node_02, 5)
graph_18.add_edge(node_04, node_03, 1)
graph_18.add_edge(node_01, node_02, 17)
graph_18.add_edge(node_04, node_04, 2)

"""
	GRAPH 19
"""

graph_19 = Graph(True)

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

graph_19.add_edge(node_03, node_00, 12)
graph_19.add_edge(node_03, node_04, 19)
graph_19.add_edge(node_00, node_02, 17)
graph_19.add_edge(node_00, node_01, 16)
graph_19.add_edge(node_04, node_02, 11)
graph_19.add_edge(node_01, node_03, 14)
graph_19.add_edge(node_01, node_04, 3)
graph_19.add_edge(node_03, node_01, 13)
graph_19.add_edge(node_02, node_02, 6)
graph_19.add_edge(node_03, node_02, 16)
graph_19.add_edge(node_01, node_04, 5)
graph_19.add_edge(node_00, node_02, 7)
graph_19.add_edge(node_04, node_01, 8)
graph_19.add_edge(node_03, node_02, 2)
graph_19.add_edge(node_02, node_00, 2)
graph_19.add_edge(node_02, node_03, 7)
graph_19.add_edge(node_03, node_00, 5)
graph_19.add_edge(node_03, node_01, 7)
graph_19.add_edge(node_00, node_01, 5)
graph_19.add_edge(node_04, node_00, 7)

"""
	GRAPH 20
"""

graph_20 = Graph(True)

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

graph_20.add_edge(node_01, node_04, 3)
graph_20.add_edge(node_00, node_04, 2)
graph_20.add_edge(node_03, node_03, 17)
graph_20.add_edge(node_02, node_04, 9)
graph_20.add_edge(node_00, node_04, 9)
graph_20.add_edge(node_02, node_01, 10)
graph_20.add_edge(node_04, node_02, 6)
graph_20.add_edge(node_04, node_04, 19)
graph_20.add_edge(node_03, node_01, 12)
graph_20.add_edge(node_01, node_04, 8)
graph_20.add_edge(node_01, node_02, 19)
graph_20.add_edge(node_01, node_00, 4)
graph_20.add_edge(node_04, node_02, 5)
graph_20.add_edge(node_04, node_02, 16)
graph_20.add_edge(node_01, node_04, 20)
graph_20.add_edge(node_04, node_03, 20)
graph_20.add_edge(node_04, node_04, 17)
graph_20.add_edge(node_02, node_01, 18)
graph_20.add_edge(node_00, node_01, 9)
graph_20.add_edge(node_01, node_01, 7)

"""
	GRAPH 21
"""

graph_21 = Graph(True)

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

graph_21.add_edge(node_03, node_00, 13)
graph_21.add_edge(node_02, node_02, 10)
graph_21.add_edge(node_04, node_03, 6)
graph_21.add_edge(node_01, node_01, 18)
graph_21.add_edge(node_01, node_02, 6)
graph_21.add_edge(node_04, node_03, 1)
graph_21.add_edge(node_04, node_03, 13)
graph_21.add_edge(node_03, node_03, 4)
graph_21.add_edge(node_02, node_01, 5)
graph_21.add_edge(node_03, node_02, 2)
graph_21.add_edge(node_03, node_02, 5)
graph_21.add_edge(node_04, node_02, 11)
graph_21.add_edge(node_00, node_03, 10)
graph_21.add_edge(node_04, node_01, 14)
graph_21.add_edge(node_02, node_04, 7)
graph_21.add_edge(node_03, node_04, 11)
graph_21.add_edge(node_02, node_00, 9)
graph_21.add_edge(node_03, node_03, 3)
graph_21.add_edge(node_03, node_04, 17)
graph_21.add_edge(node_03, node_02, 14)

"""
	GRAPH 22
"""

graph_22 = Graph(True)

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

graph_22.add_edge(node_00, node_04, 17)
graph_22.add_edge(node_03, node_04, 20)
graph_22.add_edge(node_00, node_04, 2)
graph_22.add_edge(node_01, node_03, 5)
graph_22.add_edge(node_03, node_01, 5)
graph_22.add_edge(node_03, node_04, 7)
graph_22.add_edge(node_03, node_02, 19)
graph_22.add_edge(node_00, node_02, 15)
graph_22.add_edge(node_01, node_04, 12)
graph_22.add_edge(node_00, node_04, 8)
graph_22.add_edge(node_03, node_00, 7)
graph_22.add_edge(node_03, node_02, 3)
graph_22.add_edge(node_04, node_04, 11)
graph_22.add_edge(node_04, node_01, 4)
graph_22.add_edge(node_03, node_04, 14)
graph_22.add_edge(node_02, node_03, 18)
graph_22.add_edge(node_03, node_04, 3)
graph_22.add_edge(node_03, node_04, 6)
graph_22.add_edge(node_03, node_02, 10)
graph_22.add_edge(node_01, node_00, 6)

"""
	GRAPH 23
"""

graph_23 = Graph(True)

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

graph_23.add_edge(node_04, node_03, 5)
graph_23.add_edge(node_02, node_02, 4)
graph_23.add_edge(node_00, node_02, 2)
graph_23.add_edge(node_02, node_03, 19)
graph_23.add_edge(node_00, node_00, 1)
graph_23.add_edge(node_04, node_01, 10)
graph_23.add_edge(node_01, node_02, 15)
graph_23.add_edge(node_04, node_03, 19)
graph_23.add_edge(node_02, node_01, 9)
graph_23.add_edge(node_02, node_04, 4)
graph_23.add_edge(node_02, node_04, 9)
graph_23.add_edge(node_01, node_04, 14)
graph_23.add_edge(node_01, node_01, 6)
graph_23.add_edge(node_02, node_03, 15)
graph_23.add_edge(node_01, node_02, 1)
graph_23.add_edge(node_00, node_00, 19)
graph_23.add_edge(node_03, node_02, 10)
graph_23.add_edge(node_04, node_00, 5)
graph_23.add_edge(node_02, node_04, 5)
graph_23.add_edge(node_00, node_04, 9)

"""
	GRAPH 24
"""

graph_24 = Graph(True)

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

graph_24.add_edge(node_00, node_00, 7)
graph_24.add_edge(node_02, node_01, 6)
graph_24.add_edge(node_02, node_02, 1)
graph_24.add_edge(node_03, node_02, 3)
graph_24.add_edge(node_02, node_01, 11)
graph_24.add_edge(node_04, node_00, 7)
graph_24.add_edge(node_04, node_03, 15)
graph_24.add_edge(node_04, node_02, 16)
graph_24.add_edge(node_03, node_02, 11)
graph_24.add_edge(node_04, node_03, 12)
graph_24.add_edge(node_01, node_02, 4)
graph_24.add_edge(node_00, node_02, 7)
graph_24.add_edge(node_01, node_03, 14)
graph_24.add_edge(node_01, node_00, 19)
graph_24.add_edge(node_01, node_00, 10)
graph_24.add_edge(node_02, node_00, 15)
graph_24.add_edge(node_00, node_03, 12)
graph_24.add_edge(node_00, node_01, 19)
graph_24.add_edge(node_04, node_02, 14)
graph_24.add_edge(node_00, node_01, 4)

"""
	GRAPH 25
"""

graph_25 = Graph(True)

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

graph_25.add_edge(node_00, node_02, 17)
graph_25.add_edge(node_03, node_00, 2)
graph_25.add_edge(node_02, node_00, 16)
graph_25.add_edge(node_01, node_03, 9)
graph_25.add_edge(node_00, node_02, 17)
graph_25.add_edge(node_02, node_00, 1)
graph_25.add_edge(node_00, node_00, 19)
graph_25.add_edge(node_02, node_03, 2)
graph_25.add_edge(node_02, node_03, 17)
graph_25.add_edge(node_01, node_04, 14)
graph_25.add_edge(node_01, node_02, 1)
graph_25.add_edge(node_04, node_02, 1)
graph_25.add_edge(node_01, node_02, 8)
graph_25.add_edge(node_00, node_04, 8)
graph_25.add_edge(node_01, node_00, 7)
graph_25.add_edge(node_00, node_02, 2)
graph_25.add_edge(node_02, node_02, 14)
graph_25.add_edge(node_04, node_00, 11)
graph_25.add_edge(node_04, node_03, 6)
graph_25.add_edge(node_03, node_02, 20)

"""
	GRAPH 26
"""

graph_26 = Graph(True)

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

graph_26.add_edge(node_00, node_04, 1)
graph_26.add_edge(node_02, node_02, 18)
graph_26.add_edge(node_01, node_03, 15)
graph_26.add_edge(node_02, node_00, 1)
graph_26.add_edge(node_03, node_00, 17)
graph_26.add_edge(node_04, node_01, 5)
graph_26.add_edge(node_00, node_04, 18)
graph_26.add_edge(node_04, node_01, 20)
graph_26.add_edge(node_00, node_00, 11)
graph_26.add_edge(node_04, node_04, 12)
graph_26.add_edge(node_01, node_00, 2)
graph_26.add_edge(node_02, node_00, 7)
graph_26.add_edge(node_04, node_02, 19)
graph_26.add_edge(node_02, node_03, 12)
graph_26.add_edge(node_03, node_02, 3)
graph_26.add_edge(node_03, node_04, 5)
graph_26.add_edge(node_00, node_04, 18)
graph_26.add_edge(node_00, node_00, 16)
graph_26.add_edge(node_00, node_01, 19)
graph_26.add_edge(node_04, node_04, 4)

"""
	GRAPH 27
"""

graph_27 = Graph(True)

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

graph_27.add_edge(node_01, node_01, 19)
graph_27.add_edge(node_00, node_01, 17)
graph_27.add_edge(node_00, node_01, 11)
graph_27.add_edge(node_00, node_00, 17)
graph_27.add_edge(node_00, node_00, 1)
graph_27.add_edge(node_00, node_00, 15)
graph_27.add_edge(node_01, node_00, 14)
graph_27.add_edge(node_02, node_02, 5)
graph_27.add_edge(node_03, node_00, 18)
graph_27.add_edge(node_01, node_02, 2)
graph_27.add_edge(node_00, node_04, 9)
graph_27.add_edge(node_04, node_03, 17)
graph_27.add_edge(node_02, node_02, 5)
graph_27.add_edge(node_03, node_00, 3)
graph_27.add_edge(node_02, node_04, 7)
graph_27.add_edge(node_03, node_01, 4)
graph_27.add_edge(node_04, node_04, 18)
graph_27.add_edge(node_04, node_03, 3)
graph_27.add_edge(node_03, node_03, 17)
graph_27.add_edge(node_02, node_01, 5)

"""
	GRAPH 28
"""

graph_28 = Graph(True)

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

graph_28.add_edge(node_00, node_00, 1)
graph_28.add_edge(node_03, node_02, 16)
graph_28.add_edge(node_00, node_04, 7)
graph_28.add_edge(node_04, node_00, 12)
graph_28.add_edge(node_03, node_00, 4)
graph_28.add_edge(node_02, node_00, 15)
graph_28.add_edge(node_00, node_02, 14)
graph_28.add_edge(node_04, node_01, 10)
graph_28.add_edge(node_02, node_00, 10)
graph_28.add_edge(node_04, node_04, 11)
graph_28.add_edge(node_00, node_02, 6)
graph_28.add_edge(node_04, node_03, 7)
graph_28.add_edge(node_00, node_04, 11)
graph_28.add_edge(node_00, node_01, 8)
graph_28.add_edge(node_03, node_03, 19)
graph_28.add_edge(node_00, node_02, 3)
graph_28.add_edge(node_03, node_02, 13)
graph_28.add_edge(node_02, node_01, 1)
graph_28.add_edge(node_00, node_01, 8)
graph_28.add_edge(node_02, node_01, 6)

"""
	GRAPH 29
"""

graph_29 = Graph(True)

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

graph_29.add_edge(node_01, node_03, 15)
graph_29.add_edge(node_04, node_01, 20)
graph_29.add_edge(node_02, node_01, 2)
graph_29.add_edge(node_01, node_02, 14)
graph_29.add_edge(node_00, node_02, 16)
graph_29.add_edge(node_04, node_00, 11)
graph_29.add_edge(node_04, node_00, 19)
graph_29.add_edge(node_04, node_04, 10)
graph_29.add_edge(node_03, node_02, 8)
graph_29.add_edge(node_01, node_04, 18)
graph_29.add_edge(node_01, node_01, 17)
graph_29.add_edge(node_03, node_00, 14)
graph_29.add_edge(node_00, node_02, 3)
graph_29.add_edge(node_02, node_04, 16)
graph_29.add_edge(node_04, node_03, 5)
graph_29.add_edge(node_02, node_00, 3)
graph_29.add_edge(node_00, node_04, 6)
graph_29.add_edge(node_01, node_01, 6)
graph_29.add_edge(node_03, node_03, 7)
graph_29.add_edge(node_03, node_01, 19)

"""
	GRAPH 30
"""

graph_30 = Graph(True)

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

graph_30.add_edge(node_01, node_01, 8)
graph_30.add_edge(node_02, node_03, 20)
graph_30.add_edge(node_03, node_01, 5)
graph_30.add_edge(node_00, node_04, 18)
graph_30.add_edge(node_04, node_04, 17)
graph_30.add_edge(node_01, node_04, 4)
graph_30.add_edge(node_00, node_03, 16)
graph_30.add_edge(node_01, node_03, 15)
graph_30.add_edge(node_04, node_02, 15)
graph_30.add_edge(node_03, node_01, 5)
graph_30.add_edge(node_03, node_01, 4)
graph_30.add_edge(node_02, node_03, 16)
graph_30.add_edge(node_04, node_04, 13)
graph_30.add_edge(node_04, node_00, 7)
graph_30.add_edge(node_03, node_02, 14)
graph_30.add_edge(node_04, node_04, 19)
graph_30.add_edge(node_02, node_03, 9)
graph_30.add_edge(node_01, node_02, 4)
graph_30.add_edge(node_02, node_01, 19)
graph_30.add_edge(node_03, node_01, 5)

"""
	GRAPH 31
"""

graph_31 = Graph(True)

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

graph_31.add_edge(node_02, node_02, 17)
graph_31.add_edge(node_04, node_01, 14)
graph_31.add_edge(node_01, node_04, 8)
graph_31.add_edge(node_00, node_01, 16)
graph_31.add_edge(node_02, node_01, 10)
graph_31.add_edge(node_02, node_01, 5)
graph_31.add_edge(node_03, node_03, 2)
graph_31.add_edge(node_02, node_01, 15)
graph_31.add_edge(node_01, node_00, 15)
graph_31.add_edge(node_04, node_01, 10)
graph_31.add_edge(node_00, node_04, 18)
graph_31.add_edge(node_03, node_04, 3)
graph_31.add_edge(node_02, node_04, 20)
graph_31.add_edge(node_03, node_03, 11)
graph_31.add_edge(node_01, node_04, 14)
graph_31.add_edge(node_01, node_04, 5)
graph_31.add_edge(node_02, node_02, 20)
graph_31.add_edge(node_00, node_01, 2)
graph_31.add_edge(node_02, node_04, 13)
graph_31.add_edge(node_03, node_03, 13)

"""
	GRAPH 32
"""

graph_32 = Graph(True)

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

graph_32.add_edge(node_03, node_01, 15)
graph_32.add_edge(node_00, node_02, 6)
graph_32.add_edge(node_02, node_03, 14)
graph_32.add_edge(node_02, node_02, 17)
graph_32.add_edge(node_01, node_00, 17)
graph_32.add_edge(node_03, node_03, 6)
graph_32.add_edge(node_00, node_00, 3)
graph_32.add_edge(node_00, node_02, 1)
graph_32.add_edge(node_04, node_01, 1)
graph_32.add_edge(node_01, node_03, 14)
graph_32.add_edge(node_03, node_03, 11)
graph_32.add_edge(node_00, node_01, 1)
graph_32.add_edge(node_02, node_01, 19)
graph_32.add_edge(node_00, node_00, 17)
graph_32.add_edge(node_03, node_02, 7)
graph_32.add_edge(node_04, node_01, 16)
graph_32.add_edge(node_03, node_00, 5)
graph_32.add_edge(node_04, node_04, 13)
graph_32.add_edge(node_04, node_01, 15)
graph_32.add_edge(node_00, node_03, 1)

"""
	GRAPH 33
"""

graph_33 = Graph(True)

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

graph_33.add_edge(node_01, node_02, 18)
graph_33.add_edge(node_04, node_04, 11)
graph_33.add_edge(node_02, node_01, 13)
graph_33.add_edge(node_03, node_03, 8)
graph_33.add_edge(node_00, node_03, 20)
graph_33.add_edge(node_01, node_03, 20)
graph_33.add_edge(node_04, node_00, 7)
graph_33.add_edge(node_01, node_03, 18)
graph_33.add_edge(node_03, node_04, 2)
graph_33.add_edge(node_04, node_03, 12)
graph_33.add_edge(node_02, node_02, 5)
graph_33.add_edge(node_04, node_04, 16)
graph_33.add_edge(node_04, node_03, 13)
graph_33.add_edge(node_02, node_02, 5)
graph_33.add_edge(node_04, node_04, 4)
graph_33.add_edge(node_01, node_01, 1)
graph_33.add_edge(node_01, node_04, 4)
graph_33.add_edge(node_00, node_00, 4)
graph_33.add_edge(node_03, node_01, 20)
graph_33.add_edge(node_01, node_04, 14)

"""
	GRAPH 34
"""

graph_34 = Graph(True)

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

graph_34.add_edge(node_00, node_02, 20)
graph_34.add_edge(node_02, node_02, 2)
graph_34.add_edge(node_03, node_02, 16)
graph_34.add_edge(node_03, node_02, 14)
graph_34.add_edge(node_00, node_04, 12)
graph_34.add_edge(node_03, node_02, 6)
graph_34.add_edge(node_01, node_04, 5)
graph_34.add_edge(node_00, node_00, 17)
graph_34.add_edge(node_01, node_00, 9)
graph_34.add_edge(node_02, node_01, 11)
graph_34.add_edge(node_04, node_02, 15)
graph_34.add_edge(node_01, node_01, 6)
graph_34.add_edge(node_01, node_03, 16)
graph_34.add_edge(node_02, node_02, 4)
graph_34.add_edge(node_04, node_03, 11)
graph_34.add_edge(node_00, node_01, 4)
graph_34.add_edge(node_01, node_03, 7)
graph_34.add_edge(node_04, node_01, 8)
graph_34.add_edge(node_01, node_01, 9)
graph_34.add_edge(node_00, node_01, 20)

"""
	GRAPH 35
"""

graph_35 = Graph(True)

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

graph_35.add_edge(node_00, node_04, 2)
graph_35.add_edge(node_01, node_03, 7)
graph_35.add_edge(node_02, node_01, 18)
graph_35.add_edge(node_00, node_02, 6)
graph_35.add_edge(node_03, node_02, 12)
graph_35.add_edge(node_03, node_03, 14)
graph_35.add_edge(node_04, node_03, 17)
graph_35.add_edge(node_04, node_04, 14)
graph_35.add_edge(node_00, node_04, 7)
graph_35.add_edge(node_02, node_02, 8)
graph_35.add_edge(node_00, node_03, 6)
graph_35.add_edge(node_02, node_03, 16)
graph_35.add_edge(node_03, node_01, 6)
graph_35.add_edge(node_03, node_03, 18)
graph_35.add_edge(node_01, node_04, 18)
graph_35.add_edge(node_02, node_03, 20)
graph_35.add_edge(node_04, node_01, 13)
graph_35.add_edge(node_02, node_03, 6)
graph_35.add_edge(node_00, node_01, 14)
graph_35.add_edge(node_03, node_03, 14)

"""
	GRAPH 36
"""

graph_36 = Graph(True)

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

graph_36.add_edge(node_03, node_00, 2)
graph_36.add_edge(node_01, node_00, 9)
graph_36.add_edge(node_01, node_03, 11)
graph_36.add_edge(node_01, node_01, 4)
graph_36.add_edge(node_00, node_04, 2)
graph_36.add_edge(node_02, node_02, 11)
graph_36.add_edge(node_00, node_00, 1)
graph_36.add_edge(node_03, node_00, 16)
graph_36.add_edge(node_00, node_02, 6)
graph_36.add_edge(node_02, node_03, 4)
graph_36.add_edge(node_00, node_02, 18)
graph_36.add_edge(node_03, node_04, 13)
graph_36.add_edge(node_00, node_02, 4)
graph_36.add_edge(node_00, node_03, 5)
graph_36.add_edge(node_00, node_02, 20)
graph_36.add_edge(node_00, node_01, 5)
graph_36.add_edge(node_03, node_04, 15)
graph_36.add_edge(node_03, node_00, 2)
graph_36.add_edge(node_00, node_00, 10)
graph_36.add_edge(node_03, node_04, 13)

"""
	GRAPH 37
"""

graph_37 = Graph(True)

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

graph_37.add_edge(node_01, node_01, 11)
graph_37.add_edge(node_03, node_01, 2)
graph_37.add_edge(node_02, node_04, 7)
graph_37.add_edge(node_01, node_01, 8)
graph_37.add_edge(node_00, node_04, 17)
graph_37.add_edge(node_03, node_00, 9)
graph_37.add_edge(node_03, node_00, 17)
graph_37.add_edge(node_04, node_04, 16)
graph_37.add_edge(node_04, node_00, 7)
graph_37.add_edge(node_04, node_03, 18)
graph_37.add_edge(node_03, node_02, 15)
graph_37.add_edge(node_00, node_03, 6)
graph_37.add_edge(node_00, node_02, 10)
graph_37.add_edge(node_02, node_00, 1)
graph_37.add_edge(node_04, node_04, 2)
graph_37.add_edge(node_02, node_01, 13)
graph_37.add_edge(node_03, node_01, 1)
graph_37.add_edge(node_02, node_02, 20)
graph_37.add_edge(node_04, node_02, 6)
graph_37.add_edge(node_03, node_00, 12)

"""
	GRAPH 38
"""

graph_38 = Graph(True)

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

graph_38.add_edge(node_01, node_03, 6)
graph_38.add_edge(node_03, node_00, 15)
graph_38.add_edge(node_01, node_00, 3)
graph_38.add_edge(node_03, node_04, 5)
graph_38.add_edge(node_00, node_03, 10)
graph_38.add_edge(node_03, node_00, 4)
graph_38.add_edge(node_02, node_00, 12)
graph_38.add_edge(node_04, node_03, 6)
graph_38.add_edge(node_03, node_03, 2)
graph_38.add_edge(node_02, node_04, 17)
graph_38.add_edge(node_04, node_01, 2)
graph_38.add_edge(node_02, node_03, 13)
graph_38.add_edge(node_01, node_00, 2)
graph_38.add_edge(node_02, node_04, 10)
graph_38.add_edge(node_00, node_04, 11)
graph_38.add_edge(node_00, node_00, 13)
graph_38.add_edge(node_02, node_04, 11)
graph_38.add_edge(node_02, node_01, 12)
graph_38.add_edge(node_02, node_04, 19)
graph_38.add_edge(node_04, node_01, 17)

"""
	GRAPH 39
"""

graph_39 = Graph(True)

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

graph_39.add_edge(node_04, node_01, 18)
graph_39.add_edge(node_00, node_04, 10)
graph_39.add_edge(node_03, node_01, 19)
graph_39.add_edge(node_01, node_00, 13)
graph_39.add_edge(node_02, node_00, 15)
graph_39.add_edge(node_04, node_01, 12)
graph_39.add_edge(node_00, node_01, 10)
graph_39.add_edge(node_04, node_04, 18)
graph_39.add_edge(node_04, node_02, 14)
graph_39.add_edge(node_00, node_04, 6)
graph_39.add_edge(node_01, node_00, 1)
graph_39.add_edge(node_03, node_02, 9)
graph_39.add_edge(node_01, node_04, 12)
graph_39.add_edge(node_03, node_00, 11)
graph_39.add_edge(node_03, node_00, 9)
graph_39.add_edge(node_03, node_04, 19)
graph_39.add_edge(node_03, node_02, 18)
graph_39.add_edge(node_02, node_03, 6)
graph_39.add_edge(node_00, node_00, 2)
graph_39.add_edge(node_02, node_01, 2)

"""
	GRAPH 40
"""

graph_40 = Graph(True)

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

graph_40.add_edge(node_02, node_02, 2)
graph_40.add_edge(node_03, node_01, 20)
graph_40.add_edge(node_01, node_02, 2)
graph_40.add_edge(node_00, node_04, 11)
graph_40.add_edge(node_02, node_02, 16)
graph_40.add_edge(node_03, node_02, 3)
graph_40.add_edge(node_03, node_03, 20)
graph_40.add_edge(node_00, node_03, 20)
graph_40.add_edge(node_04, node_02, 18)
graph_40.add_edge(node_04, node_04, 15)
graph_40.add_edge(node_01, node_01, 9)
graph_40.add_edge(node_00, node_01, 13)
graph_40.add_edge(node_03, node_00, 16)
graph_40.add_edge(node_02, node_04, 2)
graph_40.add_edge(node_04, node_01, 8)
graph_40.add_edge(node_03, node_01, 13)
graph_40.add_edge(node_04, node_02, 10)
graph_40.add_edge(node_00, node_00, 3)
graph_40.add_edge(node_02, node_00, 7)
graph_40.add_edge(node_03, node_04, 2)

"""
	GRAPH 41
"""

graph_41 = Graph(True)

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

graph_41.add_edge(node_04, node_00, 1)
graph_41.add_edge(node_00, node_03, 15)
graph_41.add_edge(node_04, node_00, 10)
graph_41.add_edge(node_02, node_03, 20)
graph_41.add_edge(node_04, node_00, 11)
graph_41.add_edge(node_04, node_01, 17)
graph_41.add_edge(node_00, node_01, 4)
graph_41.add_edge(node_03, node_00, 5)
graph_41.add_edge(node_02, node_03, 18)
graph_41.add_edge(node_02, node_03, 14)
graph_41.add_edge(node_00, node_00, 6)
graph_41.add_edge(node_03, node_00, 2)
graph_41.add_edge(node_03, node_01, 17)
graph_41.add_edge(node_02, node_03, 17)
graph_41.add_edge(node_02, node_00, 18)
graph_41.add_edge(node_00, node_03, 16)
graph_41.add_edge(node_00, node_00, 8)
graph_41.add_edge(node_02, node_01, 9)
graph_41.add_edge(node_01, node_02, 5)
graph_41.add_edge(node_02, node_01, 9)

"""
	GRAPH 42
"""

graph_42 = Graph(True)

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

graph_42.add_edge(node_04, node_00, 10)
graph_42.add_edge(node_02, node_02, 20)
graph_42.add_edge(node_01, node_01, 6)
graph_42.add_edge(node_01, node_01, 14)
graph_42.add_edge(node_03, node_00, 16)
graph_42.add_edge(node_04, node_01, 11)
graph_42.add_edge(node_03, node_03, 19)
graph_42.add_edge(node_00, node_01, 8)
graph_42.add_edge(node_04, node_00, 5)
graph_42.add_edge(node_04, node_01, 12)
graph_42.add_edge(node_01, node_03, 19)
graph_42.add_edge(node_00, node_01, 5)
graph_42.add_edge(node_01, node_03, 14)
graph_42.add_edge(node_03, node_01, 16)
graph_42.add_edge(node_01, node_03, 10)
graph_42.add_edge(node_03, node_00, 9)
graph_42.add_edge(node_00, node_01, 20)
graph_42.add_edge(node_00, node_02, 2)
graph_42.add_edge(node_03, node_01, 7)
graph_42.add_edge(node_01, node_00, 7)

"""
	GRAPH 43
"""

graph_43 = Graph(True)

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

graph_43.add_edge(node_04, node_02, 17)
graph_43.add_edge(node_00, node_02, 12)
graph_43.add_edge(node_01, node_01, 5)
graph_43.add_edge(node_04, node_01, 2)
graph_43.add_edge(node_02, node_02, 7)
graph_43.add_edge(node_02, node_04, 5)
graph_43.add_edge(node_04, node_04, 18)
graph_43.add_edge(node_03, node_04, 2)
graph_43.add_edge(node_04, node_04, 15)
graph_43.add_edge(node_01, node_02, 5)
graph_43.add_edge(node_04, node_01, 7)
graph_43.add_edge(node_01, node_00, 15)
graph_43.add_edge(node_03, node_04, 15)
graph_43.add_edge(node_00, node_00, 2)
graph_43.add_edge(node_01, node_02, 12)
graph_43.add_edge(node_01, node_04, 13)
graph_43.add_edge(node_00, node_02, 4)
graph_43.add_edge(node_01, node_00, 9)
graph_43.add_edge(node_00, node_03, 8)
graph_43.add_edge(node_04, node_02, 1)

"""
	GRAPH 44
"""

graph_44 = Graph(True)

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

graph_44.add_edge(node_00, node_02, 19)
graph_44.add_edge(node_01, node_02, 19)
graph_44.add_edge(node_03, node_02, 14)
graph_44.add_edge(node_02, node_02, 2)
graph_44.add_edge(node_00, node_00, 15)
graph_44.add_edge(node_02, node_01, 7)
graph_44.add_edge(node_03, node_04, 14)
graph_44.add_edge(node_03, node_00, 17)
graph_44.add_edge(node_01, node_03, 20)
graph_44.add_edge(node_02, node_01, 14)
graph_44.add_edge(node_03, node_04, 19)
graph_44.add_edge(node_03, node_01, 10)
graph_44.add_edge(node_04, node_02, 8)
graph_44.add_edge(node_00, node_03, 20)
graph_44.add_edge(node_01, node_02, 1)
graph_44.add_edge(node_00, node_03, 6)
graph_44.add_edge(node_04, node_02, 9)
graph_44.add_edge(node_04, node_03, 9)
graph_44.add_edge(node_03, node_03, 14)
graph_44.add_edge(node_04, node_02, 2)

"""
	GRAPH 45
"""

graph_45 = Graph(True)

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

graph_45.add_edge(node_04, node_02, 10)
graph_45.add_edge(node_01, node_04, 4)
graph_45.add_edge(node_04, node_03, 8)
graph_45.add_edge(node_04, node_02, 4)
graph_45.add_edge(node_03, node_03, 3)
graph_45.add_edge(node_02, node_04, 18)
graph_45.add_edge(node_01, node_02, 1)
graph_45.add_edge(node_03, node_03, 7)
graph_45.add_edge(node_01, node_04, 10)
graph_45.add_edge(node_01, node_03, 1)
graph_45.add_edge(node_03, node_01, 10)
graph_45.add_edge(node_01, node_00, 10)
graph_45.add_edge(node_01, node_04, 4)
graph_45.add_edge(node_03, node_04, 9)
graph_45.add_edge(node_03, node_03, 9)
graph_45.add_edge(node_02, node_04, 9)
graph_45.add_edge(node_04, node_01, 11)
graph_45.add_edge(node_01, node_03, 2)
graph_45.add_edge(node_02, node_00, 20)
graph_45.add_edge(node_02, node_01, 12)

"""
	GRAPH 46
"""

graph_46 = Graph(True)

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

graph_46.add_edge(node_00, node_04, 16)
graph_46.add_edge(node_02, node_01, 10)
graph_46.add_edge(node_03, node_03, 8)
graph_46.add_edge(node_00, node_04, 6)
graph_46.add_edge(node_00, node_02, 19)
graph_46.add_edge(node_00, node_01, 3)
graph_46.add_edge(node_00, node_00, 20)
graph_46.add_edge(node_03, node_04, 14)
graph_46.add_edge(node_04, node_00, 14)
graph_46.add_edge(node_01, node_02, 10)
graph_46.add_edge(node_02, node_02, 6)
graph_46.add_edge(node_00, node_03, 8)
graph_46.add_edge(node_02, node_04, 6)
graph_46.add_edge(node_02, node_02, 18)
graph_46.add_edge(node_04, node_01, 14)
graph_46.add_edge(node_03, node_01, 17)
graph_46.add_edge(node_00, node_04, 16)
graph_46.add_edge(node_03, node_01, 8)
graph_46.add_edge(node_01, node_01, 3)
graph_46.add_edge(node_03, node_01, 20)

"""
	GRAPH 47
"""

graph_47 = Graph(True)

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

graph_47.add_edge(node_01, node_02, 4)
graph_47.add_edge(node_03, node_00, 14)
graph_47.add_edge(node_04, node_04, 15)
graph_47.add_edge(node_02, node_00, 20)
graph_47.add_edge(node_04, node_04, 7)
graph_47.add_edge(node_03, node_01, 1)
graph_47.add_edge(node_00, node_03, 5)
graph_47.add_edge(node_01, node_01, 19)
graph_47.add_edge(node_03, node_02, 6)
graph_47.add_edge(node_01, node_04, 5)
graph_47.add_edge(node_04, node_02, 20)
graph_47.add_edge(node_03, node_01, 9)
graph_47.add_edge(node_01, node_03, 14)
graph_47.add_edge(node_03, node_01, 11)
graph_47.add_edge(node_01, node_03, 12)
graph_47.add_edge(node_04, node_04, 18)
graph_47.add_edge(node_04, node_01, 10)
graph_47.add_edge(node_04, node_04, 13)
graph_47.add_edge(node_00, node_04, 18)
graph_47.add_edge(node_04, node_03, 6)

"""
	GRAPH 48
"""

graph_48 = Graph(True)

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

graph_48.add_edge(node_02, node_04, 3)
graph_48.add_edge(node_03, node_01, 11)
graph_48.add_edge(node_01, node_01, 13)
graph_48.add_edge(node_04, node_00, 10)
graph_48.add_edge(node_01, node_01, 4)
graph_48.add_edge(node_04, node_01, 13)
graph_48.add_edge(node_00, node_00, 3)
graph_48.add_edge(node_02, node_04, 5)
graph_48.add_edge(node_02, node_03, 5)
graph_48.add_edge(node_02, node_01, 11)
graph_48.add_edge(node_04, node_02, 8)
graph_48.add_edge(node_03, node_02, 14)
graph_48.add_edge(node_01, node_04, 15)
graph_48.add_edge(node_00, node_02, 17)
graph_48.add_edge(node_03, node_02, 7)
graph_48.add_edge(node_00, node_00, 14)
graph_48.add_edge(node_01, node_00, 14)
graph_48.add_edge(node_04, node_01, 17)
graph_48.add_edge(node_03, node_00, 7)
graph_48.add_edge(node_02, node_01, 8)

"""
	GRAPH 49
"""

graph_49 = Graph(True)

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

graph_49.add_edge(node_01, node_01, 19)
graph_49.add_edge(node_01, node_01, 10)
graph_49.add_edge(node_00, node_03, 3)
graph_49.add_edge(node_00, node_02, 16)
graph_49.add_edge(node_00, node_01, 16)
graph_49.add_edge(node_00, node_01, 5)
graph_49.add_edge(node_03, node_01, 5)
graph_49.add_edge(node_00, node_00, 3)
graph_49.add_edge(node_00, node_03, 8)
graph_49.add_edge(node_04, node_04, 1)
graph_49.add_edge(node_00, node_02, 14)
graph_49.add_edge(node_02, node_03, 4)
graph_49.add_edge(node_01, node_04, 8)
graph_49.add_edge(node_04, node_02, 12)
graph_49.add_edge(node_00, node_01, 13)
graph_49.add_edge(node_00, node_01, 19)
graph_49.add_edge(node_01, node_02, 11)
graph_49.add_edge(node_04, node_03, 7)
graph_49.add_edge(node_02, node_04, 11)
graph_49.add_edge(node_04, node_02, 19)

"""
	GRAPH 50
"""

graph_50 = Graph(True)

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

graph_50.add_edge(node_04, node_00, 20)
graph_50.add_edge(node_00, node_04, 14)
graph_50.add_edge(node_04, node_01, 15)
graph_50.add_edge(node_04, node_00, 10)
graph_50.add_edge(node_04, node_02, 15)
graph_50.add_edge(node_04, node_04, 10)
graph_50.add_edge(node_01, node_03, 16)
graph_50.add_edge(node_03, node_03, 15)
graph_50.add_edge(node_00, node_01, 19)
graph_50.add_edge(node_00, node_04, 11)
graph_50.add_edge(node_04, node_04, 13)
graph_50.add_edge(node_00, node_03, 5)
graph_50.add_edge(node_00, node_01, 1)
graph_50.add_edge(node_01, node_02, 5)
graph_50.add_edge(node_02, node_04, 10)
graph_50.add_edge(node_04, node_04, 18)
graph_50.add_edge(node_02, node_00, 10)
graph_50.add_edge(node_01, node_02, 9)
graph_50.add_edge(node_04, node_02, 11)
graph_50.add_edge(node_01, node_02, 6)

"""
	GRAPH 51
"""

graph_51 = Graph(True)

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

graph_51.add_edge(node_03, node_01, 15)
graph_51.add_edge(node_03, node_00, 18)
graph_51.add_edge(node_01, node_01, 14)
graph_51.add_edge(node_00, node_01, 5)
graph_51.add_edge(node_03, node_00, 13)
graph_51.add_edge(node_02, node_02, 12)
graph_51.add_edge(node_04, node_03, 10)
graph_51.add_edge(node_00, node_01, 17)
graph_51.add_edge(node_03, node_00, 10)
graph_51.add_edge(node_00, node_04, 4)
graph_51.add_edge(node_03, node_01, 1)
graph_51.add_edge(node_04, node_02, 18)
graph_51.add_edge(node_03, node_02, 1)
graph_51.add_edge(node_01, node_02, 17)
graph_51.add_edge(node_00, node_00, 20)
graph_51.add_edge(node_00, node_04, 7)
graph_51.add_edge(node_03, node_03, 17)
graph_51.add_edge(node_01, node_04, 18)
graph_51.add_edge(node_01, node_01, 12)
graph_51.add_edge(node_02, node_01, 7)

"""
	GRAPH 52
"""

graph_52 = Graph(True)

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

graph_52.add_edge(node_01, node_04, 7)
graph_52.add_edge(node_02, node_00, 18)
graph_52.add_edge(node_00, node_04, 9)
graph_52.add_edge(node_02, node_04, 19)
graph_52.add_edge(node_01, node_01, 3)
graph_52.add_edge(node_02, node_04, 2)
graph_52.add_edge(node_01, node_04, 19)
graph_52.add_edge(node_04, node_01, 9)
graph_52.add_edge(node_03, node_03, 15)
graph_52.add_edge(node_03, node_02, 6)
graph_52.add_edge(node_04, node_04, 15)
graph_52.add_edge(node_04, node_02, 13)
graph_52.add_edge(node_02, node_04, 1)
graph_52.add_edge(node_03, node_03, 17)
graph_52.add_edge(node_04, node_02, 17)
graph_52.add_edge(node_04, node_01, 3)
graph_52.add_edge(node_01, node_00, 17)
graph_52.add_edge(node_02, node_03, 20)
graph_52.add_edge(node_03, node_01, 1)
graph_52.add_edge(node_00, node_02, 20)

"""
	GRAPH 53
"""

graph_53 = Graph(True)

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

graph_53.add_edge(node_01, node_04, 14)
graph_53.add_edge(node_04, node_01, 9)
graph_53.add_edge(node_02, node_02, 1)
graph_53.add_edge(node_04, node_04, 3)
graph_53.add_edge(node_01, node_00, 20)
graph_53.add_edge(node_03, node_03, 1)
graph_53.add_edge(node_00, node_00, 8)
graph_53.add_edge(node_03, node_01, 1)
graph_53.add_edge(node_02, node_04, 18)
graph_53.add_edge(node_04, node_02, 2)
graph_53.add_edge(node_00, node_01, 18)
graph_53.add_edge(node_04, node_04, 5)
graph_53.add_edge(node_04, node_02, 2)
graph_53.add_edge(node_02, node_01, 18)
graph_53.add_edge(node_04, node_02, 13)
graph_53.add_edge(node_03, node_01, 9)
graph_53.add_edge(node_04, node_02, 11)
graph_53.add_edge(node_03, node_01, 17)
graph_53.add_edge(node_02, node_00, 19)
graph_53.add_edge(node_00, node_03, 5)

"""
	GRAPH 54
"""

graph_54 = Graph(True)

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

graph_54.add_edge(node_00, node_03, 2)
graph_54.add_edge(node_01, node_03, 6)
graph_54.add_edge(node_03, node_04, 20)
graph_54.add_edge(node_04, node_04, 12)
graph_54.add_edge(node_00, node_02, 16)
graph_54.add_edge(node_01, node_02, 9)
graph_54.add_edge(node_00, node_02, 14)
graph_54.add_edge(node_01, node_00, 2)
graph_54.add_edge(node_02, node_01, 9)
graph_54.add_edge(node_01, node_01, 2)
graph_54.add_edge(node_00, node_04, 3)
graph_54.add_edge(node_03, node_02, 11)
graph_54.add_edge(node_04, node_03, 8)
graph_54.add_edge(node_02, node_04, 8)
graph_54.add_edge(node_03, node_01, 4)
graph_54.add_edge(node_00, node_04, 12)
graph_54.add_edge(node_02, node_00, 8)
graph_54.add_edge(node_02, node_03, 10)
graph_54.add_edge(node_02, node_00, 7)
graph_54.add_edge(node_01, node_02, 5)

"""
	GRAPH 55
"""

graph_55 = Graph(True)

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

graph_55.add_edge(node_01, node_00, 7)
graph_55.add_edge(node_04, node_01, 15)
graph_55.add_edge(node_02, node_00, 20)
graph_55.add_edge(node_04, node_01, 10)
graph_55.add_edge(node_04, node_01, 2)
graph_55.add_edge(node_01, node_00, 3)
graph_55.add_edge(node_03, node_02, 4)
graph_55.add_edge(node_03, node_02, 6)
graph_55.add_edge(node_01, node_01, 14)
graph_55.add_edge(node_03, node_03, 14)
graph_55.add_edge(node_02, node_01, 4)
graph_55.add_edge(node_03, node_02, 16)
graph_55.add_edge(node_03, node_02, 10)
graph_55.add_edge(node_03, node_00, 16)
graph_55.add_edge(node_01, node_00, 8)
graph_55.add_edge(node_03, node_00, 14)
graph_55.add_edge(node_03, node_01, 10)
graph_55.add_edge(node_00, node_00, 3)
graph_55.add_edge(node_00, node_01, 12)
graph_55.add_edge(node_03, node_03, 15)

"""
	GRAPH 56
"""

graph_56 = Graph(True)

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

graph_56.add_edge(node_03, node_02, 20)
graph_56.add_edge(node_02, node_00, 4)
graph_56.add_edge(node_01, node_02, 10)
graph_56.add_edge(node_02, node_01, 17)
graph_56.add_edge(node_03, node_03, 9)
graph_56.add_edge(node_04, node_03, 13)
graph_56.add_edge(node_02, node_00, 4)
graph_56.add_edge(node_02, node_01, 13)
graph_56.add_edge(node_04, node_03, 20)
graph_56.add_edge(node_03, node_04, 4)
graph_56.add_edge(node_00, node_02, 14)
graph_56.add_edge(node_03, node_03, 15)
graph_56.add_edge(node_02, node_04, 5)
graph_56.add_edge(node_00, node_04, 11)
graph_56.add_edge(node_03, node_00, 8)
graph_56.add_edge(node_00, node_03, 11)
graph_56.add_edge(node_02, node_04, 20)
graph_56.add_edge(node_01, node_04, 18)
graph_56.add_edge(node_01, node_00, 19)
graph_56.add_edge(node_04, node_01, 7)

"""
	GRAPH 57
"""

graph_57 = Graph(True)

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

graph_57.add_edge(node_02, node_04, 13)
graph_57.add_edge(node_03, node_01, 13)
graph_57.add_edge(node_02, node_02, 3)
graph_57.add_edge(node_01, node_01, 16)
graph_57.add_edge(node_02, node_04, 7)
graph_57.add_edge(node_03, node_03, 15)
graph_57.add_edge(node_04, node_00, 8)
graph_57.add_edge(node_02, node_04, 9)
graph_57.add_edge(node_00, node_00, 13)
graph_57.add_edge(node_00, node_02, 15)
graph_57.add_edge(node_02, node_03, 4)
graph_57.add_edge(node_01, node_03, 2)
graph_57.add_edge(node_01, node_01, 12)
graph_57.add_edge(node_01, node_04, 15)
graph_57.add_edge(node_00, node_01, 4)
graph_57.add_edge(node_01, node_04, 12)
graph_57.add_edge(node_02, node_04, 8)
graph_57.add_edge(node_00, node_04, 1)
graph_57.add_edge(node_01, node_01, 18)
graph_57.add_edge(node_01, node_02, 18)

"""
	GRAPH 58
"""

graph_58 = Graph(True)

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

graph_58.add_edge(node_03, node_04, 2)
graph_58.add_edge(node_01, node_01, 16)
graph_58.add_edge(node_04, node_02, 3)
graph_58.add_edge(node_03, node_01, 7)
graph_58.add_edge(node_01, node_03, 14)
graph_58.add_edge(node_01, node_02, 13)
graph_58.add_edge(node_02, node_02, 11)
graph_58.add_edge(node_01, node_03, 1)
graph_58.add_edge(node_04, node_00, 13)
graph_58.add_edge(node_00, node_02, 3)
graph_58.add_edge(node_01, node_01, 12)
graph_58.add_edge(node_02, node_01, 11)
graph_58.add_edge(node_01, node_04, 7)
graph_58.add_edge(node_00, node_04, 11)
graph_58.add_edge(node_01, node_00, 3)
graph_58.add_edge(node_00, node_03, 2)
graph_58.add_edge(node_03, node_01, 1)
graph_58.add_edge(node_04, node_03, 16)
graph_58.add_edge(node_04, node_02, 3)
graph_58.add_edge(node_04, node_00, 10)

"""
	GRAPH 59
"""

graph_59 = Graph(True)

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

graph_59.add_edge(node_00, node_01, 14)
graph_59.add_edge(node_02, node_02, 12)
graph_59.add_edge(node_00, node_03, 15)
graph_59.add_edge(node_00, node_04, 10)
graph_59.add_edge(node_02, node_00, 2)
graph_59.add_edge(node_02, node_04, 12)
graph_59.add_edge(node_04, node_02, 8)
graph_59.add_edge(node_04, node_04, 17)
graph_59.add_edge(node_00, node_02, 2)
graph_59.add_edge(node_04, node_03, 17)
graph_59.add_edge(node_00, node_00, 4)
graph_59.add_edge(node_01, node_02, 15)
graph_59.add_edge(node_03, node_01, 10)
graph_59.add_edge(node_01, node_04, 3)
graph_59.add_edge(node_01, node_04, 12)
graph_59.add_edge(node_04, node_03, 12)
graph_59.add_edge(node_00, node_02, 19)
graph_59.add_edge(node_03, node_01, 3)
graph_59.add_edge(node_04, node_02, 6)
graph_59.add_edge(node_04, node_02, 15)

"""
	GRAPH 60
"""

graph_60 = Graph(True)

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

graph_60.add_edge(node_01, node_00, 5)
graph_60.add_edge(node_00, node_02, 5)
graph_60.add_edge(node_01, node_00, 13)
graph_60.add_edge(node_00, node_03, 10)
graph_60.add_edge(node_03, node_00, 15)
graph_60.add_edge(node_04, node_03, 1)
graph_60.add_edge(node_01, node_00, 5)
graph_60.add_edge(node_02, node_01, 1)
graph_60.add_edge(node_01, node_03, 10)
graph_60.add_edge(node_04, node_03, 5)
graph_60.add_edge(node_03, node_01, 20)
graph_60.add_edge(node_01, node_03, 7)
graph_60.add_edge(node_01, node_00, 7)
graph_60.add_edge(node_00, node_00, 19)
graph_60.add_edge(node_00, node_04, 17)
graph_60.add_edge(node_00, node_04, 13)
graph_60.add_edge(node_04, node_04, 18)
graph_60.add_edge(node_04, node_03, 7)
graph_60.add_edge(node_02, node_03, 18)
graph_60.add_edge(node_02, node_04, 20)

"""
	GRAPH 61
"""

graph_61 = Graph(True)

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

graph_61.add_edge(node_03, node_00, 8)
graph_61.add_edge(node_01, node_00, 4)
graph_61.add_edge(node_04, node_01, 9)
graph_61.add_edge(node_01, node_02, 19)
graph_61.add_edge(node_01, node_04, 1)
graph_61.add_edge(node_04, node_02, 7)
graph_61.add_edge(node_03, node_03, 5)
graph_61.add_edge(node_04, node_02, 9)
graph_61.add_edge(node_04, node_03, 7)
graph_61.add_edge(node_02, node_03, 5)
graph_61.add_edge(node_04, node_04, 1)
graph_61.add_edge(node_01, node_03, 17)
graph_61.add_edge(node_00, node_01, 14)
graph_61.add_edge(node_04, node_03, 6)
graph_61.add_edge(node_04, node_02, 14)
graph_61.add_edge(node_03, node_04, 19)
graph_61.add_edge(node_02, node_01, 1)
graph_61.add_edge(node_03, node_00, 1)
graph_61.add_edge(node_03, node_03, 9)
graph_61.add_edge(node_03, node_04, 8)

"""
	GRAPH 62
"""

graph_62 = Graph(True)

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

graph_62.add_edge(node_01, node_02, 12)
graph_62.add_edge(node_03, node_02, 11)
graph_62.add_edge(node_00, node_02, 12)
graph_62.add_edge(node_01, node_02, 12)
graph_62.add_edge(node_00, node_04, 4)
graph_62.add_edge(node_02, node_03, 19)
graph_62.add_edge(node_00, node_03, 19)
graph_62.add_edge(node_00, node_01, 2)
graph_62.add_edge(node_02, node_02, 19)
graph_62.add_edge(node_03, node_02, 6)
graph_62.add_edge(node_00, node_03, 3)
graph_62.add_edge(node_02, node_03, 1)
graph_62.add_edge(node_02, node_04, 2)
graph_62.add_edge(node_00, node_00, 12)
graph_62.add_edge(node_03, node_00, 18)
graph_62.add_edge(node_01, node_04, 2)
graph_62.add_edge(node_02, node_03, 20)
graph_62.add_edge(node_01, node_04, 16)
graph_62.add_edge(node_02, node_02, 2)
graph_62.add_edge(node_02, node_02, 9)

"""
	GRAPH 63
"""

graph_63 = Graph(True)

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

graph_63.add_edge(node_03, node_00, 19)
graph_63.add_edge(node_04, node_00, 5)
graph_63.add_edge(node_02, node_04, 18)
graph_63.add_edge(node_03, node_03, 20)
graph_63.add_edge(node_01, node_04, 7)
graph_63.add_edge(node_01, node_03, 15)
graph_63.add_edge(node_04, node_00, 1)
graph_63.add_edge(node_03, node_04, 11)
graph_63.add_edge(node_04, node_04, 13)
graph_63.add_edge(node_02, node_00, 14)
graph_63.add_edge(node_03, node_03, 3)
graph_63.add_edge(node_03, node_02, 20)
graph_63.add_edge(node_01, node_04, 5)
graph_63.add_edge(node_02, node_00, 10)
graph_63.add_edge(node_03, node_01, 7)
graph_63.add_edge(node_04, node_04, 6)
graph_63.add_edge(node_02, node_01, 13)
graph_63.add_edge(node_04, node_01, 14)
graph_63.add_edge(node_02, node_02, 3)
graph_63.add_edge(node_01, node_02, 8)

"""
	GRAPH 64
"""

graph_64 = Graph(True)

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

graph_64.add_edge(node_00, node_00, 18)
graph_64.add_edge(node_00, node_04, 14)
graph_64.add_edge(node_03, node_04, 19)
graph_64.add_edge(node_01, node_01, 6)
graph_64.add_edge(node_04, node_01, 18)
graph_64.add_edge(node_01, node_03, 18)
graph_64.add_edge(node_01, node_00, 10)
graph_64.add_edge(node_02, node_03, 17)
graph_64.add_edge(node_03, node_02, 18)
graph_64.add_edge(node_02, node_00, 8)
graph_64.add_edge(node_03, node_04, 20)
graph_64.add_edge(node_04, node_00, 3)
graph_64.add_edge(node_00, node_04, 6)
graph_64.add_edge(node_02, node_04, 2)
graph_64.add_edge(node_04, node_04, 4)
graph_64.add_edge(node_01, node_02, 11)
graph_64.add_edge(node_01, node_04, 11)
graph_64.add_edge(node_02, node_02, 1)
graph_64.add_edge(node_04, node_03, 12)
graph_64.add_edge(node_04, node_03, 19)

"""
	GRAPH 65
"""

graph_65 = Graph(True)

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

graph_65.add_edge(node_00, node_01, 15)
graph_65.add_edge(node_03, node_04, 13)
graph_65.add_edge(node_02, node_04, 10)
graph_65.add_edge(node_03, node_00, 16)
graph_65.add_edge(node_00, node_02, 17)
graph_65.add_edge(node_00, node_00, 13)
graph_65.add_edge(node_02, node_04, 13)
graph_65.add_edge(node_03, node_02, 19)
graph_65.add_edge(node_04, node_00, 18)
graph_65.add_edge(node_04, node_00, 16)
graph_65.add_edge(node_00, node_01, 3)
graph_65.add_edge(node_00, node_02, 9)
graph_65.add_edge(node_03, node_03, 2)
graph_65.add_edge(node_01, node_02, 8)
graph_65.add_edge(node_02, node_02, 16)
graph_65.add_edge(node_00, node_03, 4)
graph_65.add_edge(node_03, node_00, 20)
graph_65.add_edge(node_01, node_01, 20)
graph_65.add_edge(node_01, node_03, 3)
graph_65.add_edge(node_02, node_02, 5)

"""
	GRAPH 66
"""

graph_66 = Graph(True)

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

graph_66.add_edge(node_00, node_04, 20)
graph_66.add_edge(node_04, node_00, 12)
graph_66.add_edge(node_03, node_01, 13)
graph_66.add_edge(node_02, node_04, 4)
graph_66.add_edge(node_03, node_03, 7)
graph_66.add_edge(node_00, node_00, 8)
graph_66.add_edge(node_01, node_03, 2)
graph_66.add_edge(node_03, node_04, 15)
graph_66.add_edge(node_02, node_04, 7)
graph_66.add_edge(node_01, node_04, 4)
graph_66.add_edge(node_01, node_03, 7)
graph_66.add_edge(node_01, node_02, 9)
graph_66.add_edge(node_04, node_04, 6)
graph_66.add_edge(node_04, node_04, 13)
graph_66.add_edge(node_03, node_02, 13)
graph_66.add_edge(node_03, node_03, 3)
graph_66.add_edge(node_00, node_04, 11)
graph_66.add_edge(node_00, node_03, 17)
graph_66.add_edge(node_04, node_00, 1)
graph_66.add_edge(node_01, node_01, 12)

"""
	GRAPH 67
"""

graph_67 = Graph(True)

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

graph_67.add_edge(node_00, node_04, 9)
graph_67.add_edge(node_00, node_02, 18)
graph_67.add_edge(node_01, node_01, 15)
graph_67.add_edge(node_02, node_02, 11)
graph_67.add_edge(node_02, node_03, 3)
graph_67.add_edge(node_03, node_02, 4)
graph_67.add_edge(node_01, node_04, 2)
graph_67.add_edge(node_04, node_00, 7)
graph_67.add_edge(node_02, node_04, 8)
graph_67.add_edge(node_04, node_04, 9)
graph_67.add_edge(node_04, node_00, 5)
graph_67.add_edge(node_03, node_03, 14)
graph_67.add_edge(node_01, node_02, 5)
graph_67.add_edge(node_00, node_00, 2)
graph_67.add_edge(node_04, node_04, 19)
graph_67.add_edge(node_01, node_04, 8)
graph_67.add_edge(node_01, node_01, 20)
graph_67.add_edge(node_01, node_03, 7)
graph_67.add_edge(node_03, node_01, 3)
graph_67.add_edge(node_04, node_00, 16)

"""
	GRAPH 68
"""

graph_68 = Graph(True)

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

graph_68.add_edge(node_00, node_03, 8)
graph_68.add_edge(node_04, node_03, 6)
graph_68.add_edge(node_00, node_00, 13)
graph_68.add_edge(node_01, node_00, 8)
graph_68.add_edge(node_04, node_01, 6)
graph_68.add_edge(node_04, node_03, 14)
graph_68.add_edge(node_03, node_02, 2)
graph_68.add_edge(node_02, node_04, 11)
graph_68.add_edge(node_03, node_02, 15)
graph_68.add_edge(node_03, node_04, 18)
graph_68.add_edge(node_03, node_04, 10)
graph_68.add_edge(node_00, node_04, 18)
graph_68.add_edge(node_04, node_00, 17)
graph_68.add_edge(node_00, node_02, 9)
graph_68.add_edge(node_01, node_00, 3)
graph_68.add_edge(node_00, node_02, 12)
graph_68.add_edge(node_03, node_04, 3)
graph_68.add_edge(node_04, node_03, 16)
graph_68.add_edge(node_00, node_03, 3)
graph_68.add_edge(node_01, node_02, 17)

"""
	GRAPH 69
"""

graph_69 = Graph(True)

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

graph_69.add_edge(node_00, node_04, 11)
graph_69.add_edge(node_04, node_04, 1)
graph_69.add_edge(node_02, node_00, 6)
graph_69.add_edge(node_02, node_04, 5)
graph_69.add_edge(node_00, node_04, 20)
graph_69.add_edge(node_01, node_00, 16)
graph_69.add_edge(node_01, node_01, 16)
graph_69.add_edge(node_01, node_03, 13)
graph_69.add_edge(node_02, node_00, 1)
graph_69.add_edge(node_04, node_01, 5)
graph_69.add_edge(node_02, node_04, 13)
graph_69.add_edge(node_02, node_00, 8)
graph_69.add_edge(node_03, node_00, 5)
graph_69.add_edge(node_01, node_02, 5)
graph_69.add_edge(node_03, node_01, 3)
graph_69.add_edge(node_01, node_00, 20)
graph_69.add_edge(node_01, node_02, 10)
graph_69.add_edge(node_03, node_04, 4)
graph_69.add_edge(node_01, node_03, 17)
graph_69.add_edge(node_03, node_01, 13)

"""
	GRAPH 70
"""

graph_70 = Graph(True)

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

graph_70.add_edge(node_03, node_03, 4)
graph_70.add_edge(node_04, node_03, 5)
graph_70.add_edge(node_00, node_02, 1)
graph_70.add_edge(node_04, node_00, 11)
graph_70.add_edge(node_03, node_01, 7)
graph_70.add_edge(node_00, node_00, 2)
graph_70.add_edge(node_03, node_03, 14)
graph_70.add_edge(node_03, node_03, 7)
graph_70.add_edge(node_02, node_00, 2)
graph_70.add_edge(node_00, node_03, 20)
graph_70.add_edge(node_03, node_04, 16)
graph_70.add_edge(node_03, node_03, 8)
graph_70.add_edge(node_03, node_02, 15)
graph_70.add_edge(node_02, node_03, 10)
graph_70.add_edge(node_02, node_04, 4)
graph_70.add_edge(node_04, node_02, 20)
graph_70.add_edge(node_00, node_02, 10)
graph_70.add_edge(node_04, node_01, 6)
graph_70.add_edge(node_00, node_04, 5)
graph_70.add_edge(node_03, node_01, 19)

"""
	GRAPH 71
"""

graph_71 = Graph(True)

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

graph_71.add_edge(node_04, node_01, 3)
graph_71.add_edge(node_02, node_03, 16)
graph_71.add_edge(node_04, node_03, 16)
graph_71.add_edge(node_01, node_01, 6)
graph_71.add_edge(node_00, node_00, 5)
graph_71.add_edge(node_01, node_02, 18)
graph_71.add_edge(node_04, node_03, 14)
graph_71.add_edge(node_01, node_01, 11)
graph_71.add_edge(node_01, node_04, 15)
graph_71.add_edge(node_02, node_04, 4)
graph_71.add_edge(node_00, node_00, 13)
graph_71.add_edge(node_02, node_02, 9)
graph_71.add_edge(node_00, node_00, 13)
graph_71.add_edge(node_00, node_04, 9)
graph_71.add_edge(node_03, node_04, 16)
graph_71.add_edge(node_04, node_01, 5)
graph_71.add_edge(node_04, node_02, 17)
graph_71.add_edge(node_04, node_03, 13)
graph_71.add_edge(node_04, node_04, 5)
graph_71.add_edge(node_03, node_01, 2)

"""
	GRAPH 72
"""

graph_72 = Graph(True)

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

graph_72.add_edge(node_00, node_04, 3)
graph_72.add_edge(node_00, node_02, 11)
graph_72.add_edge(node_02, node_03, 11)
graph_72.add_edge(node_02, node_01, 15)
graph_72.add_edge(node_03, node_00, 6)
graph_72.add_edge(node_01, node_01, 15)
graph_72.add_edge(node_02, node_04, 3)
graph_72.add_edge(node_03, node_02, 11)
graph_72.add_edge(node_04, node_02, 14)
graph_72.add_edge(node_04, node_00, 11)
graph_72.add_edge(node_00, node_01, 5)
graph_72.add_edge(node_04, node_01, 1)
graph_72.add_edge(node_02, node_00, 17)
graph_72.add_edge(node_02, node_03, 13)
graph_72.add_edge(node_04, node_02, 20)
graph_72.add_edge(node_02, node_02, 19)
graph_72.add_edge(node_02, node_04, 13)
graph_72.add_edge(node_00, node_03, 17)
graph_72.add_edge(node_00, node_02, 6)
graph_72.add_edge(node_04, node_02, 9)

"""
	GRAPH 73
"""

graph_73 = Graph(True)

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

graph_73.add_edge(node_03, node_03, 7)
graph_73.add_edge(node_04, node_04, 14)
graph_73.add_edge(node_01, node_00, 18)
graph_73.add_edge(node_00, node_01, 16)
graph_73.add_edge(node_00, node_01, 17)
graph_73.add_edge(node_03, node_00, 10)
graph_73.add_edge(node_04, node_03, 3)
graph_73.add_edge(node_04, node_04, 20)
graph_73.add_edge(node_03, node_01, 15)
graph_73.add_edge(node_02, node_04, 13)
graph_73.add_edge(node_03, node_01, 2)
graph_73.add_edge(node_04, node_04, 5)
graph_73.add_edge(node_00, node_00, 6)
graph_73.add_edge(node_01, node_03, 19)
graph_73.add_edge(node_02, node_01, 16)
graph_73.add_edge(node_01, node_00, 5)
graph_73.add_edge(node_02, node_01, 16)
graph_73.add_edge(node_04, node_03, 2)
graph_73.add_edge(node_00, node_02, 4)
graph_73.add_edge(node_02, node_00, 15)

"""
	GRAPH 74
"""

graph_74 = Graph(True)

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

graph_74.add_edge(node_00, node_00, 17)
graph_74.add_edge(node_04, node_00, 7)
graph_74.add_edge(node_02, node_03, 9)
graph_74.add_edge(node_02, node_03, 14)
graph_74.add_edge(node_00, node_02, 6)
graph_74.add_edge(node_01, node_01, 19)
graph_74.add_edge(node_03, node_02, 14)
graph_74.add_edge(node_02, node_01, 1)
graph_74.add_edge(node_02, node_03, 2)
graph_74.add_edge(node_02, node_00, 9)
graph_74.add_edge(node_04, node_03, 9)
graph_74.add_edge(node_02, node_02, 20)
graph_74.add_edge(node_02, node_04, 5)
graph_74.add_edge(node_00, node_00, 8)
graph_74.add_edge(node_00, node_01, 2)
graph_74.add_edge(node_00, node_00, 14)
graph_74.add_edge(node_04, node_02, 7)
graph_74.add_edge(node_01, node_02, 1)
graph_74.add_edge(node_00, node_01, 2)
graph_74.add_edge(node_01, node_04, 17)

"""
	GRAPH 75
"""

graph_75 = Graph(True)

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

graph_75.add_edge(node_00, node_01, 16)
graph_75.add_edge(node_02, node_04, 16)
graph_75.add_edge(node_00, node_01, 1)
graph_75.add_edge(node_02, node_01, 20)
graph_75.add_edge(node_01, node_01, 11)
graph_75.add_edge(node_03, node_03, 11)
graph_75.add_edge(node_03, node_02, 18)
graph_75.add_edge(node_03, node_01, 17)
graph_75.add_edge(node_02, node_00, 12)
graph_75.add_edge(node_02, node_01, 11)
graph_75.add_edge(node_04, node_04, 3)
graph_75.add_edge(node_04, node_03, 9)
graph_75.add_edge(node_00, node_01, 13)
graph_75.add_edge(node_01, node_00, 16)
graph_75.add_edge(node_04, node_00, 19)
graph_75.add_edge(node_03, node_04, 2)
graph_75.add_edge(node_03, node_02, 17)
graph_75.add_edge(node_02, node_04, 11)
graph_75.add_edge(node_03, node_00, 15)
graph_75.add_edge(node_01, node_04, 11)

"""
	GRAPH 76
"""

graph_76 = Graph(True)

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

graph_76.add_edge(node_02, node_02, 5)
graph_76.add_edge(node_03, node_04, 5)
graph_76.add_edge(node_02, node_00, 13)
graph_76.add_edge(node_02, node_00, 5)
graph_76.add_edge(node_02, node_00, 15)
graph_76.add_edge(node_03, node_01, 2)
graph_76.add_edge(node_02, node_00, 5)
graph_76.add_edge(node_03, node_02, 14)
graph_76.add_edge(node_01, node_04, 16)
graph_76.add_edge(node_02, node_00, 12)
graph_76.add_edge(node_04, node_03, 13)
graph_76.add_edge(node_02, node_03, 6)
graph_76.add_edge(node_00, node_04, 13)
graph_76.add_edge(node_00, node_00, 12)
graph_76.add_edge(node_00, node_03, 9)
graph_76.add_edge(node_03, node_03, 15)
graph_76.add_edge(node_04, node_01, 4)
graph_76.add_edge(node_04, node_00, 15)
graph_76.add_edge(node_04, node_04, 11)
graph_76.add_edge(node_03, node_00, 20)

"""
	GRAPH 77
"""

graph_77 = Graph(True)

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

graph_77.add_edge(node_04, node_03, 10)
graph_77.add_edge(node_00, node_04, 10)
graph_77.add_edge(node_01, node_01, 18)
graph_77.add_edge(node_01, node_00, 12)
graph_77.add_edge(node_04, node_00, 4)
graph_77.add_edge(node_02, node_00, 11)
graph_77.add_edge(node_03, node_00, 7)
graph_77.add_edge(node_04, node_02, 10)
graph_77.add_edge(node_00, node_01, 2)
graph_77.add_edge(node_02, node_03, 16)
graph_77.add_edge(node_00, node_02, 4)
graph_77.add_edge(node_04, node_01, 11)
graph_77.add_edge(node_01, node_03, 15)
graph_77.add_edge(node_00, node_00, 15)
graph_77.add_edge(node_02, node_04, 17)
graph_77.add_edge(node_01, node_02, 3)
graph_77.add_edge(node_04, node_02, 4)
graph_77.add_edge(node_02, node_01, 3)
graph_77.add_edge(node_00, node_01, 6)
graph_77.add_edge(node_00, node_01, 7)

"""
	GRAPH 78
"""

graph_78 = Graph(True)

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

graph_78.add_edge(node_02, node_03, 4)
graph_78.add_edge(node_04, node_02, 4)
graph_78.add_edge(node_02, node_03, 10)
graph_78.add_edge(node_00, node_03, 20)
graph_78.add_edge(node_01, node_01, 17)
graph_78.add_edge(node_01, node_00, 6)
graph_78.add_edge(node_03, node_03, 16)
graph_78.add_edge(node_04, node_02, 14)
graph_78.add_edge(node_00, node_04, 19)
graph_78.add_edge(node_03, node_02, 9)
graph_78.add_edge(node_04, node_03, 3)
graph_78.add_edge(node_04, node_00, 10)
graph_78.add_edge(node_01, node_03, 11)
graph_78.add_edge(node_03, node_03, 9)
graph_78.add_edge(node_04, node_00, 11)
graph_78.add_edge(node_03, node_04, 3)
graph_78.add_edge(node_01, node_00, 19)
graph_78.add_edge(node_00, node_02, 11)
graph_78.add_edge(node_03, node_02, 12)
graph_78.add_edge(node_01, node_01, 12)

"""
	GRAPH 79
"""

graph_79 = Graph(True)

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

graph_79.add_edge(node_00, node_01, 19)
graph_79.add_edge(node_04, node_00, 18)
graph_79.add_edge(node_04, node_03, 12)
graph_79.add_edge(node_04, node_01, 12)
graph_79.add_edge(node_01, node_04, 1)
graph_79.add_edge(node_01, node_00, 10)
graph_79.add_edge(node_02, node_00, 19)
graph_79.add_edge(node_03, node_02, 8)
graph_79.add_edge(node_02, node_00, 18)
graph_79.add_edge(node_00, node_00, 11)
graph_79.add_edge(node_02, node_02, 15)
graph_79.add_edge(node_01, node_03, 6)
graph_79.add_edge(node_03, node_03, 12)
graph_79.add_edge(node_04, node_02, 18)
graph_79.add_edge(node_00, node_04, 13)
graph_79.add_edge(node_02, node_02, 3)
graph_79.add_edge(node_04, node_01, 5)
graph_79.add_edge(node_01, node_00, 18)
graph_79.add_edge(node_03, node_02, 19)
graph_79.add_edge(node_01, node_02, 16)

"""
	GRAPH 80
"""

graph_80 = Graph(True)

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

graph_80.add_edge(node_00, node_04, 7)
graph_80.add_edge(node_00, node_03, 6)
graph_80.add_edge(node_02, node_02, 8)
graph_80.add_edge(node_02, node_04, 10)
graph_80.add_edge(node_01, node_03, 6)
graph_80.add_edge(node_00, node_03, 16)
graph_80.add_edge(node_00, node_04, 20)
graph_80.add_edge(node_03, node_03, 18)
graph_80.add_edge(node_01, node_00, 16)
graph_80.add_edge(node_03, node_03, 17)
graph_80.add_edge(node_02, node_02, 1)
graph_80.add_edge(node_04, node_04, 8)
graph_80.add_edge(node_02, node_02, 5)
graph_80.add_edge(node_01, node_01, 4)
graph_80.add_edge(node_02, node_03, 3)
graph_80.add_edge(node_03, node_04, 7)
graph_80.add_edge(node_04, node_01, 16)
graph_80.add_edge(node_02, node_00, 20)
graph_80.add_edge(node_03, node_02, 18)
graph_80.add_edge(node_03, node_01, 20)

"""
	GRAPH 81
"""

graph_81 = Graph(True)

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

graph_81.add_edge(node_04, node_01, 11)
graph_81.add_edge(node_01, node_00, 20)
graph_81.add_edge(node_00, node_04, 6)
graph_81.add_edge(node_03, node_03, 20)
graph_81.add_edge(node_02, node_03, 17)
graph_81.add_edge(node_04, node_03, 2)
graph_81.add_edge(node_00, node_04, 20)
graph_81.add_edge(node_02, node_00, 19)
graph_81.add_edge(node_03, node_02, 17)
graph_81.add_edge(node_04, node_04, 19)
graph_81.add_edge(node_00, node_04, 14)
graph_81.add_edge(node_03, node_01, 12)
graph_81.add_edge(node_02, node_02, 7)
graph_81.add_edge(node_02, node_03, 10)
graph_81.add_edge(node_03, node_04, 2)
graph_81.add_edge(node_01, node_04, 13)
graph_81.add_edge(node_04, node_00, 16)
graph_81.add_edge(node_00, node_04, 11)
graph_81.add_edge(node_03, node_04, 11)
graph_81.add_edge(node_01, node_04, 17)

"""
	GRAPH 82
"""

graph_82 = Graph(True)

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

graph_82.add_edge(node_01, node_01, 15)
graph_82.add_edge(node_02, node_04, 10)
graph_82.add_edge(node_00, node_04, 8)
graph_82.add_edge(node_03, node_02, 9)
graph_82.add_edge(node_00, node_03, 15)
graph_82.add_edge(node_02, node_01, 7)
graph_82.add_edge(node_00, node_00, 17)
graph_82.add_edge(node_04, node_02, 1)
graph_82.add_edge(node_01, node_02, 2)
graph_82.add_edge(node_00, node_04, 10)
graph_82.add_edge(node_04, node_00, 11)
graph_82.add_edge(node_01, node_03, 6)
graph_82.add_edge(node_04, node_01, 19)
graph_82.add_edge(node_02, node_02, 4)
graph_82.add_edge(node_01, node_00, 19)
graph_82.add_edge(node_01, node_01, 11)
graph_82.add_edge(node_01, node_04, 11)
graph_82.add_edge(node_02, node_04, 12)
graph_82.add_edge(node_01, node_03, 1)
graph_82.add_edge(node_00, node_00, 15)

"""
	GRAPH 83
"""

graph_83 = Graph(True)

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

graph_83.add_edge(node_00, node_02, 3)
graph_83.add_edge(node_03, node_03, 13)
graph_83.add_edge(node_03, node_02, 20)
graph_83.add_edge(node_03, node_04, 19)
graph_83.add_edge(node_04, node_02, 20)
graph_83.add_edge(node_02, node_01, 11)
graph_83.add_edge(node_01, node_03, 2)
graph_83.add_edge(node_02, node_02, 11)
graph_83.add_edge(node_04, node_01, 3)
graph_83.add_edge(node_00, node_01, 16)
graph_83.add_edge(node_03, node_03, 17)
graph_83.add_edge(node_04, node_03, 9)
graph_83.add_edge(node_01, node_01, 9)
graph_83.add_edge(node_02, node_03, 10)
graph_83.add_edge(node_04, node_04, 12)
graph_83.add_edge(node_00, node_02, 6)
graph_83.add_edge(node_03, node_01, 7)
graph_83.add_edge(node_02, node_00, 2)
graph_83.add_edge(node_01, node_00, 4)
graph_83.add_edge(node_03, node_03, 4)

"""
	GRAPH 84
"""

graph_84 = Graph(True)

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

graph_84.add_edge(node_04, node_02, 12)
graph_84.add_edge(node_04, node_04, 13)
graph_84.add_edge(node_04, node_01, 4)
graph_84.add_edge(node_03, node_03, 5)
graph_84.add_edge(node_01, node_00, 4)
graph_84.add_edge(node_01, node_00, 6)
graph_84.add_edge(node_04, node_00, 9)
graph_84.add_edge(node_04, node_01, 9)
graph_84.add_edge(node_02, node_04, 1)
graph_84.add_edge(node_03, node_01, 15)
graph_84.add_edge(node_03, node_02, 4)
graph_84.add_edge(node_01, node_04, 17)
graph_84.add_edge(node_02, node_01, 14)
graph_84.add_edge(node_02, node_03, 18)
graph_84.add_edge(node_02, node_01, 3)
graph_84.add_edge(node_03, node_02, 5)
graph_84.add_edge(node_04, node_01, 15)
graph_84.add_edge(node_02, node_03, 3)
graph_84.add_edge(node_04, node_03, 7)
graph_84.add_edge(node_01, node_04, 9)

"""
	GRAPH 85
"""

graph_85 = Graph(True)

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

graph_85.add_edge(node_03, node_02, 1)
graph_85.add_edge(node_02, node_00, 15)
graph_85.add_edge(node_04, node_02, 3)
graph_85.add_edge(node_01, node_02, 9)
graph_85.add_edge(node_02, node_02, 8)
graph_85.add_edge(node_04, node_02, 6)
graph_85.add_edge(node_00, node_02, 8)
graph_85.add_edge(node_03, node_04, 14)
graph_85.add_edge(node_02, node_00, 20)
graph_85.add_edge(node_03, node_02, 12)
graph_85.add_edge(node_02, node_04, 5)
graph_85.add_edge(node_04, node_02, 10)
graph_85.add_edge(node_02, node_01, 17)
graph_85.add_edge(node_02, node_04, 10)
graph_85.add_edge(node_03, node_03, 14)
graph_85.add_edge(node_04, node_02, 18)
graph_85.add_edge(node_03, node_02, 16)
graph_85.add_edge(node_04, node_00, 16)
graph_85.add_edge(node_03, node_01, 18)
graph_85.add_edge(node_02, node_00, 11)

"""
	GRAPH 86
"""

graph_86 = Graph(True)

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

graph_86.add_edge(node_02, node_00, 15)
graph_86.add_edge(node_02, node_03, 6)
graph_86.add_edge(node_04, node_00, 18)
graph_86.add_edge(node_02, node_01, 3)
graph_86.add_edge(node_02, node_00, 18)
graph_86.add_edge(node_03, node_01, 20)
graph_86.add_edge(node_01, node_03, 17)
graph_86.add_edge(node_01, node_04, 17)
graph_86.add_edge(node_04, node_00, 17)
graph_86.add_edge(node_02, node_03, 15)
graph_86.add_edge(node_02, node_01, 8)
graph_86.add_edge(node_01, node_01, 1)
graph_86.add_edge(node_00, node_00, 3)
graph_86.add_edge(node_01, node_00, 9)
graph_86.add_edge(node_00, node_02, 17)
graph_86.add_edge(node_00, node_00, 4)
graph_86.add_edge(node_00, node_04, 19)
graph_86.add_edge(node_02, node_00, 19)
graph_86.add_edge(node_01, node_00, 13)
graph_86.add_edge(node_00, node_04, 2)

"""
	GRAPH 87
"""

graph_87 = Graph(True)

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

graph_87.add_edge(node_04, node_04, 11)
graph_87.add_edge(node_01, node_00, 4)
graph_87.add_edge(node_03, node_02, 13)
graph_87.add_edge(node_03, node_01, 7)
graph_87.add_edge(node_03, node_04, 17)
graph_87.add_edge(node_01, node_00, 6)
graph_87.add_edge(node_04, node_03, 11)
graph_87.add_edge(node_01, node_01, 1)
graph_87.add_edge(node_04, node_01, 15)
graph_87.add_edge(node_03, node_02, 7)
graph_87.add_edge(node_04, node_02, 11)
graph_87.add_edge(node_02, node_04, 6)
graph_87.add_edge(node_03, node_02, 6)
graph_87.add_edge(node_00, node_01, 7)
graph_87.add_edge(node_02, node_04, 17)
graph_87.add_edge(node_01, node_01, 19)
graph_87.add_edge(node_02, node_01, 13)
graph_87.add_edge(node_03, node_00, 15)
graph_87.add_edge(node_01, node_03, 18)
graph_87.add_edge(node_01, node_01, 5)

"""
	GRAPH 88
"""

graph_88 = Graph(True)

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

graph_88.add_edge(node_03, node_04, 13)
graph_88.add_edge(node_03, node_01, 20)
graph_88.add_edge(node_01, node_02, 1)
graph_88.add_edge(node_02, node_00, 2)
graph_88.add_edge(node_03, node_03, 12)
graph_88.add_edge(node_04, node_03, 20)
graph_88.add_edge(node_03, node_03, 16)
graph_88.add_edge(node_03, node_04, 15)
graph_88.add_edge(node_04, node_01, 12)
graph_88.add_edge(node_04, node_01, 12)
graph_88.add_edge(node_00, node_04, 7)
graph_88.add_edge(node_03, node_02, 18)
graph_88.add_edge(node_00, node_00, 7)
graph_88.add_edge(node_01, node_02, 16)
graph_88.add_edge(node_00, node_04, 4)
graph_88.add_edge(node_00, node_02, 17)
graph_88.add_edge(node_00, node_04, 20)
graph_88.add_edge(node_00, node_02, 11)
graph_88.add_edge(node_03, node_01, 5)
graph_88.add_edge(node_00, node_00, 15)

"""
	GRAPH 89
"""

graph_89 = Graph(True)

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

graph_89.add_edge(node_04, node_00, 9)
graph_89.add_edge(node_00, node_02, 6)
graph_89.add_edge(node_02, node_00, 13)
graph_89.add_edge(node_04, node_01, 9)
graph_89.add_edge(node_01, node_02, 6)
graph_89.add_edge(node_00, node_01, 4)
graph_89.add_edge(node_02, node_02, 11)
graph_89.add_edge(node_03, node_03, 3)
graph_89.add_edge(node_00, node_04, 12)
graph_89.add_edge(node_01, node_03, 2)
graph_89.add_edge(node_01, node_00, 18)
graph_89.add_edge(node_02, node_00, 7)
graph_89.add_edge(node_02, node_01, 15)
graph_89.add_edge(node_02, node_00, 7)
graph_89.add_edge(node_03, node_03, 13)
graph_89.add_edge(node_01, node_04, 15)
graph_89.add_edge(node_00, node_03, 12)
graph_89.add_edge(node_04, node_00, 8)
graph_89.add_edge(node_00, node_01, 17)
graph_89.add_edge(node_03, node_02, 16)

"""
	GRAPH 90
"""

graph_90 = Graph(True)

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

graph_90.add_edge(node_03, node_02, 5)
graph_90.add_edge(node_02, node_00, 3)
graph_90.add_edge(node_00, node_04, 17)
graph_90.add_edge(node_00, node_03, 14)
graph_90.add_edge(node_04, node_04, 16)
graph_90.add_edge(node_03, node_04, 8)
graph_90.add_edge(node_03, node_02, 6)
graph_90.add_edge(node_01, node_02, 18)
graph_90.add_edge(node_01, node_01, 12)
graph_90.add_edge(node_03, node_04, 4)
graph_90.add_edge(node_04, node_03, 4)
graph_90.add_edge(node_04, node_02, 9)
graph_90.add_edge(node_00, node_03, 20)
graph_90.add_edge(node_02, node_04, 12)
graph_90.add_edge(node_04, node_02, 17)
graph_90.add_edge(node_02, node_02, 7)
graph_90.add_edge(node_01, node_03, 5)
graph_90.add_edge(node_01, node_04, 16)
graph_90.add_edge(node_03, node_01, 1)
graph_90.add_edge(node_02, node_04, 1)

"""
	GRAPH 91
"""

graph_91 = Graph(True)

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

graph_91.add_edge(node_03, node_03, 19)
graph_91.add_edge(node_03, node_01, 3)
graph_91.add_edge(node_03, node_04, 12)
graph_91.add_edge(node_03, node_00, 1)
graph_91.add_edge(node_03, node_02, 19)
graph_91.add_edge(node_00, node_01, 15)
graph_91.add_edge(node_04, node_00, 8)
graph_91.add_edge(node_01, node_00, 12)
graph_91.add_edge(node_00, node_02, 3)
graph_91.add_edge(node_03, node_01, 7)
graph_91.add_edge(node_04, node_02, 19)
graph_91.add_edge(node_00, node_02, 9)
graph_91.add_edge(node_04, node_03, 15)
graph_91.add_edge(node_04, node_02, 6)
graph_91.add_edge(node_03, node_01, 3)
graph_91.add_edge(node_04, node_04, 16)
graph_91.add_edge(node_00, node_04, 10)
graph_91.add_edge(node_04, node_03, 16)
graph_91.add_edge(node_03, node_03, 11)
graph_91.add_edge(node_02, node_03, 3)

"""
	GRAPH 92
"""

graph_92 = Graph(True)

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

graph_92.add_edge(node_03, node_01, 9)
graph_92.add_edge(node_01, node_03, 11)
graph_92.add_edge(node_00, node_01, 17)
graph_92.add_edge(node_03, node_02, 11)
graph_92.add_edge(node_04, node_01, 19)
graph_92.add_edge(node_01, node_04, 12)
graph_92.add_edge(node_02, node_01, 16)
graph_92.add_edge(node_04, node_00, 20)
graph_92.add_edge(node_04, node_02, 5)
graph_92.add_edge(node_03, node_03, 19)
graph_92.add_edge(node_01, node_00, 14)
graph_92.add_edge(node_00, node_01, 10)
graph_92.add_edge(node_00, node_04, 15)
graph_92.add_edge(node_03, node_03, 4)
graph_92.add_edge(node_03, node_04, 20)
graph_92.add_edge(node_04, node_01, 5)
graph_92.add_edge(node_01, node_01, 13)
graph_92.add_edge(node_01, node_03, 4)
graph_92.add_edge(node_03, node_01, 20)
graph_92.add_edge(node_00, node_02, 4)

"""
	GRAPH 93
"""

graph_93 = Graph(True)

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

graph_93.add_edge(node_02, node_00, 19)
graph_93.add_edge(node_02, node_01, 17)
graph_93.add_edge(node_01, node_03, 20)
graph_93.add_edge(node_02, node_03, 19)
graph_93.add_edge(node_03, node_04, 15)
graph_93.add_edge(node_00, node_00, 12)
graph_93.add_edge(node_01, node_03, 10)
graph_93.add_edge(node_04, node_01, 18)
graph_93.add_edge(node_02, node_04, 20)
graph_93.add_edge(node_01, node_02, 2)
graph_93.add_edge(node_01, node_04, 1)
graph_93.add_edge(node_00, node_00, 8)
graph_93.add_edge(node_01, node_03, 15)
graph_93.add_edge(node_02, node_00, 5)
graph_93.add_edge(node_02, node_02, 11)
graph_93.add_edge(node_00, node_01, 18)
graph_93.add_edge(node_01, node_04, 12)
graph_93.add_edge(node_01, node_00, 11)
graph_93.add_edge(node_00, node_03, 13)
graph_93.add_edge(node_02, node_02, 14)

"""
	GRAPH 94
"""

graph_94 = Graph(True)

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

graph_94.add_edge(node_01, node_02, 8)
graph_94.add_edge(node_03, node_00, 4)
graph_94.add_edge(node_00, node_02, 14)
graph_94.add_edge(node_03, node_00, 2)
graph_94.add_edge(node_04, node_00, 7)
graph_94.add_edge(node_03, node_02, 11)
graph_94.add_edge(node_03, node_01, 19)
graph_94.add_edge(node_03, node_02, 20)
graph_94.add_edge(node_04, node_00, 1)
graph_94.add_edge(node_03, node_01, 1)
graph_94.add_edge(node_03, node_03, 6)
graph_94.add_edge(node_00, node_03, 3)
graph_94.add_edge(node_02, node_01, 9)
graph_94.add_edge(node_03, node_00, 19)
graph_94.add_edge(node_01, node_00, 8)
graph_94.add_edge(node_03, node_00, 2)
graph_94.add_edge(node_04, node_00, 13)
graph_94.add_edge(node_00, node_03, 19)
graph_94.add_edge(node_04, node_02, 3)
graph_94.add_edge(node_02, node_02, 12)

"""
	GRAPH 95
"""

graph_95 = Graph(True)

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

graph_95.add_edge(node_01, node_04, 10)
graph_95.add_edge(node_02, node_02, 5)
graph_95.add_edge(node_02, node_04, 12)
graph_95.add_edge(node_01, node_01, 13)
graph_95.add_edge(node_03, node_02, 2)
graph_95.add_edge(node_02, node_00, 18)
graph_95.add_edge(node_02, node_02, 17)
graph_95.add_edge(node_04, node_00, 2)
graph_95.add_edge(node_04, node_03, 10)
graph_95.add_edge(node_04, node_03, 14)
graph_95.add_edge(node_03, node_03, 5)
graph_95.add_edge(node_03, node_01, 4)
graph_95.add_edge(node_03, node_04, 15)
graph_95.add_edge(node_03, node_03, 20)
graph_95.add_edge(node_01, node_02, 16)
graph_95.add_edge(node_03, node_04, 9)
graph_95.add_edge(node_04, node_00, 17)
graph_95.add_edge(node_03, node_00, 13)
graph_95.add_edge(node_03, node_01, 3)
graph_95.add_edge(node_03, node_00, 9)

"""
	GRAPH 96
"""

graph_96 = Graph(True)

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

graph_96.add_edge(node_04, node_01, 16)
graph_96.add_edge(node_00, node_04, 15)
graph_96.add_edge(node_01, node_04, 3)
graph_96.add_edge(node_01, node_01, 1)
graph_96.add_edge(node_01, node_01, 6)
graph_96.add_edge(node_01, node_02, 13)
graph_96.add_edge(node_03, node_03, 7)
graph_96.add_edge(node_01, node_02, 1)
graph_96.add_edge(node_00, node_03, 19)
graph_96.add_edge(node_02, node_02, 12)
graph_96.add_edge(node_03, node_01, 12)
graph_96.add_edge(node_00, node_01, 13)
graph_96.add_edge(node_01, node_02, 15)
graph_96.add_edge(node_00, node_03, 20)
graph_96.add_edge(node_02, node_00, 18)
graph_96.add_edge(node_02, node_01, 17)
graph_96.add_edge(node_02, node_02, 1)
graph_96.add_edge(node_04, node_04, 11)
graph_96.add_edge(node_04, node_02, 11)
graph_96.add_edge(node_04, node_04, 18)

"""
	GRAPH 97
"""

graph_97 = Graph(True)

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

graph_97.add_edge(node_00, node_00, 20)
graph_97.add_edge(node_02, node_03, 19)
graph_97.add_edge(node_03, node_03, 15)
graph_97.add_edge(node_03, node_02, 10)
graph_97.add_edge(node_04, node_00, 5)
graph_97.add_edge(node_02, node_00, 9)
graph_97.add_edge(node_03, node_00, 20)
graph_97.add_edge(node_02, node_03, 11)
graph_97.add_edge(node_02, node_03, 3)
graph_97.add_edge(node_04, node_00, 4)
graph_97.add_edge(node_02, node_04, 10)
graph_97.add_edge(node_00, node_04, 17)
graph_97.add_edge(node_04, node_03, 9)
graph_97.add_edge(node_03, node_02, 14)
graph_97.add_edge(node_02, node_02, 1)
graph_97.add_edge(node_01, node_01, 15)
graph_97.add_edge(node_00, node_02, 15)
graph_97.add_edge(node_02, node_03, 3)
graph_97.add_edge(node_02, node_03, 19)
graph_97.add_edge(node_03, node_02, 8)

"""
	GRAPH 98
"""

graph_98 = Graph(True)

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

graph_98.add_edge(node_04, node_02, 13)
graph_98.add_edge(node_01, node_00, 19)
graph_98.add_edge(node_03, node_04, 5)
graph_98.add_edge(node_03, node_01, 17)
graph_98.add_edge(node_03, node_00, 11)
graph_98.add_edge(node_01, node_02, 10)
graph_98.add_edge(node_04, node_02, 19)
graph_98.add_edge(node_01, node_01, 11)
graph_98.add_edge(node_03, node_04, 6)
graph_98.add_edge(node_00, node_03, 18)
graph_98.add_edge(node_01, node_04, 1)
graph_98.add_edge(node_02, node_03, 18)
graph_98.add_edge(node_04, node_00, 10)
graph_98.add_edge(node_00, node_00, 7)
graph_98.add_edge(node_01, node_01, 16)
graph_98.add_edge(node_01, node_01, 4)
graph_98.add_edge(node_02, node_00, 5)
graph_98.add_edge(node_03, node_02, 3)
graph_98.add_edge(node_01, node_00, 3)
graph_98.add_edge(node_02, node_00, 20)

"""
	GRAPH 99
"""

graph_99 = Graph(True)

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

graph_99.add_edge(node_00, node_01, 8)
graph_99.add_edge(node_01, node_03, 9)
graph_99.add_edge(node_02, node_01, 7)
graph_99.add_edge(node_00, node_00, 20)
graph_99.add_edge(node_00, node_00, 9)
graph_99.add_edge(node_04, node_02, 10)
graph_99.add_edge(node_03, node_03, 17)
graph_99.add_edge(node_00, node_02, 18)
graph_99.add_edge(node_02, node_03, 2)
graph_99.add_edge(node_00, node_03, 12)
graph_99.add_edge(node_00, node_04, 6)
graph_99.add_edge(node_04, node_01, 12)
graph_99.add_edge(node_04, node_04, 12)
graph_99.add_edge(node_03, node_00, 17)
graph_99.add_edge(node_04, node_03, 14)
graph_99.add_edge(node_00, node_01, 14)
graph_99.add_edge(node_03, node_02, 16)
graph_99.add_edge(node_03, node_04, 14)
graph_99.add_edge(node_02, node_04, 7)
graph_99.add_edge(node_04, node_04, 20)

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
