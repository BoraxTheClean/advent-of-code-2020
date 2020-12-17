def get_passport_number(s):

    pointer = 0


    start,end = 0,128

    while s[pointer] == 'F' or s[pointer] == 'B':
        if s[pointer] == 'F':
            end = (start+end)//2
        else:
            start = (start+end)//2
        pointer += 1
    row = (start + end)//2

    start,end = 0,8
    

    while s[pointer] == 'L' or s[pointer] == 'R':
        if s[pointer] == 'R':
            start = (start+end)//2
        elif s[pointer] == 'L':
            end = (start+end)//2
        if pointer >= len(s):
            break
        pointer += 1
        if pointer >= len(s):
            break

    column = (start+end)//2

    return row*8 + column

            




def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [str(i) for i in lines if i!='']
    #lines = [j.split(' ') for i in lines for j in i]
    m = 0
    for i in lines:
        m = max(m,get_passport_number(i))
    print(m)
    sort = []
    for i in lines:
         sort.append(get_passport_number(i))

    c = [0]*1000
    for i in sort:
        c[i] = 1

    for i in range(1,len(c)-1):
        if c[i] == 0 and c[i-1] ==1 and c[i-1] ==1:
#            print(i)
    print(c)


inp = get_input()
