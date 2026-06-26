s = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

user = input("Input a roman numerial: ")


def romanToInt(roman):
    score = 0
    for i in range(len(roman)):
        if 'I' == roman[i]:
            if 'V' == roman[i+1] or 'X' == roman[i+1]:
                score -= 2
            score += 1
            print(score)
        elif 'V' == roman[i]:
            score += 5
            print(score)
        elif 'X' == roman[i]:
            if 'L' == roman[i+1] or 'C' == roman[i+1]:
                score -= 20
            score += 10
            print(score)
        elif 'L' == roman[i]:
            score += 50
            print(score)
        elif 'C' == roman[i]:
            if 'D' == roman[i+1] or 'M' == roman[i+1]:
                score -= 200
            score += 100
            print(score)
        elif 'D' == roman[i]:
            score += 500
            print(score)
        elif 'M' == roman[i]:
            score += 1000
            print(score)
    return score


print(romanToInt(user))
