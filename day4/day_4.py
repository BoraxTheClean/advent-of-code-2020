MANDATORY_FIELDS = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
OPTIONAL_FIELDS = ['cid']

def is_passport_data_valid(data):
    d = {i.split(':')[0]:i.split(':')[1] for i in data}

    field_count = 0

    for i in d.keys():
        if i in MANDATORY_FIELDS and validate_field(i,d[i]):
            field_count += 1

    return field_count == len(MANDATORY_FIELDS)

def validate_field(field,data):
    if field == 'byr':
        try:
            data = int(data)
            return data >= 1920 and data <= 2002
        except:
            print("Validation failed on ",field," ",data)
            return False
    elif field == 'iyr':
        try:
            data = int(data)
            return data >= 2010 and data <= 2020
        except:
            print("Validation failed on ",field," ",data)
            return False
    elif field == 'eyr':
        try:
            data = int(data)
            return data >= 2020 and data <= 2030
        except:
            print("Validation failed on ",field," ",data)
            return False
    elif field == 'pid':
        try:
            return len(data) == 9 and int(data)
        except:
            print("Validation failed on ",field," ",data)
            return False
    elif field == 'ecl':
        try:
            return data == 'amb' or data == 'blu' or data =='brn' or data == 'gry' or data == 'grn' or data =='hzl' or data == 'oth'
        except:
            print("Validation failed on ",field," ",data)
    elif field == 'hgt':
        try:
            height = int(data[:-2])
            measure= data[-2:]
            if measure == 'cm':
                return height >= 150 and height <= 193
            elif measure == 'in':
                return height >= 59 and height <= 76
            else:
                raise Exception("Invalid measurement")
        except:
            print("Validation failed on ",field," ",data)
            return False
    elif field == 'hcl':
        try:
            one = data[0]
            two = data[1:]
            if one!='#':
                return False
            v = 'abcdef0123456789'
            for i in two:
                if i not in v:
                    return False
            return True
        except:
            print("Validation failed on ",field," ",data)
            return False


def get_input():
    f = open('input.txt')
    lines = f.read()
    lines = lines.split('\n\n')
    lines = [str(i) for i in lines if i!='']
    lines = [i.split() for i in lines]
    #lines = [j.split(' ') for i in lines for j in i]
    print(lines)
    valid_pp = 0
    for i in lines:
        valid_pp += 1 if is_passport_data_valid(i) else 0

    print(valid_pp)
        

inp = get_input()
