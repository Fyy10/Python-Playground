# naive implementation of a calculator
def calc(expr: str):
    # remove spaces
    e = expr.replace(' ', '')

    # split nums and ops
    nums = []
    ops = []
    prev = 0
    n = len(e)
    for i in range(n):
        if e[i] in '+-*/':
            if i == 0:
                # deal with the first negative number
                # e.g., '-1 + 2'
                continue

            nums.append(int(e[prev:i]))
            ops.append(e[i])
            prev = i + 1

    # append the last number
    nums.append(int(e[prev:]))
    # print(nums)
    # print(ops)

    # eval for all * and / from left to right
    while '*' in ops or '/' in ops:
        # first * or /
        i = 0
        for i in range(len(ops)):
            if ops[i] in '*/':
                break

        op = ops[i]
        num1 = nums[i]
        num2 = nums[i+1]
        if op == '*':
            res = num1 * num2
        elif op == '/':
            res = num1 / num2
        else:
            # unreachable
            raise ValueError(ops[i] + ' is not * or /')

        nums = nums[:i] + [res] + nums[i+2:]
        ops = ops[:i] + ops[i+1:]

    # eval for all + and - from left to right
    while '+' in ops or '-' in ops:
        # first + or -
        i = 0
        for i in range(len(ops)):
            if ops[i] in '+-':
                break

        op = ops[i]
        num1 = nums[i]
        num2 = nums[i+1]
        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        else:
            raise ValueError(ops[i] + ' is not + or -')

        nums = nums[:i] + [res] + nums[i+2:]
        ops = ops[:i] + ops[i+1:]

    assert len(nums) == 1
    assert len(ops) == 0

    return nums[0]

if __name__ == '__main__':
    expr = '-1 + 2 - 3 * 4 * 5 / 6'
    print(eval(expr))
    print(calc(expr))
