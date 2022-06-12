class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first we need to sort the given list to make it posssible to skip duplicates
        candidates.sort()
        res = []

        def generate(combination, idx, total):

            if total == 0:
                res.append(combination[:])
            #  if our total somehow goes pass zero that means we have overshot the target and need to cease pursing this path
            if total <= 0:
                return
