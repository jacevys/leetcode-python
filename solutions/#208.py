class Trie:
    def __init__(self):
        self.links = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        current = self

        for w in word:
            if w not in current.links:
                new_obj = Trie()
                current.links[w] = new_obj
                current = current.links[w]
            else:
                current = current.links[w]

        current.is_end = True

    def search(self, word: str) -> bool:
        current = self

        for w in word:
            if w not in current.links:
                return False
            else:
                current = current.links[w]

        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self

        for w in prefix:
            if w not in current.links:
                return False
            else:
                current = current.links[w]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
2023.08.07
1.failed
'''