a = 10
b = 3
c = 7
d = -3


def divide(dividend, divisor):
    quotient = int(dividend/divisor)
    if quotient > 2147483647:
        return 2147483647
    return quotient


print(divide(a, b))
print(divide(c, d))
