import copy
class PocketDimensionSquared:
    def __init__(self,initial_state):
        self.length = len(initial_state)
        print("PDS Length",self.length)
        length = self.length
        self.matrix = [PocketDimension(length=length) for _ in range(length)] #TODO Length
        self.matrix[0].matrix[0] = initial_state
        self.assert_matrix()

    def tick(self):
        self.pad_matrix()
        length = self.length
        matrix_copy = [copy.deepcopy(i) for i in self.matrix]
        for x in range(length):
            for y in range(length):
                for z in range(length):
                    for w in range(length):
                        neighbors = self.get_neighbors(x,y,z,w)
                        cube = self.matrix[x].matrix[y][z][w]
                        if cube == '.':
                            if neighbors == 3:
                                matrix_copy[x].matrix[y][z][w] = '#'
                        elif cube == '#':
                            if neighbors == 2 or neighbors == 3:
                                continue
                            else:
                                matrix_copy[x].matrix[y][z][w] = '.'
                        else:
                            raise Exception("Invalid state encountered",cube)
        self.matrix = matrix_copy

    def get_neighbors(self,x,y,z,w):
        total = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                for k in range(z-1,z+2):
                    for l in range(w-1,w+2):
                        if x==i and y==j and z==k and w==l:
                            continue
                        try:
                            total += self.matrix[i].matrix[j][k][l] == '#'
                        except:
                            continue
        return total

    def assert_matrix(self):
        return self.length == len(self.matrix)

    def count_active(self):
        active = 0
        for i in self.matrix:
            active += i.count_active()
        return active

    def pad_matrix(self):
        for m in self.matrix:
            m.pad_matrix()
        self.length += 2
        self.matrix = [PocketDimension(length=self.length)] + self.matrix + [PocketDimension(length=self.length)] #TODO Length
        self.assert_matrix()

class PocketDimension:
    def __init__(self,initial_state=None,length=0):
        if initial_state:
            self.length = len(initial_state[0])
        else:
            self.length = length
        length = self.length
        print("PD Length",length)
        self.matrix = [[['.']*length for _ in range(length)] for _ in range(length)]
        if initial_state:
            self.matrix[0] = initial_state
        self.assert_matrix()

    def tick(self):
        self.pad_matrix()
        matrix_copy = [[self.matrix[x][y][:] for y in range(self.length)] for x in range(self.length)]

        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                for z in range(len(self.matrix[x][y])):
                    neighbors = self.get_neighbors(x,y,z)
                    cube = self.matrix[x][y][z]
                    if cube == '.':
                        if neighbors == 3:
                            matrix_copy[x][y][z] = '#'
                    elif cube == '#':
                        if neighbors == 2 or neighbors == 3:
                            continue
                        else:
                            matrix_copy[x][y][z] = '.'
                    else:
                        raise Exception("Invalid state encountered",cube)
        self.matrix = matrix_copy

    def pretty_print(self):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                print(self.matrix[x][y])


    def pad_matrix(self):
        self.length += 2
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = ['.'] + self.matrix[x][y] + ['.']
        for x in range(len(self.matrix)):
            self.matrix[x] = [['.']*self.length] + self.matrix[x] + [['.']*self.length ]
        self.matrix = [[['.']*self.length for _ in range(self.length)] for _ in range(1)] + self.matrix + [[['.']*self.length for _ in range(self.length)] for _ in range(1)]
#        self.assert_matrix()

    def assert_matrix(self):
        length = self.length
        assert len(self.matrix) == length
        for x in self.matrix:
            assert len(x) == length
            for y in x:
                assert len(y) == length
                for z in y:
                    assert len(z) == 1

    def count_active(self):
        active = 0
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                for z in range(len(self.matrix[x][y])):
                    active += self.matrix[x][y][z] == '#'
        return active


    def get_neighbors(self,x,y,z):
        neighbors = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                for k in range(z-1,z+2):
                    if i == x and j == y and k==z:
                        continue
                    try:
                        neighbors += self.matrix[i][j][k] == '#'
                    except Exception as e:
                        continue
        return neighbors

def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    matrix = [list(i) for i in lines if i!='']
    pd = PocketDimension(matrix)
    for _ in range(6):
        pd.tick()
    print(pd.count_active())
    pds = PocketDimensionSquared(matrix)
    for _ in range(6):
        print("Tick",_)
        pds.tick()
    print(pds.count_active())

        
inp = get_input()
