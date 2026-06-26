array = [5, 7, 7, 8, 8, 10]
n = 8


def searchRange(nums, target):
    mapNums = {}
    finalArray = []
    low = 0
    high = len(finalArray) - 1
    for i, v in enumerate(nums):
        mapNums[i] = v

    for k, v in mapNums.items():
        if v == target:
            finalArray.append(k)
    try:
        finalArray = [finalArray[low], finalArray[high]]
    except IndexError:
        pass

    if len(finalArray) == 0:
        finalArray = [-1, -1]
    elif len(finalArray) == 1:
        finalArray.append(finalArray[0])
    print(finalArray)


searchRange(array, n)
