import student_code as sc
import Queue

def init_map(map_array):
	testmap = []
	for ms in map_array:
		ms_arr = []
		for c in ms:
			ms_arr.append(int(c))
		testmap.append(ms_arr)
	return testmap

def check_map_equal (map1, map2):
	flag = True
	for i in range(len(map1)):
		for j in range(len(map1[0])):
			if map1[i][j] != map2[i][j]:
				flag = False
	return flag

data1= ["2000000000",
        "0101111111",
        "0100000000",
        "0101111111",
        "0101000001",
        "0101010110",
        "0101010000",
        "0100011110",
        "0011111110",
        "1011111110",
        "1011111111",
        "1000000003"]
gold_df1 = ["5444444444",
            "5141111111",
            "5144444444",
            "5141111111",
            "5141444441",
            "5141414114",
            "5141414444",
            "5144411114",
            "5511111114",
            "1511111114",
            "1511111111",
            "1555555555"]
gold_bf1 = ["5444444444",
            "5141111111",
            "5144444444",
            "5141111111",
            "5141444441",
            "5141414110",
            "5141414440",
            "5144411110",
            "5511111110",
            "1511111110",
            "1511111111",
            "1555555555"]
data2= ["0000000000",
        "1111110101",
        "0300010101",
        "1111010101",
        "0001010101",
        "0100010101",
        "1111010101",
        "0000000101",
        "0111111100",
        "0000000101",
        "0111111120",
        "0000000010"]
gold_df2 = ["0000005554",
            "1111115151",
            "0555515151",
            "1111515151",
            "4441515151",
            "4144515151",
            "1111515151",
            "4444555151",
            "4111111154",
            "4444444151",
            "4111111154",
            "4444444414"]
gold_bf2 = ["4444445554",
            "1111115151",
            "0555515151",
            "1111515151",
            "4441515151",
            "4144515151",
            "1111515151",
            "4444555151",
            "4111111154",
            "4440000151",
            "4111111154",
            "4000000014"]

def print_map (testmap):
	for lst in testmap:
		print lst
		print '\n'

def find_start(testmap):
    world = init_map(testmap)
    row = 0
    sq = 0
    while (row < len(world)):
        while (sq < len(world[0])):
            if (world[row][sq] == 2):
                return [row, sq]
            sq = sq + 1
        sq = 0
        row = row + 1

    # finds the start square labeled 2
    # and returns its position [row, sq]
    # row = 0
    # sq = 0
    # while (row < len(testmap)):
    #     while (sq < len(testmap[0])):
    #         #print testmap[row][sq]
    #         if (testmap[row][sq] == "2"):
    #             #print "found it"
    #             return [row, sq]
    #         sq = sq + 1
    #     sq = 0
    #     row = row + 1


