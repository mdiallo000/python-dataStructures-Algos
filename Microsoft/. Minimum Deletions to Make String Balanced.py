# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

from http.cookiejar import CookieJar


class Solution:
    def minimum_Deletions(self, s: str) -> int:
        countA = 0
        countB = 0
        balance = 0
        for char in s:
            if char == 'a':
                countA += 1
            else:
                countB += 1
            balance = max(balance, abs(countA - countB))
        return balance
    # above attempt only passed initial test case failed others

    def minimumDeletions(self, s: str) -> int:

        stack = []
        balance = 0

        for char in s:
            if stack and stack[-1] == 'b' and char == 'b':
                stack.pop()
                balance += 1
            else:
                stack.append(char)
