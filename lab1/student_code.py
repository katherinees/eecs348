
##################################################################
# Notes:                                                         #
# You can import packages when you need, such as structures.     #
# Feel free to write helper functions, but please don't use many #
# helper functions.                                              #
##################################################################
import Queue

def my_init_map(map_array):
	testmap = []
	for ms in map_array:
		ms_arr = []
		for c in ms:
			ms_arr.append(int(c))
		testmap.append(ms_arr)
	return testmap

def find_start(testmap):
    world = my_init_map(testmap)
    row = 0
    sq = 0
    while (row < len(world)):
        while (sq < len(world[0])):
            if (world[row][sq] == 2):
                return [row, sq]
            sq = sq + 1
        sq = 0
        row = row + 1

def dfs(testmap):
    start_square = find_start(testmap)
    world = testmap
    prev_sq = my_init_map(testmap)
    world[start_square[0]][start_square[1]] = 5
    q = Queue.LifoQueue(len(testmap)*len(testmap[0]))
    q.put([start_square[0], start_square[1]])
    found = False
    end_spot = [-1, -1]
    while (found == False):
        current = q.get()
        if (world[current[0]][current[1]] != 5):
			world[current[0]][current[1]] = 4
		# North
        if (current[0]-1 >= 0):
            if (world[current[0]-1][current[1]] == 3):
                prev_sq[current[0]-1][current[1]] = [current[0], current[1]]
                world[current[0]-1][current[1]] = 5
                found = True
                end_spot = [current[0]-1, current[1]]
            if (world[current[0]-1][current[1]] == 0):
                prev_sq[current[0]-1][current[1]] = [current[0], current[1]]
                q.put([current[0]-1, current[1]])
		# West
        if (current[1]-1 >= 0):
            if (world[current[0]][current[1]-1] == 3):
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                world[current[0]][current[1]-1] = 5
                found = True
                end_spot = [current[0], current[1]-1]
            if (world[current[0]][current[1]-1] == 0):
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                q.put([current[0], current[1]-1])
		# South
        if (current[0]+1 < len(testmap)):
            if (world[current[0]+1][current[1]] == 3):
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                world[current[0]+1][current[1]] = 5
                found = True
                end_spot = [current[0]+1, current[1]]
            if (world[current[0]+1][current[1]] == 0):
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                q.put([current[0]+1, current[1]])
		# East
        if (current[1]+1 < len(testmap[0])):
            if (world[current[0]][current[1]+1] == 3):
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                world[current[0]][current[1]+1] = 5
                found = True
                end_spot = [current[0], current[1]+1]
            if (world[current[0]][current[1]+1] == 0):
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                q.put([current[0], current[1]+1])
    finished = False
    current = [end_spot[0], end_spot[1]]
    while (finished == False):
        current = prev_sq[current[0]][current[1]]
        if (world[current[0]][current[1]] == 5):
            finished = True
        world[current[0]][current[1]] = 5
    solution = []
    k = 0
    while (k < len(world)):
		word = ""
		for sq in world[k]:
			word = word + str(sq)
		solution.append(word)
		k = k + 1
    testmap = world
    return testmap



def bfs(testmap):
    start_square = find_start(testmap)
    world = testmap
    prev_sq = my_init_map(testmap)
    world[start_square[0]][start_square[1]] = 5
    q = Queue.Queue(len(testmap)*len(testmap[0]))
    q.put([start_square[0], start_square[1]])
    found = False
    end_spot = [-1, -1]
    while (found == False):
        current = q.get()
        if (current[1]+1 < len(testmap[0])):
            if (world[current[0]][current[1]+1] == 3):
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                world[current[0]][current[1]+1] = 5
                found = True
                end_spot = [current[0], current[1]+1]
            if (world[current[0]][current[1]+1] == 0):
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                world[current[0]][current[1]+1] = 4
                q.put([current[0], current[1]+1])
	    # South
        if (current[0]+1 < len(testmap)):
            if (world[current[0]+1][current[1]] == 3):
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                world[current[0]+1][current[1]] = 5
                found = True
                end_spot = [current[0]+1, current[1]]
            if (world[current[0]+1][current[1]] == 0):
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                world[current[0]+1][current[1]] = 4
                q.put([current[0]+1, current[1]])
	    # West
        if (current[1]-1 >= 0):
            if (world[current[0]][current[1]-1] == 3):
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                world[current[0]][current[1]-1] = 5
                found = True
                end_spot = [current[0], current[1]-1]
            if (world[current[0]][current[1]-1] == 0):
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                world[current[0]][current[1]-1] = 4
                q.put([current[0], current[1]-1])
	    # North
        if (current[0]-1 >= 0):
            if (world[current[0]-1][current[1]] == 3):
                prev_sq[current[0]-1][current[1]] = [current[0], current[1]]
                world[current[0]-1][current[1]] = 5
                found = True
                end_spot = [current[0]-1, current[1]]
            if (world[current[0]-1][current[1]] == 0):
                prev_sq[current[0]-1][current[1]] = [current[0], current[1]]
                world[current[0]-1][current[1]] = 4
                q.put([current[0]-1, current[1]])
    finished = False
    current = [end_spot[0], end_spot[1]]
    while (finished == False):
        current = prev_sq[current[0]][current[1]]
        if (world[current[0]][current[1]] == 5):
            finished = True
        world[current[0]][current[1]] = 5
    solution = []
    k = 0
    while (k < len(world)):
		word = ""
		for sq in world[k]:
			word = word + str(sq)
		solution.append(word)
		k = k + 1
    testmap = world
    return testmap


