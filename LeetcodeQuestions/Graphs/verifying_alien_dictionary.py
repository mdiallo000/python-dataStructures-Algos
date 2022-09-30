class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordDict = {c: i for c, i in enumerate(order)}
