#Dijkstra's algo

def find_cheapest_node(costs, visited, set_nodes):
	#node, cost
	unvisited_nodes = list(set_nodes - set(visited))	
	smallest_node = unvisited_nodes[0]
	smallest_cost = costs[smallest_node]
	for node in unvisited_nodes:
		if costs[node] < smallest_cost:
			smallest_cost = costs[node]
			smallest_node = node
	return smallest_node


def dijkstra(graph, costs, parents, last):
	set_nodes = set(costs.keys()) 
	visited = []
	set_nodes = set(costs.keys()) 
	visited = []
	while set(visited) != set_nodes:
		cn = find_cheapest_node(costs, visited, set_nodes) #find the cheapest that haven't been visited
		neighbors = graph[cn] #is a dic, new costs
		for nei in neighbors.keys():
			parent = cn
			if costs[nei] > (costs[parent] + graph[parent][nei]):
				costs[nei] = costs[parent] + graph[parent][nei]
				parents[nei] = parent 
		visited.append(cn)
	final_path = [last]
	while last in parents.keys():
		final_path.append(parents[last])
		last = parents[last]
	return final_path[::-1]


def main():
	#First step
	graph = {
	'book':{'poster':0, 'lp':5},
	'poster': {'guitar':30, 'drum':35},
	'lp': {'guitar':15, 'drum':20},
	'guitar': {'piano':20},
	'drum':{'piano':10},
	'piano' : {}
	}

	costs = {
	'poster': 0,
	'lp': 5,
	'guitar': float('inf'),
	'drum': float('inf'),
	'piano': float('inf')
	}

	parents = {
	'poster': 'book',
	'lp': 'book',
	'guitar': '',
	'drum': '',
	'piano': ''
	}

	print(dijkstra(graph, costs, parents, 'piano'))


if __name__=='__main__':
	main()