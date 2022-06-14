class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(str, l, r):
            while l < r:
                if str[l] != str[r]:
                    return False
                l += 1
                r -= 1
            return True

        def generate(idx, partition):
            if idx == len(s):
                res.append(partition[:])
                return

            for j in range(idx, len):
                if isPalindrome(s, idx, j):
                    partition.append(s[idx:j+1])
                    generate(j, partition)
                    partition.pop()

        generate(0, [])
        return res
