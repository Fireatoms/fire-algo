# stack


def execute(m, n, op):
    if op == '+':
        res = m + n
    elif op == '-':
        res = m - n
    elif op == '*':
        res = m * n
    else:
        res = m / n

    return res


def str_to_num(e):
    try:
        return int(e)
    except ValueError:
        return float(e)


# calculate: support four methods: + - * /
# No exception is considered
def calculate(expression):
    symbol_priority = {'+': 0, '-': 0, '*': 1, '/': 1}
    num_stack = []
    symbol_stack = []

    for e in expression:
        if e in symbol_priority:
            while symbol_stack and symbol_priority[e] <= symbol_priority[symbol_stack[-1]]:
                n = num_stack.pop()
                m = num_stack.pop()
                op = symbol_stack.pop()
                res = execute(m, n, op)
                num_stack.append(res)
            symbol_stack.append(e)
        else:
            num_stack.append(str_to_num(e))

    while symbol_stack:
        op = symbol_stack.pop()
        n = num_stack.pop()
        m = num_stack.pop()
        tmp = execute(m, n, op)
        num_stack.append(tmp)

    return num_stack.pop()


if __name__ == "__main__":
    res = calculate('3+4*8-4/2*9')
    print(res)