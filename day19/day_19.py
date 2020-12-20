def is_valid(s,rule,rule_map,pointer):
    if type(rule_map[rule]) is str:
        try:
            if s[pointer] == rule_map[rule]:
                return pointer + 1
            else:
                return pointer
        except:
#            print("Exception when trying to index into",s,"at pointer",pointer)
            return pointer
    for r in rule_map[rule]:
        satisfied = True
        temp_pointer = pointer
        for statement in r:
            if rule in [8,11,31,42]:
                pass
            valid = is_valid(s,statement,rule_map,temp_pointer)
            if valid == temp_pointer:
                satisfied = False
                break
            temp_pointer = valid
        if satisfied:
            return temp_pointer
    return pointer 





def get_input(): 
    f = open('input.txt') 
    lines = f.read()
    lines = lines.split('\n\n')
    rules = lines[0]
    rules = rules.split('\n')
    messages = lines[1]
    messages = messages.split('\n')

    rule_map = {}

    for r in rules:
        r = r.split(':')
        rule_id  = int(r[0])
        logic = r[1]
        logic = logic.strip()

        if '"' in logic:
            rule_map[rule_id] = logic.strip('"')
        else:
            rule_map[rule_id] = []
            for i in logic.split('|'):
                sub_rule = []
                for j in i.split(' '):
                    if j == '':
                        continue
                    sub_rule.append(int(j))
                rule_map[rule_id].append(sub_rule)
    valid = 0
    print(rule_map)
    print(rule_map[8])
    print(rule_map[11])
    for m in messages:
        if m == '':
            continue
        result = is_valid(m,0,rule_map,0)
        if result == len(m):
            valid += 1
            print(m)

    print('part 1',valid)




        
inp = get_input()
