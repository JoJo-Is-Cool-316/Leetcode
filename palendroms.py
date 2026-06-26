exampleNumber = int(input("Number: "))


def palendrome(x):
    integer = str(x)
    low = 0
    high = len(integer) - 1

    while low <= high:
        if integer[low] == integer[high]:
            low += 1
            high -= 1
        else:
            return False
    return True


print(palendrome(exampleNumber))
