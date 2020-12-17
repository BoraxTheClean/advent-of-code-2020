def count_trees(lis,x,y):
    i,j = 0,0
    count = 0
    line_length = len(lis[0])

    while i < len(lis) and j < len(lis[i]):
        print(lis[i][j])
        if lis[i][j] == '#':
            count+= 1
        j += x
        j %= line_length
        i += y

    return count

    


def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [str(i) for i in lines if i!='']
    print(lines)
    print(count_trees(lines,3,1)*count_trees(lines,1,1)*count_trees(lines,5,1)*count_trees(lines,7,1)*count_trees(lines,1,2))

inp = get_input()
