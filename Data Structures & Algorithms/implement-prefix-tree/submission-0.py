class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = {} # symbolize end of word (if this is in a char's map, it means a word can be ended at this point)

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        if '#' in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True
        