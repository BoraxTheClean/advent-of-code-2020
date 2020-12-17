import math

def get_soonest_bus(start,bus_ids):
    c = start
    m = math.inf
    bus_id = 0
    minutes = 0
    for i in bus_ids:
        minutes = i - (start % i)
        m = min(m,minutes)
        if m == minutes:
            bus_id = i
            minutes = i - (start % i)
    print(m)
    print(bus_id)
    return m*bus_id


def get_consecutive_busses(bus_ids):
    sparse_ids = []
    real_ids = []
    offset = 0
    for i in bus_ids:
        if i != 'x':
            sparse_ids.append(offset)
            real_ids.append(int(i))
        offset += 1
    print(sparse_ids)
    increment = real_ids[0]

    pointer = 1

    while pointer < len(sparse_ids): 
        while sparse_ids[pointer] % real_ids[pointer] !=0:
            for i in range(len(sparse_ids)):
                sparse_ids[i] += increment
        print("Increasing increment from",increment,"by multiplying by",real_ids[pointer],"to",increment*real_ids[pointer])
        increment *= real_ids[pointer]
        pointer += 1

    return sparse_ids[0]
        

def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i for i in lines if i!='']
    start = int(lines[0])
    bus_ids = [int(i) for i in lines[1].split(',') if i != 'x']
    print(start,bus_ids)
    print('Part 1',get_soonest_bus(start,bus_ids))
    f = open('input-test.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i for i in lines if i!='']
    start = int(lines[0])
    bus_ids = [i for i in lines[1].split(',') ]
    print(start,bus_ids)
    print('Part Test 2',get_consecutive_busses(bus_ids))
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i for i in lines if i!='']
    start = int(lines[0])
    bus_ids = [i for i in lines[1].split(',') ]
    print(start,bus_ids)
    print('Part 2',get_consecutive_busses(bus_ids))

inp = get_input()
