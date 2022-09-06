class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #  we get a list of words our goal is to create a single word from the list of words in a way that it can be then decode into the original list. The only way this can happen is if we use a delimiter in between the words so that we can differentiate them
        # edge cases:
        #  we can't just use any delimiter since it is possible that the character we choose to be the delimiter can also be presented in the original word, this of course can create a problem
        # exammple: ['neet', 'code']
        res = ""

        for wrd in strs:
            res += str(len(wrd)) + "#" + wrd
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # the decode method is meant to accept the string that was encoded and its goal is to return the original list of words that was used to create the string
        res, i = [], 0
        while i < len(s):
            j = 0
