

def FailIfTotalIsGreaterThanAllElements(values, key):
    total = 0
    for number in values:
        total += number

    return total < key     

def FindConsecutiveListSum(values, key, startingIndex):
    index = startingIndex
    sum = 0

    while (index < len(values)):
        sum += values[index]

        if (sum == key):
            # StartingIndex = startingIndex
            # EndingIndex = index
            return [startingIndex, index]
        
        elif (sum > key):
            nextStartingIndex = startingIndex + 1
            return FindConsecutiveListSum(values, key, nextStartingIndex)
                            

        index += 1
    
    return [-1, -1]


def solution(l, t):
    if (FailIfTotalIsGreaterThanAllElements(l, t)):
       return [-1, -1]
    
    return FindConsecutiveListSum(l, t, 0)

    


#result = solution([1, 2, 3, 4], 15)  #[-1, -1]
#result = solution([4, 3, 10, 2, 8], 12) #[2, 3]
#result = solution([4, 4, 4, 4], 13)  #[-1, -1]
#result = solution([8, 40, 9, 2, 20, 20, 20, 2, 4, 4, 10], 68)  #[3, 8]
#result = solution([8, 40, 9, 2, 20, 20, 20, 2, 4, 4, 10], 44)  #[-1, -1]
result = solution([8, 40, 9, 2, 20, 20, 20, 2, 4, 4, 10], 40)  #[1, 1]

print(result)
