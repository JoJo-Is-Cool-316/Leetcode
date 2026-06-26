import bisect

array1 = [4, 5, 6, 7, 0, 1, 2]
a = 0
b = 3

array2 = [1]
c = 0


def search(nums, target):  # returning an int
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1


print(search(array1, a))
print(search(array1, b))
print(search(array2, c))
