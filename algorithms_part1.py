import numpy as np
import matplotlib.pyplot as plt 

#https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/methodes-de-tri
#la complexité en temps est de Θ(n2), avec n la taille du tableau.
#Le pire cas (n itérations) est atteint lorsque le plus petit élément est à la fin du tableau. La complexité est alors Θ(n2).
def tri_a_bulle(l):
	print(l)
	n = len(l)
	for i in range(n - 1):
		for j in range(n -1 - i ):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
	print(f'ordered list {l}')

def count_step_bin_s(n):
	count = 0
	while n !=1:
		n = n //2
		print(n)
		count += 1
	print('count', count)

def bin_s(mylist, item):
	#the idea is to return the index of the item from the list
	low = 0
	high = len(mylist) - 1

	#problem with this: doesn't work with the None case !
	while low != high:
		#print(f'low {low}, high {high}')
		mid = (low + high) //2 #rounded down
		guess = mylist[mid]
		if guess == item:
			return mid 
		if guess < item:
			low = mid
		if guess > item:
			high = mid
	return None
	'''
	#my first answer
	while item != mylist[high//2]:
		if item > mylist[high//2]:
			low = high//2
		else:
			high = high//2
		print(low, high)
	'''

def off_bin_s(mylist, item):
	#the idea is to return the index of the item from the list
	low = 0
	high = len(mylist) - 1

	while low <= high:
		#print(f'low {low}, high {high}')
		mid = (low + high) //2 #rounded down
		guess = mylist[mid]
		if guess == item:
			return mid 
		if guess < item:
			low = mid + 1
		if guess > item:
			high = mid -1
	return None


##SELECTION SORT
def findSmallest(arr):
	smallest = arr[0]
	smallestIdx = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallestIdx = i
	return smallestIdx

def selectionSort(arr):
	resArr = []
	for i in range(len(arr)):
		smallestIdx = findSmallest(arr)
		resArr.append(arr.pop(smallestIdx))
	return resArr


##RECURSION

def factorial(n):
	res = 1
	if n == 0: return res
	while n != 1:
		res *= n
		n -= 1
	return res

def factorialbis(n):
	for i in range(1, n):
		n *= i
	return n


def factorialrec(n):
	if n == 1:
		return 1
	else:
		return n*factorialrec(n-1)

def countdown(i):
	print(i)
	if i <= 0:
		return
	else:
		countdown(i-1)

#Divide and conquer
#You’re given an array of numbers.
#You have to add up all the numbers and return the total without using a loop -> recursion
def rec_sum(arr):
	#base case
	n = len(arr)
	if n == 1:
		return arr[0]
	#recursive case
	first_value = arr.pop(0)
	return first_value + rec_sum(arr)

#Write a recursive function to count the number of items in a list
def rec_count(arr):
	#base case
	print('arr',arr)
	if len(arr) == 1:
		return 1
	arr.remove(arr[0])
	return 1 + rec_count(arr)

#cleaner solution
def rec_count(arr):
	if not arr:
		return 0
	return 1 + rec_count(arr[1:])

#Find the maximum number in a list.
def rec_max(arr):
	#base case
	if len(arr) == 1:
		return arr[0]
	#rec case
	if arr[0] > rec_max(arr[1:]):
		return arr[0]
	else:
		return rec_max(arr[1:])

#Binary Search -> recursive
''' MY BAD SOLUTION
def rec_bs(arr, target):
	#sorting first
	arr = selectionSort(arr)
	
	mid = len(arr)//2
	print('mid', mid, 'arr', arr)
	guess = arr[mid]
	print('mid', mid, 'guess', guess)

	if item == guess:
		return mid
	elif item > guess:
		return mid + rec_bs(arr[mid + 1:], item)
	else:
		return mid - rec_bs(arr[:mid], item)
'''

def binary_search(arr, target):
	arr = selectionSort(arr)
	if not arr:
	    return -1        
	if len(arr) == 1 and arr[0] == target:
	    return 0
	if len(arr) == 1 and arr[0] != target:
	    return -1
	low = 0         
	high = len(arr) - 1    
	mid = (low + high) // 2

	if arr[mid] > target:
	    return binary_search(arr[:mid], target)
	else:
	    return binary_search(arr[mid+1:], target)

def div_eucli(n, q):
	r = n
	p = 1
	while(r >= q):
		r = n - p*q
		p+=1
		print(r)
	return r

#breadth-first search
'''
from collections import deque
def bfs(name):
	search_queue = deque()
	searched = []
	search_queue += graph[name]
	while search_queue:
		person = search_queue.popleft()  
		if not in searched:
			if is_mango_seller(person):
				print(f'{person} is a seller')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False
'''


#Depth Fisrt search
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def main():
	#l = list(np.random.randint(0,10, 10))
	#tri_a_bulle(l)
	'''
	x = np.arange(0,50,1)
	fig, ax = plt.subplots()
	ax.plot(x, x*x, color= 'r')
	ax.plot(x, [np.math.factorial(v) for v in x], color = 'b')
	ax.plot(x, [factorial(v) for v in x], color = 'g')
	ax.legend(['ncarré', 'nfactor'])
	plt.show()	
	
	'''
	#for x in range(10):
	#	print(np.math.factorial(x), factorial(x), factorialbis(x))
	#countdown(5)


	'''
	l = list(np.random.randint(0,10,10))
	print(l)
	print(selectionSort(l))
	'''
	#l = [1,2,3,5,9]
	#print(binary_search(l, 9))

	#DFS
	# Using a Python dictionary to act as an adjacency list
	graph = {
	    'A' : ['B','C'],
	    'B' : ['D', 'E'],
	    'C' : ['F'],
	    'D' : [],
	    'E' : ['F'],
	    'F' : []
	}
	visited = set() # Set to keep track of visited nodes.
	# Driver Code
	dfs(visited, graph, 'A')

if __name__ == '__main__':
	main()


