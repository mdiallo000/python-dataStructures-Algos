class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first we need to sort the given list to make it posssible to skip duplicates
        candidates.sort()
