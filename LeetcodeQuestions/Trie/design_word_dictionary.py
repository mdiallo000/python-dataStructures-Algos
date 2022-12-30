class Trie_Node:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = Trie_Node()

    def addWord(self, word: str) -> None:
        #  we need to add a word in the dictionary
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie_Node()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        #  this method allows us to establish whether a word exists or not in our dictionary
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word
