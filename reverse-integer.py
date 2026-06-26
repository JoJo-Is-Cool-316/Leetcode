a = 123
b = -123
c = 120


def reverse(x):
    s = str(x)
    backwards = ''
    length = len(s) - 1
    n = 0

    for i in range(length, -1, -1):
        if s[i] == '-':
            n += 1
        else:
            backwards += s[i]

    if n > 0:
        backwards = '-' + backwards
    r = int(backwards)  # r stands for reversed

    if r < -2147483648 or r > 2147483648:
        return 0
    return r


reverse(a)
reverse(b)
reverse(c)
