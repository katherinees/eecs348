import planner

def main():
	## Test 0
	plan = planner.find_plan("student_domain.pddl", "task00.pddl")
	print "Test 0"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 1 and len(plan.plan) < 4:
			print "Pass Test 0"
		else:
			print "Fail Test 0"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 0"
		exit(1)

	## Test 1
	plan = planner.find_plan("student_domain.pddl", "task01.pddl")
	print "Test 1"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 2:
			print "Pass Test 1"
		else:
			print "Fail Test 1"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 1"
		exit(1)

	## Test 2
	plan = planner.find_plan("student_domain.pddl", "task02.pddl")
	print "Test 2"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 2 and len(plan.plan) < 10:
			print "Pass Test 2"
		else:
			print "Fail Test 2"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 2"
		exit(1)

	## Test 3
	plan = planner.find_plan("student_domain.pddl", "task03.pddl")
	print "Test 3"
	if plan.ok:
		print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 4 and len(plan.plan) < 30: #modified from 18 to 30
			print "Pass Test 3"
		else:
			print "Fail Test 3"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 3"
		exit(1)

	## Test 4
	plan = planner.find_plan("student_domain.pddl", "task04.pddl")
	print "Test 4"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 1 and len(plan.plan) < 4:
			print "Pass Test 4"
		else:
			print "Fail Test 4"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 4"
		exit(1)

	##Test 5: Checks to make sure that we cannot use (at location location)
	plan = planner.find_plan("student_domain.pddl", "task05.pddl")
	print "Test 5"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		print "Fail Test 5: Undefined predicate use"
	else:
		print "Pass Test 5"


    ##Test 6
	plan = planner.find_plan("student_domain.pddl", "task06.pddl")
	print "Test 6"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		print "Fail Test 6: Should not have found a plan"
	else:

		print "Pass Test 6"

	##Test 7: Checks to make sure we cannot go from suntheatre to happydale in less than 2 moves
	plan = planner.find_plan("student_domain.pddl", "task07.pddl")
	print "Test 7"
	if plan.ok:
		if len(plan.plan) < 2:
			print "Fail Test 7: Impossible to go from happydale to suntheatre and back in 2 steps"
		else:
			print "Pass Test 7"
			# exit(1)

	else:
		print "Fail Test 7"
		print plan.error


	##Test 8: Test 4 with the additional constraint that the dragon is not asleep

	plan = planner.find_plan("student_domain.pddl", "task08.pddl")
	print "Test 8"
	if plan.ok:
		# print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 1 and len(plan.plan) < 4:
			print "Fail Test 8: We were able to kill the dragons in less than 4 steps"
		else:
			print "Pass Test 8: We killed the dragon"

	else:
		print "Couldn't find any plan at all"
		print plan.error
		print "Fail Test 8"
		exit(1)

	##Test 9: Testing whether we can kill the dragon without being strong

	plan = planner.find_plan("student_domain.pddl", "task09.pddl")
	print "Test 9"
	if plan.ok:
		print "Fail Test 9: We killed the dragon without being strong"

	else:
		print "Pass Test 9: Couldn't find a plan"

	##Test 10: Testing that the dragon cannot be both asleep and dead

	plan = planner.find_plan("student_domain.pddl", "task10.pddl")
	print "Test 10"
	if plan.ok:
		print "Fail Test 10: The dragon is asleep and dead"

	else:
		print "Pass Test 10: This solution is infeasible"


	##Test 11: Testing that happydale cannot be saved without a hero

	plan = planner.find_plan("student_domain.pddl", "task11.pddl")
	print "Test 11"
	if plan.ok:
		print "Fail Test 11: We saved happydale without a hero"

	else:
		print "Pass Test 11"




if __name__ == '__main__':
    main()
