class Solution:
    def minDeletions(self, s: str) -> int:
        count = [] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        deletions = 0
        frequency_count = set()
        for i in range(len(count)):

            while count[i] and count[i] in frequency_count:
                deletions += 1
                count[i] -= 1

            frequency_count.add(count[i])
