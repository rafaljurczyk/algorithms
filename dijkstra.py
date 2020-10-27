#dijkstra.py
#I was inspired by Doug Mahugh and after I have studied his code I implemented it with a lot of similarities (https://github.com/dmahugh/dijkstra-algorithm)
#check his code!

from collections import deque


class Graph:
	def __init__(self, filename):
		self.graph_edges = []
		with open(filename) as f:
			for line in f:
				edge_from, edge_to, cost = line.strip().split(" ")
				self.graph_edges.append((edge_from, edge_to, float(cost)))

		self.nodes = set()
		for edge in self.graph_edges:
			self.nodes.update([edge[0], edge[1]])

		self.adjacency_list = {node: set() for node in self.nodes}
		for edge in self.graph_edges:
			self.adjacency_list[edge[0]].add((edge[1], edge[2]))


	def shortest_path(self, start_node, end_node):
		unvisited_nodes = self.nodes.copy()

		distance_from_start = {
			node: (0 if node == start_node else 999999) for node in self.nodes
		}

		previous_node = {node: None for node in self.nodes}
		while unvisited_nodes:
			current_node = min(unvisited_nodes, key=lambda node: distance_from_start[node])
			unvisited_nodes.remove(current_node)

			if distance_from_start[current_node] == 999999:
				break

			for neighbor, distance in self.adjacency_list[current_node]:
				new_path = distance_from_start[current_node] + distance
				if new_path < distance_from_start[neighbor]:
					distance_from_start[neighbor] = new_path
					previous_node[neighbor] = current_node

			if current_node == end_node:
				break

		path = deque()
		current_node = end_node
		while previous_node[current_node] is not None:
			path.appendleft(current_node)
			current_node = previous_node[current_node]
		path.appendleft(start_node)

		return path, distance_from_start[end_node]



def main():

	graph = Graph('dijkstra.txt')
	returned_path, returned_distance = graph.shortest_path('A', 'F')
	print(returned_path)
	print(returned_distance)

if __name__=="__main__":
	main()