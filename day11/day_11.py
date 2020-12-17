class SeatLayout:
    def __init__(self,seats):
        self.seats = seats

    def tick(self):
        copy = [i[:] for i in self.seats]
        stable = True
        for i,row in enumerate(self.seats):
            for j,seat in enumerate(row):
                if seat == '.': # Floor, do nothing
                    continue
                else:
                    occupied = self.count_adjacent_occupied_seats(i,j)
                    if seat == 'L' and occupied == 0:
                        stable = False
                        copy[i][j] = '#'
                    elif seat == '#' and occupied >= 4:
                        stable = False
                        copy[i][j] = 'L'
        self.seats = copy
        return stable

    def tick_2(self):
        copy = [i[:] for i in self.seats]
        stable = True
        for i,row in enumerate(self.seats):
            for j,seat in enumerate(row):
                if seat == '.': # Floor, do nothing
                    continue
                else:
                    occupied = self.count_adjacent_occupied_seats_2(i,j)
                    if seat == 'L' and occupied == 0:
                        stable = False
                        copy[i][j] = '#'
                    elif seat == '#' and occupied >= 5:
                        stable = False
                        copy[i][j] = 'L'
        self.seats = copy
        return stable

    def count_occupied(self):
        occ = 0
        for row in self.seats:
            for seat in row:
                if seat == '#':
                    occ += 1
        return occ

    def count_adjacent_occupied_seats(self,x,y):
        return self.is_occupied(x+1,y)  + self.is_occupied(x,y+1) + self.is_occupied(x-1,y) + self.is_occupied(x,y-1) + self.is_occupied(x+1,y+1)  + self.is_occupied(x-1,y+1)  + self.is_occupied(x-1,y-1)  + self.is_occupied(x+1,y-1)

    def is_occupied(self,x,y):
        if x >= len(self.seats) or x < 0 or y < 0 or y >= len(self.seats[x]):
            return False
        return self.seats[x][y] == '#'

    def line_of_sight(self,x,y,x_delta,y_delta):
        x += x_delta
        y += y_delta
        seat = self.is_occupied_2(x,y)
        while seat == '.':
            x += x_delta
            y += y_delta
            seat = self.is_occupied_2(x,y)
        return seat == '#'

    def count_adjacent_occupied_seats_2(self,x,y):
        return self.line_of_sight(x,y,1,0)  + self.line_of_sight(x,y,0,1) + self.line_of_sight(x,y,-1,0) + self.line_of_sight(x,y,0,-1) + self.line_of_sight(x,y,1,1)  + self.line_of_sight(x,y,-1,1)  + self.line_of_sight(x,y,-1,-1)  + self.line_of_sight(x,y,1,-1)
    
    def is_occupied_2(self,x,y):
        if x >= len(self.seats) or x < 0 or y < 0 or y >= len(self.seats[x]):
            return False
        return self.seats[x][y]

def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [list(i) for i in lines if i != '']
    seats = SeatLayout(lines)
    while not seats.tick():
        pass
    print('Part 1',seats.count_occupied())
    seats = SeatLayout(lines)
    while not seats.tick_2():
        pass
    print('Part 2',seats.count_occupied())
    f = open('input-test.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [list(i) for i in lines if i != '']
    seats = SeatLayout(lines)
    while not seats.tick():
        pass
    print('Part 1 Test',seats.count_occupied())
    seats = SeatLayout(lines)
    while not seats.tick_2():
        pass
    print('Part 2 Test',seats.count_occupied())
    


    


inp = get_input()