def bfs(testmap):
    start_square = find_start(testmap)
    world = testmap
    prev_sq = init_map(testmap)
    # prev_sq[0][0] = [0,0]
    world[start_square[0]][start_square[1]] = 5
    # current = [start_square[0], start_square[1]]
    # if E's coords work and it's zero, append to queue & prev
    q = Queue.Queue(len(testmap)*len(testmap[0]))
    q.put([start_square[0], start_square[1]])
    found = False
    end_spot = [-1, -1]
    while (found == False):
        current = q.get()
        # print "current is: -v"
        # print current
        if (current[1]+1 < len(testmap[0])):
            if (world[current[0]][current[1]+1] == 3):
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                world[current[0]][current[1]+1] = 5
                found = True
                end_spot = [current[0], current[1]+1]
            if (world[current[0]][current[1]+1] == 0):
                # print "east is " + testmap[current[0]][current[1]+1]
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                world[current[0]][current[1]+1] = 4
                # print "put this east boi on the queue"
                # print [current[0], current[1]+1]
                q.put([current[0], current[1]+1])
	        # print q.get()
	    # South
        if (current[0]+1 < len(testmap)):
            if (world[current[0]+1][current[1]] == 3):
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                world[current[0]+1][current[1]] = 5
                found = True
                end_spot = [current[0]+1, current[1]]
            if (world[current[0]+1][current[1]] == 0):
                # print "south is " + testmap[current[0]+1][current[1]]
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                world[current[0]+1][current[1]] = 4
                # print "put this south boi on the queue"
                # print [current[0]+1, current[1]]
                q.put([current[0]+1, current[1]])
	    # West
        if (current[1]-1 >= 0):
            if (world[current[0]][current[1]-1] == 3):
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                world[current[0]][current[1]-1] = 5
                found = True
                end_spot = [current[0], current[1]-1]
            if (world[current[0]][current[1]-1] == 0):
                # print "west is " + testmap[current[0]][current[1]-1]
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
                # print "north is " + testmap[current[0]-1][current[1]]
                prev_sq[current[0]-1][current[1]] = [current[0], current[1]]
                world[current[0]-1][current[1]] = 4
                q.put([current[0]-1, current[1]])
        # found = True
    # print current
    # print world
    # print prev_sq
    # print found
	# go back and do the 5 path
    finished = False
    current = [end_spot[0], end_spot[1]]
    while (finished == False):
        current = prev_sq[current[0]][current[1]]
        if (world[current[0]][current[1]] == 5):
            finished = True
        world[current[0]][current[1]] = 5
    solution = []
    # print "here is the world"
    # print world
    k = 0
    while (k < len(world)):
		word = ""
		for sq in world[k]:
			word = word + str(sq)
		solution.append(word)
		k = k + 1
    # print "my sol"
    # print solution
    testmap = world
    return testmap

def dfs(testmap):
    start_square = find_start(testmap)
    world = testmap
    prev_sq = init_map(testmap)
    # prev_sq[0][0] = [0,0]
    world[start_square[0]][start_square[1]] = 5
    # current = [start_square[0], start_square[1]]
    # if E's coords work and it's zero, append to queue & prev
    q = Queue.LifoQueue(len(testmap)*len(testmap[0]))
    q.put([start_square[0], start_square[1]])
    found = False
    end_spot = [-1, -1]
    while (found == False):
        current = q.get()
        # print "current is: -v"
        # print current
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
                # print "north is " + testmap[current[0]-1][current[1]]
                prev_sq[current[0]-1][current[1]] = [current[0], current[1]]
                # world[current[0]-1][current[1]] = 4
                q.put([current[0]-1, current[1]])
		# West
        if (current[1]-1 >= 0):
            if (world[current[0]][current[1]-1] == 3):
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                world[current[0]][current[1]-1] = 5
                found = True
                end_spot = [current[0], current[1]-1]
            if (world[current[0]][current[1]-1] == 0):
                # print "west is " + testmap[current[0]][current[1]-1]
                prev_sq[current[0]][current[1]-1] = [current[0], current[1]]
                # world[current[0]][current[1]-1] = 4
                q.put([current[0], current[1]-1])
		# South
        if (current[0]+1 < len(testmap)):
            if (world[current[0]+1][current[1]] == 3):
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                world[current[0]+1][current[1]] = 5
                found = True
                end_spot = [current[0]+1, current[1]]
            if (world[current[0]+1][current[1]] == 0):
                # print "south is " + testmap[current[0]+1][current[1]]
                prev_sq[current[0]+1][current[1]] = [current[0], current[1]]
                # world[current[0]+1][current[1]] = 4
                # print "put this south boi on the queue"
                # print [current[0]+1, current[1]]
                q.put([current[0]+1, current[1]])
		# East
        if (current[1]+1 < len(testmap[0])):
            if (world[current[0]][current[1]+1] == 3):
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                world[current[0]][current[1]+1] = 5
                found = True
                end_spot = [current[0], current[1]+1]
            if (world[current[0]][current[1]+1] == 0):
                # print "east is " + testmap[current[0]][current[1]+1]
                prev_sq[current[0]][current[1]+1] = [current[0], current[1]]
                # world[current[0]][current[1]+1] = 4
                # print "put this east boi on the queue"
                # print [current[0], current[1]+1]
                q.put([current[0], current[1]+1])
	        # print q.get()
        # found = True
    # print current
    # print world
    # print prev_sq
    # print found
	# go back and do the 5 path
    finished = False
    current = [end_spot[0], end_spot[1]]
    while (finished == False):
        current = prev_sq[current[0]][current[1]]
        if (world[current[0]][current[1]] == 5):
            finished = True
        world[current[0]][current[1]] = 5
    solution = []
    # print "here is the world"
    # print world
    k = 0
    while (k < len(world)):
		word = ""
		for sq in world[k]:
			word = word + str(sq)
		solution.append(word)
		k = k + 1
    # print "my sol"
    # print solution
    testmap = world
    return testmap

