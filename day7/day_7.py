'''
Nested Bags = [(big bag,[smaller bags, that fit bag, in big bag])...]

Goal:
    Find all bags that can contain a shiny gold bag.

Strategy:
    Create an inverted index of the form:
        nested bag -> [list of, big bags, that can, hold nested bag]

    Add index[shiny gold bag] to search_list
        Add index[each bag] to search_list

    return all visited bags

'''


def solution_part_one(nested_bags):
    inverted_index = make_inverted_index(nested_bags)
    search = inverted_index['shiny gold bag']

    return_set = set()

    total = 0

    while search:
        next_search = []
        for bag in search:
            return_set.add(bag)
            if bag in inverted_index:
                next_search.extend(inverted_index[bag])
        total += len(search)
        search = next_search

    return len(return_set)
def make_inverted_index(nested_bags):
    m = {}
    for big_bag,inner_bags in nested_bags:
        for small_bag in inner_bags:
            if small_bag in m:
                m[small_bag].append(big_bag)
            else:
                m[small_bag] = [big_bag]

    return m
def solution_part_two(nested_bags):
    quantity_map = make_quantity_map(nested_bags)
    print(quantity_map)
    total = 0
    total =  total_bag(quantity_map,'shiny gold bag')

    return total

def total_bag(bag_map,bag):
    if bag not in bag_map or bag_map[bag] == [(1,'no other bag')]:
        return 0
    total = 0

    for quantity,inner_bag in bag_map[bag]:
        total += quantity*total_bag(bag_map,inner_bag)+1*quantity

    print(bag, ' ',total)

    return total



def make_quantity_map(nested_bags):
    m = {}
    for big_bag,inner_bags in nested_bags:
        for small_bag in inner_bags:
            quantity,bag = parse_inner_bag(small_bag)
            if big_bag in m:
                m[big_bag].append((quantity,bag))
            else:
                m[big_bag] = [(quantity,bag)]

    return m

def parse_inner_bag(small_bag):
    pointer = 0
    while small_bag[pointer] in '0123456789':
        pointer += 1
    if pointer == 0:
        return (1,small_bag)
    else:
        return (int(small_bag[:pointer]),small_bag[pointer+1:])

def get_input():
    f = open('input.txt-test')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.split('contain') for i in lines if i!='']
    lines = [(i.strip('. ').rstrip('s'),j.strip().split(',')) for i,j in lines if i!='']
    lines = [(i,[k.strip('.0123456789 ').rstrip('s') for k in j]) for i,j in lines if i!='']
    found_gold = True
    previous_size = 1
    print(solution_part_one(lines))
    f.seek(0)
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.split('contain') for i in lines if i!='']
    lines = [(i.strip('. ').rstrip('s'),j.strip().split(',')) for i,j in lines if i!='']
    lines = [(i,[k.strip().rstrip('s.') for k in j]) for i,j in lines if i!='']
    print(lines)
                
    print(solution_part_two(lines))




inp = get_input()
