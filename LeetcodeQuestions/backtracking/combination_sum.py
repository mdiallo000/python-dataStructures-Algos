class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solving these problems will follow a similar behavior like finding the subsets of a range of numbers
        res = []

        def finSum(idx, seqs, total):

            # establish base case
            if idx >= len(candidates):
                if total == target:
                    res.append(seqs.copy())
                return

            seqs.append(candidates[idx])
