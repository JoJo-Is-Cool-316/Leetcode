arr = [3, 3]


def twoSum(nums, target):
    emptyDict = {}

    for index, value in enumerate(nums):
        emptyDict[index] = value

    counter = 0
    for k, v in emptyDict.items():
        if counter > 0:
            break
        difference = target - v
        if difference in emptyDict.values():
            for k2, v2 in emptyDict.items():
                if v2 == difference and k != k2:
                    print([k, k2])
                    counter += 1


twoSum(arr, 6)
