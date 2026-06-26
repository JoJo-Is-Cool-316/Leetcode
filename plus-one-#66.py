array = [9, 9]


def plusOne(digits):
    n = int(''.join(map(str, digits)))
    n += 1
    digits = list(map(int, str(n)))
    print(digits)  # IN LEETCODE, THIS IS RETURN


plusOne(array)
