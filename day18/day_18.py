'''
I want to transform this
    4 + (9 + 7 * (6 + 3 + 9 + 7))
    4 + (16 * (6 + 3 + 9 +7))
    4 + (16 * 25)
    4 + 400
    444
Into:

    


'''

def get_operating_order(eq,advanced=False):
    ops = []
    stk = []
    for t in eq:
        if t == '(':
            # Pop off equation until we find our closing parens
            while ops[-1] != ')':
                stk.append(ops.pop())
            # Remove parens
            ops.pop()
        elif t == '*':
            while advanced and ops and ops[-1] == "+":
                stk.append(ops.pop())
            ops.append(t)
        elif t in ')+':
            ops.append(t)
        else:
            stk.append(int(t))
    while ops:
        stk.append(ops.pop())

    cur = []
    for v in stk:
        if v == '+':
            x = cur.pop()
            y = cur.pop()
            cur.append(x + y)
        elif v == '*':
            x = cur.pop()
            y = cur.pop()
            cur.append(x * y)
        else:
            cur.append(v)
    return cur[0]





def get_input(): 
    f = open('input.txt') 
    lines = f.read()
    lines = lines.split('\n')
    lines = [i.split(' ') for i in lines if i!='']
    lines = [''.join(i) for i in lines if i!='']
    lines = [list(i) for i in lines if i!='']
    s = 0
    s_2 = 0
    for l in lines:
        l.reverse()
        l = ''.join(l)
        l.split()
        s += get_operating_order(l)
        s_2 += get_operating_order(l,advanced=True)
    print(s)
    print(s_2)



        
inp = get_input()
