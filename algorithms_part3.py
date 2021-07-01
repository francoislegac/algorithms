

def main():
	states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
	stations = {}
	stations['kone'] = set(['id', 'nv', 'ut'])
	stations['ktwo'] = set(['wa', 'id', 'mt'])
	stations['kthree'] = set(['or', 'nv', 'ca'])
	stations['kfour'] = set(['nv', 'ut'])
	stations['kfive'] = set(['ca', 'az'])

	final_stations = set()

	while states_needed: #use of states_needed 
		best_station = None #starts with a None !
		states_covered = set()
		for station, states_for_station in stations.items():
			covered = states_needed & states_for_station
			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered
		states_needed -= states_covered	
		final_stations.add(best_station)
	
	print(final_stations)


if __name__=='__main__':
	main()
