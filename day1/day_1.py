def two_sum(lis):
    m = { i:True for i in lis }

    for i in lis:
        if 2020 - i in m:
            return (2020 - i) * i

    return -1

def three_sum(lis):
    seen = { i:True for i in lis }
    
    for i,m in enumerate(lis):
        for j,n in enumerate(lis):
            if i >= j:
                continue
            if 2020 - m - n in seen:
                return m * n * (2020 - m - n)


def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i for i in lines if i!='']
    nums = [int(i.strip()) for i in lines]
    return nums

inp = get_input()
print(two_sum(inp))
print(three_sum(inp))
