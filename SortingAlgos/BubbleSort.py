

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


nums = [1, 8, 64, 12, 47, 56, 45, 10, 78, 54, 3]


def fib(num):
    if num <= 2:
        return num
    return fib(num - 1) + fib(num-2)


print(fib(2))
