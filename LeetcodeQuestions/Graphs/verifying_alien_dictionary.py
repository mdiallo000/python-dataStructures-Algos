class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordDict = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            wrd1, wrd2 = words[i], words[i+1]
            for j in range(len(wrd1)):
                if j == len(wrd2):
                    return False
                if wrd1[j] != wrd2[j]:
                    if ordDict[wrd2[j]] < ordDict[wrd1[j]]:
                        return False
                    break
        return True
