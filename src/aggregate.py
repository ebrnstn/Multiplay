import sys
import json

def parse_json(json_file):
	inputs = json.loads(json_file)

	frequency = {}
	filtered_frequencies = {}
	valid_commands = ["up", "down", "right", "left"]

	for entity in inputs:
		if entity['message'] not in frequency:
			frequency[entity['message']] = 0
		frequency[entity['message']] += 1


	for element in frequency:
		if element in valid_commands:
			if element not in filtered_frequencies:
				filtered_frequencies[element] = 0
			filtered_frequencies[element] += 1

	return filtered_frequencies

def pick_aggregated_move(json_file):

	frequencies = parse_json(json_file)
	best_move = ''

	best_frequency = 0

	for element in frequencies:
		if frequencies[element] > best_frequency:
			best_frequency = frequencies[element]
			best_move = element

	return best_move

def pick_sequential_move(json_file):
	inputs = json.loads(json_file)

	for entity in inputs:
		return entity['message']

if __name__ == '__main__':
	
	json_file = sys.argv[1]

	move_type = sys.argv[2]

	json_file = open(json_file).read()

	#frequencies = parse_json(json_file)
	if move_type == '0':
		print pick_sequential_move(json_file)
	else:
		print pick_aggregated_move(json_file)