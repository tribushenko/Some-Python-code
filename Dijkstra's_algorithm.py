graph = {"start": {"a": 6, "b": 2}, "a": {"fin": 1}, "b": {"a": 3, "fin": 5}, "fin": {}}
infinity = float("inf")
costs = {"a": 6, "b": 2, "fin": infinity}
parents = {"a": "start", "b": "start", "in": None}
processed = []
print(f"graph - {graph}\ncosts - {costs}\nparents - {parents}")


def find_lowest_cost_node(costs):
	lowest_cost = float("inf")  # means infinity
	lowest_cost_node = None  # declare a variable
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


def dijkstra_algorithm():
	node = find_lowest_cost_node(costs)  # finds the lowest cost node and adds it to the list of processed
	while node is not None:  # if all nodes are used, the function return None, what means that all nodes ended
		cost = costs[node]  # we take the cost of some node and how long it will take to get to that node cost -> int
		neighbors = graph[node]  # take the dictionary of neighbours with their cost if we wanna get from node to them
		for n in neighbors.keys():  # iterating neighbours nodes
			new_cost = cost + neighbors[n]  # new cost means the whole cost of node if we wanna to get from start
			if costs[n] > new_cost:  # we compare if cost of node is bigger than in costs is declared
				costs[n] = new_cost  # if new cost is less we change with previous cost
				parents[n] = node  # we change a parent for a neighbours.keys() if its cost bigger than declared costs
		processed.append(node)  # we mark it as processed node or used
		node = find_lowest_cost_node(costs)  # we find the lowest cost node again while all nodes are not processed
	return costs  # return new costs for nodes in graph (finding the shortest path)


print(f"costs - {costs}", dijkstra_algorithm(), sep="\n")  # the goal is to write a function that implement Dijkstra's
# algorithm
