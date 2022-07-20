class TrieNode:

    def __init__(self):
        self.children = {}
        self.endWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endWord = True

    def search(self, word: str) -> bool:

    def startsWith(self, prefix: str) -> bool:
