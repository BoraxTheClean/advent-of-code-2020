class RulesEngine:
    def __init__(self,rules):
        self.rules = []
        self.parse_rules(rules)
        self.field_ids = [None]*len(rules)

    def parse_rules(self,rules):
        for rng,rng_two in rules:
            rule_list = []
            rng.split('-')
            rng = [int(i) for i in rng.split('-')]
            rng_two.split('-')
            rng_two = [int(i) for i in rng_two.split('-')]
            tu = tuple(rng)
            rule_list.append(tu)
            tu = tuple(rng_two)
            rule_list.append(tu)
            self.rules.append(rule_list)

    def process_ticket(self,ticket):
        tickets = [int(i) for i in ticket]
        satisfies_a_rule = {}
        rule_rules = []
        invalid = []
        for j,r in enumerate(self.rules):
            s = self.verify_rule_two(tickets,r)
            for i in s:
                satisfies_a_rule[i] = True
            rule_rules.append(s)
        for i in range(len(tickets)):
            if i not in satisfies_a_rule:
                invalid.append(i)
        if not invalid:
            for i,f in enumerate(self.field_ids):
                if f is None:
                    self.field_ids[i] = set(rule_rules[i])
                else:
                    curr_set = f
                    self.field_ids[i] = curr_set.intersection(set(rule_rules[i]))
        else:
            print("invalid")


    def verify_rule_two(self,ticket,rule):
        satisfying_nums = []
        for i,num in enumerate(ticket):
            r1,r2 = rule[0],rule[1]
            if self.verify_ticket_rule(num,r1) or self.verify_ticket_rule(num,r2):
                satisfying_nums.append(i)
        return satisfying_nums

        


    def verify_ticket(self,ticket):
        tickets = [int(i) for i in ticket]
        satisfies_a_rule = {}
        rule_rules = []
        for j,r in enumerate(self.rules):
            s = self.verify_rule(tickets,r)
            for i in s:
                satisfies_a_rule[i] = True
            rule_rules.append([tickets.index(i) for i in s])
        invalid = [] 
        for i in tickets:
            if i not in satisfies_a_rule:
                invalid.append(i)

        return invalid
        

    def verify_rule(self,ticket,rule):
        satisfying_nums = []
        for num in ticket:
            r1,r2 = rule[0],rule[1]
            if self.verify_ticket_rule(num,r1) or self.verify_ticket_rule(num,r2):
                satisfying_nums.append(num)
        return satisfying_nums

    def verify_ticket_rule(self,ticket_value,rule):
        upper,lower=rule[1],rule[0]
        return ticket_value >= lower and ticket_value <= upper





def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n\n')
    rules,my_ticket,other_tickets = lines[0],lines[1],lines[2]
    other_tickets = [i.split(',') for i in other_tickets.split('\n')[1:] if i != '']
    rules = [i.split(':') for i in rules.split('\n') if i!='']
    rules = [i[1].strip().split('or') for i in rules if i!='']
    rules = [(i[0].strip(),i[1].strip() )for i in rules if i!='']
    engine = RulesEngine(rules)
    invalid = 0
    for t in other_tickets:
        for i in engine.verify_ticket(t):
            invalid += i
    print(invalid)
    for t in other_tickets:
        engine.process_ticket(t)

    print(engine.field_ids)
    my_ticket = my_ticket.split('\n')[-1]
    my_ticket = [int(i) for i in my_ticket.split(',')]
    print(my_ticket)
    could_match = [[False for _ in my_ticket] for _ in rules]
    for i,rule in enumerate(engine.field_ids):
        for possible_match in rule:
            could_match[i][possible_match] = True
    print(could_match)
    matches = []
    for _ in range(len(my_ticket)):
        row_sums = [sum(row) for row in could_match]
        i = row_sums.index(1)
        j = could_match[i].index(True)
        matches.append((i,j))
        could_match[i][j] = False
        for x in range(len(my_ticket)):
            could_match[x][j] = False
    print(matches)
    part2 = 1
    for i,j in matches:
        if i < 6:
            part2 *= my_ticket[j]
    print("Part 2",part2)

        
inp = get_input()
