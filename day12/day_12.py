def distance_2(instructions):
    lateral = 0
    longitudal = 0
    waypoint = [10,1] #Eastt 10, North 1
    orientation = 0 # East
    for direction,length in instructions:
        if direction == 'N':
            waypoint[1] += length
        elif direction == 'S':
            waypoint[1] -= length
        elif direction == 'E':
            waypoint[0] += length
        elif direction == 'W':
            waypoint[0] -= length
        elif direction == 'L':
            length = length % 360
            if length == 90:
                waypoint[0],waypoint[1] = waypoint[1] * -1, waypoint[0]
            elif length == 180:
                waypoint[0],waypoint[1] = waypoint[0] * -1, waypoint[1] * -1
            elif length == 270:
                waypoint[0],waypoint[1] = waypoint[1], waypoint[0] * -1
        elif direction == 'R':
            length = length % 360
            if length == 90:
                waypoint[0],waypoint[1] = waypoint[1], waypoint[0] * -1
            elif length == 180:
                waypoint[0],waypoint[1] = waypoint[0] * -1, waypoint[1] * -1
            elif length == 270:
                waypoint[0],waypoint[1] = waypoint[1] * -1, waypoint[0]
        elif direction == 'F':
            longitudal += waypoint[1]*length
            lateral += waypoint[0]*length
    return abs(lateral)+abs(longitudal)

def distance(instructions):
    lateral = 0
    longitudal = 0
    orientation = 0 # East
    for direction,length in instructions:
        if direction == 'N':
            longitudal += length
        elif direction == 'S':
            longitudal -= length
        elif direction == 'E':
            lateral += length
        elif direction == 'W':
            lateral -= length
        elif direction == 'L':
            orientation = (orientation + (length // 90) ) % 4
        elif direction == 'R':
            orientation = (orientation - (length // 90) ) % 4
        elif direction == 'F':
            if orientation == 0:
                lateral += length
            elif orientation == 1:
                longitudal += length
            elif orientation == 2:
                lateral -= length
            elif orientation == 3:
                longitudal -= length
    return (lateral,longitudal)

def get_input():
    f = open('input-test.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [(i[0],int(i[1:])) for i in lines if i != '']
    print('Part 1 Test',distance(lines))
    print('Part 2 Test',distance_2(lines))
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [(i[0],int(i[1:])) for i in lines if i != '']
    print('Part 1',distance(lines))
    print('Part 2',distance_2(lines))
    


inp = get_input()
