class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        available = {}
        for c in s:
            if c in available:
                available[c] = available[c] + 1
            else:
                available[c] = 1
        
        i = 0
        while i < len(t):
            c = t[i]
            if c not in available:
                return False
            available[c] = available[c] - 1
            if available[c] == 0:
                del available[c]
            i += 1
            
        return True