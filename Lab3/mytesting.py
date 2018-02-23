import read, copy
from logical_classes import *
from student_code import KnowledgeBase
from util import *

def main():
    # Assert starter facts
    file = 'statements_kb2.txt'
    data = read.read_tokenize(file)
    KB = KnowledgeBase([], [])
    for dtype, item in data:
        if dtype == read.FACT:
            KB.kb_assert(item)

    # KB demonstration
    # Ask for one of the starter facts
    # print "Starting basic KB demonstration"
    _, ask1 = read.parse_input("fact: (hero ?x)")
    # print " Asking if", ask1
    # answer = KB.kb_ask(ask1)
    # # print answer
    # pprint_justification(answer)
    # print ("Basic demonstration of KB complete" if answer else "ERROR: KB demonstration failed") + "\n"

    print "Starting Test 1"
    _, test1 = read.parse_input("fact: (hero Ai)")
    # print " Retracting", test1
    KB.kb_retract(test1)
    # print KB.facts
    answer = KB.kb_ask(ask1)
    # print answer
    # pprint_justification(answer)
    print (("Fail" if answer else "Pass") + " Test 1\n")
    hai = Fact(test1).statement
    print "Starting Test 2"
    fail = True
    for dtype, item in data:
        if dtype == read.RULE:
            # print "the item is", item
            KB.kb_assert(item)
            # if not factq(item):
            #     print "SCREAM", Rule(item)
            #     print "LHS first term is", Rule(item).lhs[0]
            #     first_term = Rule(item).lhs[0]
            #     bound = match(hai, first_term)
            #     if bound:
            #         print "bindings are", bound
            #         insta = instantiate(Rule(item).lhs[0], bound)
            #         print "INSTA", insta
            #         insta2 = instantiate(Rule(item).rhs, bound)
            #         print "INSTA2", insta2
            #         new_lhs = copy.deepcopy(Rule(item).lhs)
            #         new_lhs.remove(first_term)
            #         print "new lhs", new_lhs
            #         supby = [[Rule(item), hai]]
            #         newfact = Fact(insta2, supby)
            #         print "newfact sup by is", newfact.supported_by
            #         print newfact.statement
            #         # print "now it's", Rule(item)
            #         newrulelist = [[insta.predicate], [insta2.predicate, insta2.terms]]
            #         print "list is", newrulelist
            #         # newrule = Rule(newrulelist)
            #     # else:
            #     #     print "DIDN'T MATCH"
    _, test2_1 = read.parse_input("fact: (strong ?x)")
    print " Asking", test2_1
    answer = KB.kb_ask(test2_1)
    #pprint_justification(answer)
    if answer and len(answer)==1 and answer[0]['?x'] == 'Ai':
        print " Pass Part 1"
        _, test2_2 = read.parse_input("fact: (inst Sarorah ?x)")
        print " Asking", test2_2
        answer = KB.kb_ask(test2_2)
        #pprint_justification(answer)
        if answer and len(answer)==2 and (answer[0]['?x'] == 'Sorceress' or answer[0]['?x'] == 'Wizard'):
            print " Pass Part 2"
            _, test2_3 = read.parse_input("fact: (dead ?dragon)")
            print " Asking", test2_3
            answer = KB.kb_ask(test2_3)
            #pprint_justification(answer)
            if not answer:
                print " Pass Part 3"
                _, assert_hero = read.parse_input("fact: (hero Ai)")
                print " Asserting", assert_hero
                KB.kb_assert(assert_hero)
                _, test2_4 = read.parse_input("fact: (dead ?dragon)")
                print " Asking", test2_4
                answer = KB.kb_ask(test2_4)
                # pprint_justification(answer)
                if answer and len(answer)==1 and answer[0]['?dragon'] == 'Nosliw':
                    print " Pass Part 4\nPass Test 2\n"
                    fail = False
    if fail:
        print "Fail Test 2\n"

    # DEBUGGING FOR TEST 2
    # answer = KB.kb_ask(test2_4)
    for f in KB.facts:
        print f.statement, "\n"
    # f = KB.facts[0]
    # print "the fact", f.statement
    # for s in f.supported_by[0]:
    #     print s
    # print "consider the fact", f.statement
    # print f.asserted
    # for sf in f.supported_by:
    #     print sf, "\n"

    print "Starting Test 3"
    fail = True
    _, possesses = read.parse_input("fact: (possesses Ai Loot)")
    print " Retracting", possesses
    KB.kb_retract(possesses)
    _, test3_1 = read.parse_input("fact: (dead ?dragon)")
    print " Asking", test3_1
    answer = KB.kb_ask(test3_1)
    #pprint_justification(answer)
    if not answer:
        print " Pass Part 1"
        print " Asserting", possesses
        KB.kb_assert(possesses)
        _, sleeping = read.parse_input("fact: (sleeping Nosliw)")
        _, safe = read.parse_input("rule: (sleeping Nosliw) -> (safe HappyDale)")
        print " Asserting", sleeping
        KB.kb_assert(sleeping)
        print " Asserting", safe
        KB.kb_assert(safe)
        print " Retracting", possesses
        KB.kb_retract(possesses)
        _, possesses = read.parse_input("fact: (possesses Ai Loot)")
        _, test3_2 = read.parse_input("fact: (safe ?town)")
        print " Asking", test3_2
        answer = KB.kb_ask(test3_2)
        #pprint_justification(answer)
        if answer and len(answer)==1 and answer[0]['?town'] == 'HappyDale':
            print " Pass Part 2\nPass Test 3\n"
            fail = False
    if fail:
        print "Fail Test 3\n"


def pprint_justification(answer):
    """Pretty prints (hence pprint) justifications for the answer.
    """
    if not answer: print 'Answer is False, no justification'
    else:
        print '\nJustification:'
        for i in range(0,len(answer.list_of_bindings)):
            # print bindings
            print answer.list_of_bindings[i][0]
            # print justifications
            for fact_rule in answer.list_of_bindings[i][1]:
                pprint_support(fact_rule,0)
        print

def pprint_support(fact_rule, indent):
    """Recursive pretty printer helper to nicely indent
    """
    if fact_rule:
        print " "*indent, "Support for",

        if isinstance(fact_rule, Fact):
            print fact_rule.statement
        else:
            print fact_rule.lhs, "->", fact_rule.rhs

        if fact_rule.supported_by:
            for pair in fact_rule.supported_by:
                print " "*(indent+1), "support option"
                for next in pair:
                    pprint_support(next, indent+2)



if __name__ == '__main__':
    main()
