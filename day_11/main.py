from inspect import stack


def to_posfix(s: str) -> str:
    stack = []
    posfix = ""

    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            while stack[-1] not in "([{":
                posfix += stack.pop()
            stack.pop()
        elif c in "+-*^":
            while stack and stack[-1] not in "([{" and stack[-1] != c:
                posfix += stack.pop()
            stack.append(c)
        else:
            posfix += c

    while stack:
        posfix += stack.pop()

    return posfix


if __name__ == "__main__":
    expr = "3+4"
    print(to_posfix(expr))

    expr = "3-4+5"
    print(to_posfix(expr))

    expr = "(3*4)+(5*7)"
    print(to_posfix(expr))

    expr = "[(3*4)+(5*7)]"
    print(to_posfix(expr))