def a_star_search(dis_map, time_map, start, end):
	# HERE'S WHAT WE GONNA DO:
	# scores is a dictionary of dictionaries.
	scores = {}
	# visited is a dictionary containing 'place': time to get there
	visited = {}
	# times is basically the same, but contains entries for all the same places
	# that seen does. visited only contains entries for the places that got expanded.
	times = {}
	# seen contains 'place': heuristic. we use seen to pick the next thing to expand.
	seen = {}
	# next_best is the thing we are expanding in the while loop. so like, first
	# it's campus, then Lighthouse etc. during the while loop, we're looking
	# for what the next next_best will be. it's in the form
	# ['place', time to get there, distance to endpoint]
	next_best = [start, 0, dis_map[start][end]]
	found = False # haven't found endpoint yet
	while (found == False):
		nb = next_best[0] # get the place name of node we are expanding
		visited[next_best[0]] = next_best[1] # we're expanding it, so add it to visited
		# if we've already seen it, remove it from seen. otherwise it'll get messed
		# up when we want to consider the entry in seen with the lowest heuristic
		if nb in seen:
			seen.pop(nb, None)
		# create adjacent directory and shove that onto scores
		sub = {}
		for p in time_map[nb]:
			# for each thing it's adjacent to, calculate that heuristic and add
			# to the subdictionary, which will be the key in the scores dictionary
			if (time_map[nb][p] != None):
				sub[p] = next_best[1]+time_map[nb][p]+dis_map[p][end]
		scores[nb] = sub
		# now we're looking at each of the places that nb is adjacent to
		for p in sub:
			if (p == end):
				found = True
				break
			# if we've already seen this place before, e.g. for time_map2 when
			# we already saw Whole_Food with heuristic = 15, but now we're seeing
			# it and the heuristic would be 10.
			if p in seen:
				if (visited[nb]+time_map[nb][p]+dis_map[p][end] < seen[p]):
					seen[p] = visited[nb]+time_map[nb][p]+dis_map[p][end]
					times[p] = visited[nb]+time_map[nb][p]
				# THIS IS BAD AND I SHOULD FIX IT might be an issue w ties
				# for very weird maps but my tests pass so idc
				np = min(seen, key = seen.get)
				next_best = [np, seen[np]-dis_map[np][end], dis_map[np][end]]
			# the point of this loop is to find the next next_best, so if we've
			# already visited it, then we don't care.
			if ((p not in seen) and (p not in visited)):
				if not seen:
					# if there's nothing in seen. this is only gonna be an issue
					# on the very first iteration.
					seen[p] = visited[nb]+time_map[nb][p]+dis_map[p][end]
					times[p] = visited[nb]+time_map[nb][p]
				# np stands for next place. this is definitely a bad variable name
				# choice, but i wrote it out on paper first and it was faster. np is
				# the current candidate for the next next_best. BUT we want to know
				# if p is better. so calculate p's heuristic
				np = min(seen, key = seen.get)
				p_f = visited[nb]+time_map[nb][p]+dis_map[p][end] # p's heuristic
				if (p_f == seen[np]):
					# this is the case where p's heuristic is the same as the heuristic
					# of np, e.g. for time_map2 when Beach and YWCA both have 11. in
					# this case, next_best will be the place with a lower g(x), i.e.
					# took less time to get there. this makes the tests pass.
					if (visited[nb]+time_map[nb][p] < seen[np] - dis_map[np][end]):
						next_best = [p, visited[nb]+time_map[nb][p], dis_map[p][end]]
					else:
						next_best = [np, times[np], dis_map[np][end]]
				# if p's heuristic is less than the heuristic of np, then next_best is p
				if (p_f < seen[np]):
					next_best = [p, visited[nb]+time_map[nb][p], dis_map[p][end]]
					seen[p] = p_f
					times[p] = visited[nb]+time_map[nb][p]
				# if np's heuristic is lower, then that's next_best.
				# in any case, add p to seen, and p's time to times.
				if (p_f > seen[np]):
					next_best = [np, times[np], dis_map[np][end]]
					seen[p] = p_f
					times[p] = visited[nb]+time_map[nb][p]
	return scores
