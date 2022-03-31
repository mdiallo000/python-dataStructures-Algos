#  Divide and conquer algorithim that splits the original array into smaller managable pieces which will then be eaily merged back together in an ordered format. Hence why this algo has a Big O (logN).

# This Algo needs a helper function that will merge two arrays into one

def merge(arrOne, arrTwo):
    result = []
    # for i, j in zip(arrOne, arrTwo):
    #     if i < j:
    #         result.append(i)
    #     else:
    #         result.append(j)

    i = 0
    j = 0
    arr1 = len(arrOne)-1
    arr2 = len(arrTwo)-1
    while j <= range(len(arrOne)-1) and i <= range(len(arrTwo)-1):
        if arrOne[j] < arrTwo[i]:
            result.append(arrOne[j])
            j += 1
        if arrOne[j] > arrTwo[i]:
            result.append(arrTwo[i])
            i += 1

    print(result)
    return result


items = [3, 5, 6, 7]
itmes2 = [1, 2, 4, 8]

# [1,2,4,7]
merge(items, itmes2)
