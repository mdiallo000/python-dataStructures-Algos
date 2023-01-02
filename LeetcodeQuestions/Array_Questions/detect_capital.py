class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        #  our goal is detect whether the usage of the capital letters is done correctly
        #  for it to be correct all letters are capitalized or only the first letter is capitalize
        #  what i am think is to have some counter that will check, the count should either equal one or equal to the length of the string
        #  for example "ABC" => count = 3 or "Magic" -> count = 1 return True
        #  if we have this case "BestPlayer" count != 1 or the length of string return False

        count = 0
        if len(word) == 1:
            return True
        for i in range(len(word)):
            if word[i].isupper():
                count += 1
        print(count)
        if count == len(word):
            return True
        elif count == 1 and word[0].isupper():
            return True
        elif count == 0:
            return True
        return False
