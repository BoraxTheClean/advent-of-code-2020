class VM:
    def __init__(self,instructions):
        self.acc = 0
        self.executed = {}
        self.instruction_pointer = 0
        self.instructions = instructions

    def execute_instruction(self):
        if self.instruction_pointer > len(self.instructions):
            raise Exception("End of instruction set reached")
        if self.instruction_pointer in self.executed:
            raise Exception("Loop detected")

        self.executed[self.instruction_pointer] = True

        command = self.instructions[self.instruction_pointer]
        instruction = command[0]
        argument = command[1]

        if instruction == 'nop':
            self.instruction_pointer += 1
        elif instruction == 'acc':
            self.acc += int(argument)
            self.instruction_pointer += 1
        elif instruction == 'jmp':
            self.instruction_pointer += int(argument)
        else:
            raise Exception("Invalid instruction encountered ",instruction)

        return False


def solution_part_one_refactored(vm):
    executed = {}
    acc = 0
    i = 0
    while vm.instruction_pointer < len(vm.instructions):
        if vm.instruction_pointer in vm.executed:
            return vm.acc
        vm.execute_instruction()

def solution_part_two_refactored(vm):
    executed = {}
    acc = 0
    i = 0
    while vm.instruction_pointer < len(vm.instructions):
        if vm.instruction_pointer in vm.executed:
            return False
        vm.execute_instruction()
    return vm.acc

def flip_instruction(commands,n):
    if len(commands) < n:
        raise Exception("Length exception")
    pointer = 0
    while n and pointer < len(commands):
        if commands[pointer][0] == 'jmp' or commands[pointer][0] == 'nop':
            n -= 1
        pointer += 1
    if commands[pointer-1][0] == 'jmp':
        commands[pointer-1][0] = 'nop'
    elif commands[pointer-1][0] == 'nop':
        commands[pointer-1][0] = 'jmp'
    else:
        raise Exception("Command not recognized, ",commands[pointer-1][0])

def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.split(' ') for i in lines if i != '']
    vm = VM(lines)
    print('Part 1 Refactored',solution_part_one_refactored(vm))
    skipped = {}
    n = 1
    result = solution_part_two_refactored(VM(lines))
    while not result:
        flip_instruction(lines,n)
        vm = VM(lines)
        result = solution_part_two_refactored(vm)
        flip_instruction(lines,n)
        n += 1
    print('Part 2 Refactored',result)


inp = get_input()
