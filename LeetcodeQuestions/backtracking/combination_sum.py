class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solving these problems will follow a similar behavior like finding the subsets of a range of numbers
        res = []

        def findSum(idx, seqs, total):

            # establish base case
            if idx >= len(candidates) or total > target:
                if total == target:
                    res.append(seqs.copy())
                    return
                return

            seqs.append(candidates[idx])
            findSum(idx, seqs, total + candidates[idx])
            seqs.pop()
            findSum(idx+1, seqs, total)

        findSum(0, [], 0)
        return res