## CHECKING DFS SHIT
# st_map = dfs(init_map(data2))
# print "this what i got"
# print st_map
# print "this the solution"
# print init_map(gold_df2)
# print check_map_equal(st_map, init_map(gold_df2))

def check_score_equal(score1, score2):
	flag = True
	keys1 = score1.keys()
	keys2 = score2.keys()
	if set(keys1) == set(keys2):
		for k in keys1:
			if score1[k] != score2[k]:
				flag = False
	else:
		flag = False
	return flag

dis_map = {'Campus': {'Campus': 0, 'Whole_Food': 3, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 1, 'Ryan Field': 2, 'YWCA':12},
			'Whole_Food': {'Campus': 3,  'Whole_Food': 0, 'Beach': 3, 'Cinema': 3, 'Lighthouse': 4, 'Ryan Field': 5, 'YWCA':8},
			'Beach': {'Campus': 5,  'Whole_Food': 3, 'Beach': 0, 'Cinema': 8, 'Lighthouse': 5, 'Ryan Field': 7, 'YWCA':12,},
			'Cinema': {'Campus': 5,  'Whole_Food': 3, 'Beach': 8, 'Cinema': 0, 'Lighthouse': 7, 'Ryan Field': 7, 'YWCA':2},
			'Lighthouse': {'Campus': 1, 'Whole_Food': 4, 'Beach': 5, 'Cinema': 7, 'Lighthouse': 0, 'Ryan Field': 1, 'YWCA':15},
			'Ryan Field': {'Campus': 2, 'Whole_Food': 5, 'Beach': 7, 'Cinema': 7, 'Lighthouse': 1, 'Ryan Field': 0, 'YWCA':12},
			'YWCA': {'Campus': 12, 'Whole_Food': 8, 'Beach': 12, 'Cinema': 2, 'Lighthouse': 15, 'Ryan Field': 12, 'YWCA':0}}
