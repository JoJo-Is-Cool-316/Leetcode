group = [1, 8, 6, 2, 5, 4, 8, 3, 7]
group2 = [1, 2]


def maxArea(height):
    areaArray = []
    low = 0
    high = len(height) - 1

    while low < high:
        length = high - low
        if height[high] < height[low]:
            area = height[high] * length
            areaArray.append(area)
            high -= 1
        elif height[low] <= height[high]:
            area = height[low] * length
            areaArray.append(area)
            low += 1

    print(max(areaArray))


maxArea(group)
maxArea(group2)


# first find the max
# then find the next heightest number and so on until you get the maxium value.
