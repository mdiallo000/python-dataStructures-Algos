class Solution:
    def findUnion(self, arr1, arr2):
        # Problem Statement: Given two sorted arrays, arr1 and arr2 of size n and m. Find the union of two sorted arrays.
        set1 = set(arr1)
        set2 = set(arr2)
        arr = []

        for n in set1:
            arr.append(n)
        for n in set2:
            arr.append(n)
        return arr
