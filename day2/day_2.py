def password_validator(constraint,char,password):
    start,end = parse_range(constraint)
    return bool(password[start-1] == char) != bool(password[end-1] == char)


def parse_range(constraint):
    constraint = constraint.split('-')
    return int(constraint[0]),int(constraint[1])


def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.split(' ') for i in lines if i!='']
    print(lines)
    total = 0
    for constraint,char,password in lines:
        char = char.strip(':')
        if password_validator(constraint,char,password):
            total += 1
    print(total)

inp = get_input()
