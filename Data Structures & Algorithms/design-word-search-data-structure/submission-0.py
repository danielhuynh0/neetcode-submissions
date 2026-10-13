class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = {}

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return ('#' in cur)

            c = word[i]
            if c == '.':
                for child in cur.values():
                    result = dfs(i+1, child)
                    if result:
                        return result
                return False
            else:
                if c not in cur:
                    return False
                cur = cur[c]
                return dfs(i+1, cur)
        return dfs(0, self.trie)
