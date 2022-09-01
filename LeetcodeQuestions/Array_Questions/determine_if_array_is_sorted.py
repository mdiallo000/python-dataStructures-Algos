class Solution:
    def check(self, nums: List[int]) -> bool:
        # Determine wheter or not the array is sorted even after being rotated
        # The approach i took was to use pointers and partion the list in different havves and determine whether the sorting is consistent
