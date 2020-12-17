def get_special_number(starting_numbers,STOPPING_POINT):
    m = {v:i for i,v in enumerate(starting_numbers[:-1])}

    print(starting_numbers)
    previous = starting_numbers.pop()
    count = len(starting_numbers) +1


    while count != STOPPING_POINT:
        previous_number = previous
        if (previous_number) not in m:
            previous = 0
        else:
            previous = count - m[previous_number] - 1
        m[previous_number] = count -1
        count+=1
    print(previous)
    return previous


def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split(',')
    lines = [int(i) for i in lines if i!='']
    assert 436 == get_special_number([0,3,6],2020)
    assert 1 == get_special_number([1,3,2],2020)
    assert 10== get_special_number([2,1,3],2020)
    assert 27== get_special_number([1,2,3],2020)
    assert 78== get_special_number([2,3,1],2020)
    assert 438== get_special_number([3,2,1],2020)
    assert 1836== get_special_number([3,1,2],2020)
    print(get_special_number(lines,2020))
    print(get_special_number(lines+[0],30000000))

inp = get_input()
