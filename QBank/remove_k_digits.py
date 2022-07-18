from re import S


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for n in num:
