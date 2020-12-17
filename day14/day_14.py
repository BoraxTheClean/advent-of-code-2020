class DockMemory:
    def __init__(self,instructions):
        self.mask = 'X'*36
        self.instructions = instructions
        self.memory = dict()

    def parse_instructions(self):
        def parse_mask(instruction):
            return instruction.split(' ')[2]
        def parse_memory(instruction):
            addr = instruction[4:].split(']')[0]
            val = instruction.split(' ')[-1]
            return (int(addr),int(val))
        for i in self.instructions:
            if i.startswith('mem'):
                addr,value = parse_memory(i)
                self.set_memory(addr,value)
            elif i.startswith('mask'):
                self.mask = parse_mask(i)
            else:
                raise Exception("Unknown instruction encountered",i)

    def set_memory(self,addr,val):
        val = self.mask_value(val)
        self.memory[addr] = val

    def mask_value(self,val):
        def convert_to_bin(x):
            s = ''
            while len(s) != 36:
                s = str(x % 2) + s
                x //= 2
            return s
        val = convert_to_bin(val)
        val = list(val)
        for i in range(len(self.mask)):
            ch = self.mask[i]
            if ch == 'X':
                continue
            elif ch == '1':
                val[i] = '1'
            elif ch == '0':
                val[i] = '0'
            else:
                raise Exception("Encountered unexpected bit",ch,"in bitmask",self.mask)

        def convert_to_int(masked_value):
            extracted_int = 0
            for i in range(len(masked_value)):
                ch = masked_value[i]
                if ch == '1':
                    extracted_int += 2**(35-i)
            return extracted_int

        return convert_to_int(val)

    def sum_memory(self):
        i = 0
        for v in self.memory.values():
            i += v
        return i
                    

class DockMemory2:
    def __init__(self,instructions):
        self.mask = 'X'*36
        self.instructions = instructions
        self.memory = dict()

    def parse_instructions(self):
        def parse_mask(instruction):
            return instruction.split(' ')[2]
        def parse_memory(instruction):
            addr = instruction[4:].split(']')[0]
            val = instruction.split(' ')[-1]
            return (int(addr),int(val))
        for i in self.instructions:
            if i.startswith('mem'):
                addr,value = parse_memory(i)
                self.set_memory(addr,value)
            elif i.startswith('mask'):
                self.mask = parse_mask(i)
            else:
                raise Exception("Unknown instruction encountered",i)

    def set_memory(self,addr,val):
        addrs= self.mask_memory(addr)
        for a in addrs:
            self.memory[a] = val

    def mask_memory(self,val):
        def convert_to_bin(x):
            s = ''
            while len(s) != 36:
                s = str(x % 2) + s
                x //= 2
            return s
        val = convert_to_bin(val)
        val = list(val)
        for i in range(len(self.mask)):
            ch = self.mask[i]
            if ch == '1' or ch == 'X':
                val[i] = ch

        addrs = []

        def convert_to_int(masked_value):
            extracted_int = 0
            for i in range(len(masked_value)):
                ch = masked_value[i]
                if ch == '1':
                    extracted_int += 2**(35-i)
            return extracted_int

        for i in range(2**val.count('X')):
            temp_i = i
            temp_val = val[:]
            while temp_val.count('X') != 0:
                index = temp_val.index('X')
                temp_val[index] = str(temp_i % 2)
                temp_i //= 2
            addrs.append(convert_to_int(temp_val))


        return addrs

    def sum_memory(self):
        i = 0
        for v in self.memory.values():
            i += v
        return i
                    

def get_input():
    f = open('input-test.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.strip() for i in lines if i!='']
    mem = DockMemory(lines)
    mem.parse_instructions()
    print('Part Test 1',mem.sum_memory())
    mem = DockMemory2(lines)
    mem.parse_instructions()
    print('Part Test 2',mem.sum_memory())
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.strip() for i in lines if i!='']
    mem = DockMemory(lines)
#    mem.parse_instructions()
#    print('Part 1',mem.sum_memory())
    mem = DockMemory2(lines)
    mem.parse_instructions()
    print('Part 2',mem.sum_memory())

inp = get_input()