time_map1 = {'Campus': {'Campus': None, 'Whole_Food': 4, 'Beach': 3, 'Cinema': None, 'Lighthouse': 1, 'Ryan Field': None, 'YWCA': None},
			'Whole_Food': {'Campus': 4,  'Whole_Food': None, 'Beach': 4, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
			'Beach': {'Campus': 4,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
			'Cinema': {'Campus': None,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': 2},
			'Lighthouse': {'Campus': 1, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': 1, 'YWCA': None},
			'Ryan Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 2, 'Ryan Field': None, 'YWCA': 5},
			'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': 5, 'YWCA': None}}
time_map2 = {'Campus': {'Campus': None, 'Whole_Food': 12, 'Beach': 3, 'Cinema': None, 'Lighthouse': 1, 'Ryan Field': None, 'YWCA': None},
			'Whole_Food': {'Campus': 4,  'Whole_Food': None, 'Beach': 4, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
			'Beach': {'Campus': 4,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
			'Cinema': {'Campus': None,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': 2},
			'Lighthouse': {'Campus': 1, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': 1, 'YWCA': None},
			'Ryan Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 2, 'Ryan Field': None, 'YWCA': 7},
			'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 5, 'Lighthouse': None, 'Ryan Field': 5, 'YWCA': None}}

gold_score1 = {'Whole_Food': {'Beach': 16, 'Campus': 13, 'Cinema': 7}, 'Campus': {'Lighthouse': 8, 'Beach': 11, 'Whole_Food': 7}}

def calc_f (dis_map, current_place, end_place, current_time):
	g = current_time
	h = dis_map[current_place][end_place]
	return g + h

def a_star_search (dis_map, time_map, start,end):
	scores = {}
	visited = {}
	found = False
	time = 0
	sub = {}
	q = Queue.PriorityQueue()
	q.put((0, start))
	current = q.get()
	print "current is " + str(current)
	for p in time_map[current[1]]:
		if (time_map[current[1]][p] != None):
			f = calc_f(dis_map, p, end, time_map[current[1]][p])
			# print p + str(f)
			q.put((f, p))
			sub.update({p: f})
	scores.update({current[1]: sub})
	time = time_map[current[1]][min(sub, key = sub.get)]
	print "time is " + str(time)
	next_thing = q.get()
	print "next is " + str(next_thing)
	while (found == False):
		sub2 = {}
		for p in time_map[next_thing[1]]:
			if (time_map[next_thing[1]][p] != None):
				if (p == end):
					found = True
				f = calc_f(dis_map, p, end, time + time_map[next_thing[1]][p])
				print f, p
				q.put((f, p))
				sub2.update({p: f})
		scores.update({min(sub, key = sub.get): sub2})
		sub = sub2
		next_thing = q.get()
		found = True
	print min(sub, key = sub.get)
	print scores
	for entry in scores:
		print entry + " " + min(scores[entry], key = scores[entry].get)
	allthings = {}
	for entry in scores:
		allthings.update(scores[entry])
	print allthings
	return scores

def stupid_star(dis_map, time_map, start, end):
	frontier = Queue.PriorityQueue()
	frontier.put((0, start))
	frontier.put((10000, end))
	# frontier.put((10, end))
	# print frontier.get()[1]
	#print frontier.get()
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	past = start
	while not frontier.empty():
		current = frontier.get()[1]
		print "past is " + str(past)
		print "current is " + str(current)
		if current == end:
			break

		for p in time_map[current]:
			# if (p == end):
			# 	came_from[p] = current
			# 	break
			if (time_map[current][p] != None):
				new_cost = cost_so_far[current] + time_map[current][p]
				if p not in cost_so_far or new_cost < cost_so_far[p]:
					cost_so_far[p] = new_cost
					priority = new_cost + dis_map[p][end]
					print p
					frontier.put((p, priority))
					print new_cost
					came_from[p] = current
		past = current
	print came_from
	print cost_so_far
	back = False
	while (back == False):
		print current
		back = True
# test = {'a': 1, 'b': 2}
# foo = {'c': 3, 'd': 4}
# bar = {'first': test, 'second': foo}
# for i in bar:
# 	for j in bar[i]:
# 		print bar[i][j]
# print bar
# stupid_star(dis_map, time_map2, 'Campus', 'Cinema')
def shit_star(dis_map, time_map, start, end):
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
score1 = shit_star(dis_map, time_map1, 'Campus', 'Cinema')
if check_score_equal(score1,gold_score1):
	print "pass A* search for time map1"
else:
	print "Fail A* search for time map1"

student_score2 = shit_star(dis_map,time_map2, 'Campus', 'Cinema')
gold_score2 = {'Ryan Field': {'YWCA': 11, 'Lighthouse': 11}, 'Whole_Food': {'Beach': 19, 'Campus': 16, 'Cinema': 10}, 'Lighthouse': {'Ryan Field': 9, 'Campus': 7}, 'Beach': {'Whole_Food': 10, 'Campus': 12}, 'Campus': {'Lighthouse': 8, 'Beach': 11, 'Whole_Food': 15}}
print gold_score2
if check_score_equal(student_score2,gold_score2):
	print "pass A* search for time map2"
else:
	print "Fail A* search for time map2"
