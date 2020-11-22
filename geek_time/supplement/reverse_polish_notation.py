class Notation:
    def in_notation_to_pre_notation(self, notation=[]):
        priority_map = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 100, ")": 100}
        val_stack = []
        op_stack = []
        for c in reversed(notation):
            if self.isnum(c):
                val_stack.append(c)
            elif c == ")":
                op_stack.append(c)
            elif c == "(":
                while op_stack and op_stack[-1] != ")":
                    val_stack.append(op_stack.pop())
                if op_stack and op_stack[-1] == ")":
                    op_stack.pop()
            else:
                while True:
                    if not op_stack or op_stack[-1] == ")" or priority_map[c] >= priority_map[op_stack[-1]]:
                        op_stack.append(c)
                        break
                    else:
                        val_stack.append(op_stack.pop())

        while op_stack:
            val_stack.append(op_stack.pop())

        return list(reversed(val_stack))

    def calculate_pre_notation(self, notation):
        stack = []
        op_map = {
            "-": lambda x, y: x - y,
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        for c in reversed(notation):
            if c not in op_map:
                stack.append(int(c))
            else:
                x, y = stack.pop(), stack.pop()
                stack.append(op_map[c](x, y))

        return stack[0]

    def in_notation_to_post_notation(self, notation=[]):
        notation = ["10", "*", "(", "16", "-", "4", ")", "+", "5"]
        priority_map = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 100, ")": 100}
        val_stack = []
        op_stack = []
        for c in notation:
            if self.isnum(c):
                val_stack.append(c)
            elif c == "(":
                op_stack.append(c)
            elif c == ")":
                while op_stack and op_stack[-1] != "(":
                    val_stack.append(op_stack.pop())
                if op_stack and op_stack[-1] == "(":
                    op_stack.pop()
            else:
                while True:
                    if not op_stack or op_stack[-1] == "(" or priority_map[c] > priority_map[op_stack[-1]]:
                        op_stack.append(c)
                        break
                    else:
                        val_stack.append(op_stack.pop())
        while op_stack:
            val_stack.append(op_stack.pop())

        return val_stack

    def isnum(self, c):
        return c.isdigit() or (c[0] == "-" and c[1:].isdigit())


if __name__ == "__main__":
    n = Notation()
    print(n.in_notation_to_post_notation())
    print(n.calculate_pre_notation(["-", "*", "+", "3", "4", "5", "6"]))
    pre_notation = n.in_notation_to_pre_notation(["(", "3", "+", "4", ")", "*", "5", "-", "6", "+", "4"])
    print(n.calculate_pre_notation(pre_notation))
