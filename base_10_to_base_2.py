
def convert(base_10):
    if (base_10 < 0):
        return False

    stack = []
    while (base_10):
        stack.append(base_10 % 2)
        base_10 = base_10 // 2

    base_2 = ''
    while (stack):
        base_2 += str(stack.pop())

    return base_2
        
