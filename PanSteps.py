#Euler Project 178 - Timothy Heath
BASE = 10
LENGTH = 40
#Find the number of base BASE pandigital numbers with at most LENGTH digits
import copy

def extend(old_paths):
	#find number of different path types one longer than old_paths
	new_paths = copy.deepcopy(old_paths)
	#mid_paths turn to bot_paths and top_paths turn to pan_paths at digit 0
	new_paths[0]["mid_paths"] = 0
	new_paths[0]["bot_paths"] = old_paths[1]["mid_paths"] + old_paths[1]["bot_paths"]
	new_paths[0]["top_paths"] = 0
	new_paths[0]["pan_paths"] = old_paths[1]["top_paths"] + old_paths[1]["pan_paths"]
	#paths are extended from those ending one digit higher or lower
	for digit in range(1, BASE - 1):
		for path_type in new_paths[digit].keys():
			new_paths[digit][path_type] = old_paths[digit - 1][path_type] + old_paths[digit + 1][path_type]
	#mid_paths turn to top_paths and bot_paths turn to pan_paths at top digit
	new_paths[BASE - 1]["mid_paths"] = 0
	new_paths[BASE - 1]["bot_paths"] = 0
	new_paths[BASE - 1]["top_paths"] = old_paths[BASE - 2]["mid_paths"] + old_paths[BASE - 2]["top_paths"]
	new_paths[BASE - 1]["pan_paths"] = old_paths[BASE - 2]["bot_paths"] + old_paths[BASE - 2]["pan_paths"]
	return new_paths

#intilize with 1 length paths starting at each digit
paths = [
	{
		#no path starts with 0
		"mid_paths": 0, 
		"bot_paths": 0,
		"top_paths": 0,
		"pan_paths": 0
	}]
for digit in range(1, BASE-1):
	paths.append(
	{		
		#number of paths ending at digit		
		"mid_paths": 1, #paths that have not hit 0 or top digit
		"bot_paths": 0, #paths that have hit 0 but not top digit
		"top_paths": 0, #paths that have hit top digit but not 0
		"pan_paths": 0  #pandigital paths
	})
paths.append(
	{
		"mid_paths": 0,
		"bot_paths": 0,
		"top_paths": 1,
		"pan_paths": 0	
	})

pan_steps = 0 #total number of pandigital paths
for place in range(1, LENGTH):
	paths = extend(paths) #extend paths by 1
	for digit in range(BASE):
		#add all pandigital paths of this length
		pan_steps += paths[digit]["pan_paths"]
print pan_steps
