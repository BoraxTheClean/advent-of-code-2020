from collections import defaultdict

def find_xmas_anomaly(l,offset):
    stack = []
    m = {}
    for i in range(offset):
        stack.append(l[i])
        if l[i] in m:
            m[l[i]] += 1
        else:
            m[l[i]] = 1

    for i in range(offset,len(l)):
        target = l[i]
        if not two_sum(l[i],m):
            print(stack)
            print(len(stack))
            return target
        popped_element = stack.pop(0)
        m[popped_element] -= 1
        if target in m:
            m[target] += 1
        else:
            m[target] = 1
        stack.append(target)

    return False


def two_sum(target,m):
    for i in m.keys():
        if m[i] < 1:
            continue
        if target - i in m and m[target - i] > 0:
            return True
    return False

def crack_the_code(target,l):
    ceiling = l.index(target)
    for length in range(2,ceiling):
        for i in range(ceiling-length+1):
            sub_set = l[i:i+length]
            if sum(sub_set) == target:
                print(sub_set)
                return (min(sub_set),max(sub_set))

def get_input():
    f = open('input-test.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [int(i) for i in lines if i != '']
    print(lines)
    anomaly = find_xmas_anomaly(lines,5)
    print("Part 1 Test",anomaly)
    code = crack_the_code(anomaly,lines)
    print("Part 2 Test",code,sum(code))
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [int(i) for i in lines if i != '']
    print(lines)
    anomaly = find_xmas_anomaly(lines,25)
    print("Part 1",anomaly)
    code = crack_the_code(anomaly,lines)
    print("Part 2 ",code,sum(code))
    


inp = get_input()
