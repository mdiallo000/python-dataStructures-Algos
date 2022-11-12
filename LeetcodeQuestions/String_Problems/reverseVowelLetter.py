class Solution:
    def reverseVowels(s):
        letters = ['a', 'e', 'i', 'o', 'u']
        vowels = set(letters)
        s = [c for c in s]
        l, r = 0, len(s)-1

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            while s[l] not in vowels:
                l += 1
            while s[r] not in vowels:
