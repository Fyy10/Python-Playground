class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.get(c) is None:
                curr[c] = dict()
            curr = curr[c]
        curr['*'] = 0

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if curr.get(c) is None:
                return False
            curr = curr[c]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if curr.get(c) is None:
                return False
            curr = curr[c]
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    print(t.search('apple'))    # True
    print(t.search('app'))      # False
    print(t.startsWith('app'))  # True
    t.insert('app')
    print(t.search('app'))      # True
