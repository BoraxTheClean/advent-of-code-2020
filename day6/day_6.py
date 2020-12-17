def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n\n')
    lines = [i.split('\n') for i in lines if i!='']

    lines[-1].remove('')

    total = 0
    print(lines)
    for i in lines:
        se = set()
        for s in i:
            for c in s:
                se.add(c)
        for k in m.keys():
        m = {}
        for s in i:
            for c in s:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
        for k in m.keys():
            if m[k] == len(i):
                total += 1
    print('Part 1 ',total2)

    print('Part 2 ,'total)


inp = get_input()
