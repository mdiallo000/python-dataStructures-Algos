class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #  we get a list of words our goal is to create a single word from the list of words in a way that it can be then decode into the original list. The only way this can happen is if we use a delimiter in between the words so that we can differentiate them
        # edge cases:
        #  we can't just use any delimiter since it is possible that the character we choose to be the delimiter can also be presented in the original word, this of course can create a problem. However we store information about the lenght of the word with the word then reconstructing it back will be much easier
        # exammple: ['neet', 'code']
        res = ""

        for wrd in strs:
            res += str(len(wrd)) + "#" + wrd
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # the decode method is meant to accept the string that was encoded and its goal is to return the original list of words that was used to create the string.
        res, i = [], 0
        while i < len(s):
            #  j will always start where i is. j will be our guide, it will move up to when it sees the first "#" character, thats how we know where to begin remaking the original word
            j = i
            while s[j] != '#':
                j += 1

            # "4#neet4#code"
            #  i
            #   j
            length = int(s[i:j])
            #  we get the length by looking at where
            res.append(s[j+1: j+1 + length])
            i = j + 1 + length
        return res
