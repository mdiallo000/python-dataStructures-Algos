def equal_stacks(arr1, arr2, arr3):
    h1, h2, h3 = sum(arr1), sum(arr2), sum(arr3)
    min_h = min(h1, h2, h3)

    while min_h > 0:
        while h1 > min_h:
            h1 -= arr1.pop()
        while h2 > min_h:
            h2 -= arr2.pop()


h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]
equal_stacks(h1, h2, h3)
