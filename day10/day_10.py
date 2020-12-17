def parse_jumps(jolts):
    start = 0
    ones,threes= 0,0
    for i in jolts:
        diff = i - start
        if diff > 3:
            raise Exception("Invalid joltage compatability, gap is longer than 3 Jolts",start,i)
        elif diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        start = i

    return (ones,threes)
memo={}
def count_valid_combos(jolts,pointer):
    if pointer in memo:
        return memo[pointer]
    if pointer == len(jolts)-1:
        return 1
    else:
        if pointer == -1:
            curr = 0
        else:
            curr = jolts[pointer]
        pointer += 1
        c = 0
        while pointer < len(jolts) and jolts[pointer] <= curr + 3:
            memo[pointer] = count_valid_combos(jolts,pointer)
            c += memo[pointer]
            pointer += 1
        return c

def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [int(i) for i in lines if i != '']
    lines.sort()
    print(lines)
    one_jump,three_jump = 0,1
    result = parse_jumps(lines)
    one_jump += result[0]
    three_jump += result[1]
    print(one_jump*three_jump)
    print(count_valid_combos(lines,-1))
    f = open('input-test.txt')
    global memo 
    memo = {}
    lines = f.read()
    lines = lines.split('\n')
    lines = [int(i) for i in lines if i != '']
    lines.sort()
    print(lines)
    one_jump,three_jump = 0,1
    result = parse_jumps(lines)
    one_jump += result[0]
    three_jump += result[1]
    print(one_jump*three_jump)
    print(count_valid_combos(lines,-1))
    


inp = get_input()
