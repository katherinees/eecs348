import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB

        Args:
            fact_rule (Fact|Rule) - the fact or rule to be added

        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        # if it's a fact
        if isinstance(fact_rule, Fact):
            # and it's not already in the KB
            if fact_rule not in self.facts:
                # add it
                self.facts.append(fact_rule)
                # for each rule in the KB, infer with this fact
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            # if the fact is already in the KB
            else:
                # if it's supported by stuff
                if fact_rule.supported_by:
                    # get the index of the fact in the list of facts
                    ind = self.facts.index(fact_rule)
                    # for each f that this fact is supported by
                    for f in fact_rule.supported_by:
                        # add the f to the list of facts that support the fact
                        self.facts[ind].supported_by.append(f)
        # if it's a rule
        elif isinstance(fact_rule, Rule):
            # if it's not already in the KB
            if fact_rule not in self.rules:
                # add it to the list of rules
                self.rules.append(fact_rule)
                # for each fact in the KB, infer stuff
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            # if it's already in the KB
            else:
                # if it's supported by stuff
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)

    def kb_assert(self, statement):
        """Assert a fact or rule into the KB

        Args:
            statement (Statement): Statement we're asserting in the format produced by read.py
        """
        printv("Asserting {!r}", 0, verbose, [statement])
        self.kb_add(Fact(statement) if factq(statement) else Rule(statement))

    def kb_ask(self, statement):
        """Ask if a fact is in the KB

        Args:
            statement (Statement) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        printv("Asking {!r}", 0, verbose, [statement])
        # if it's a fact
        if factq(statement):
            # fact-ify it
            f = Fact(statement)
            bindings_lst = ListOfBindings()
            # get a list of bindings
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else False

        else:
            print "Invalid ask:", statement
            return False

    def kb_retract(self, statement):
        """Retract a fact from the KB

        Args:
            statement (Statement) - Statement to be asked (will be converted into a Fact)

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [statement])
        ####################################################
        # Student code goes here
        f = Fact(statement)
        print "in kb_retract", f
        self.facts.remove(f)
        print f
        for s in f.supports_facts:
            print "148"
            print s

        # print "these are the facts", thefacts
        # thefacts.remove(f)
        # print "did i remove it", thefacts


class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here
        # _, test1 = read.parse_input("fact: (hero Ai)")
        # fact = Fact(test1)
        # get the first term on the LHS
        term1lhs = rule.lhs[0]
        # print term1lhs
        # do we have a match? if we do...
        bound = match(fact.statement, term1lhs)
        if bound:
            # print "at line 174" # WHY SO MANY TIMES
            # create a new LHS.
            lhs_temp = copy.deepcopy(rule.lhs)
            lhs_temp.remove(term1lhs)
            new_lhs = []
            for t in lhs_temp:
                new_lhs.append(instantiate(t, bound))
            # if there's nothing in the LHS, then we've satisfied
            # all the conditions of the original rule. So the RHS
            # should now become a fact
            if len(new_lhs) == 0:
                # the new fact will be supported by the rule and fact
                sup_by = [[fact, rule]] # Why does this not work
                m = match(fact.statement, rule.rhs)
                if m:
                    print "188", fact.statement, "matches", rule.rhs
                    print "gonna make a new fact with", rule.rhs,"and", bound
                new_fact = Fact(instantiate(rule.rhs, bound), sup_by)
                rule.supports_facts.append(new_fact)
                fact.supports_facts.append(new_fact)
                kb.kb_add(new_fact)
                # and then this rule supports this new fact

            # we still have conditions left, so we're going to make
            # a new, shorter rule
            else:
                # try to bind fact to RHS
                if match(fact.statement, rule.rhs):
                    print fact.statement, "matches", rule.rhs
                inst_rhs = instantiate(rule.rhs, bound)
                # if that works, then we have a new rule
                if inst_rhs:
                    # new rule is supported by the rule and fact
                    # it's basically the old rule, without first
                    # term of lhs and with a new rhs
                    sup_by = [[fact, rule]]
                    new_rule = Rule([new_lhs, inst_rhs], sup_by)
                    rule.supports_rules.append(new_rule)
                    fact.supports_rules.append(new_rule)
                    kb.kb_add(new_rule)
                    # and the old rule supports the new one

                else:
                    # otherwise create a new rule, same as old rule
                    # but without first term of lhs
                    sup_by = [[fact, rule]]
                    new_rule = Rule([new_lhs, rule.rhs], sup_by)
                    rule.supports_rules.append(new_rule)
                    fact.supports_rules.append(new_rule)
                    kb.kb_add(new_rule)
                    # and the old rule supports the new one

            # rule.supported_by.append(fact)
            # print rule.supported_by
