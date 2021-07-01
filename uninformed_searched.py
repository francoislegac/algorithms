from collections import deque
import maze_puzzle as mp 

#BFS
def run_bfs(maze_puzzle, current_point, visited_points):
	queue = deque()
	queue.append(current_point)
	while queue:
		current_point = queue.popleft()
		if not current_point in visited_points:
			visited_points.append(current_point)
			if isFinalPoint(maze_puzzle, current_point):
				print(f'This is the final point: {current_point.print()}')
				return current_point
			else:
				neighbors = maze_puzzle.get_neighbors(current_point)
				for n in neighbors:
					n.set_parent(current_point)
					queue.append(n)
	print('Couldn\'t find the way out')
	return False

#DFS
'''
def run_dfs(maze_puzzle, current_point, visited_points):
	queue = deque()
	queue.append(current_point)
	while queue:
		current_point.popleft(queue)
		if not current_point in visited_points:
			if isFinalPoint(maze_puzzle, current_point):
				print('We\'ve found the final point')
				return current_point
			else:
				neighbors = maze_puzzle.get_neighbors(current_point)
				if neighbors:
					count = 0
					for n in neighbors:
						if not n in visited_points:
							new_neighbor = n
							new_neighbor.set_parent(current_point)
							queue.append(new_neighbor)
							break
						else:
						count +=1 
					if count == len(neighbors):
						current_point = current_point.parent
				else:
					queue.append(current_point.parent)
					visited_points.append(current_point)
		else:
'''
def run_dfs(maze_game, current_point):
	visited_points = []
	stack = [current_point]
	while stack:
		next_point = stack.pop()
		if not is_in_visited_points(next_point, visited_points):
			visited_points.append(next_point)
			if isFinalPoint(maze_game, next_point):
				print('found it!')
				return next_point
			else:
				neighbors = maze_game.get_neighbors(next_point)
				for neighbor in neighbors:
					neighbor.set_parent(next_point)
					stack.append(neighbor)
	return 'No path'

def is_in_visited_points(current_point, visited_points):
	for visited_point in visited_points:
		if current_point.x == visited_point.x and current_point.y == visited_point.y:
			return True
	return False

def isFinalPoint(maze_puzzle, current_point):
	return maze_puzzle.get_current_point_value(current_point) == '*'

def get_path(point):
	path = []
	current_point = point
	while current_point.parent:
		path.append([current_point.parent.x, current_point.parent.y])
		current_point = current_point.parent
	return path[::-1] 

def main():
	maze_game_main = mp.MazePuzzle()
	starting_point = mp.Point(2,2)
	print('The maze \n')
	maze_game_main.print_maze()

	res = run_bfs(maze_game_main, starting_point, [])
	print(get_path(res))

	print('-- DFS -- ')
	res = run_dfs(maze_game_main, starting_point)
	print(get_path(res))


if __name__=='__main__':
	main()