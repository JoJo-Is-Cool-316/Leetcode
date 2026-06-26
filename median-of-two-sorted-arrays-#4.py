# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


list_1 = [2, 2, 4, 4]
list_2 = [2, 2, 2, 4, 4,]


def findMedianSortedArrays(nums1, nums2):
    nums3 = nums1 + nums2
    sortedArray = sorted(nums3)

    print(len(sortedArray))
    if len(sortedArray) % 2 == 0:
        middle = len(sortedArray) // 2
        middleNumbers = [sortedArray[middle-1], sortedArray[middle]]
        average = (middleNumbers[0] + middleNumbers[1]) / 2

        return average

    else:
        middle = (len(sortedArray) - 1) // 2
        return sortedArray[middle]


answer = findMedianSortedArrays(list_1, list_2)
print(answer)
