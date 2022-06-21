class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first we need to sort the given list to make it posssible to skip duplicates
        candidates.sort()
        res = []

        def generate(combination, idx, target):

            if target == 0:
                res.append(combination[:])
            #  if our total somehow goes pass zero that means we have overshot the target and need to cease pursing this path
            if target <= 0:
                return
            prev = -1
            for i in range(idx, len(candidates)):
                #  here we make sure we arent process a duplicate, if it is a duplicate than we move pass this value
                if candidates[i] == prev:
                    continue
                combination.append(candidates[i])
                generate(combination, i + 1, target - candidates[i])
                combination.pop()
                prev = candidates[i]
                
        generate([],0,target)
        return res 