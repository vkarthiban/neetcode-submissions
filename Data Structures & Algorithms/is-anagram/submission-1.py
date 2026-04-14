class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for ch in set(list(s)):
            if s.count(ch) != t.count(ch):
                return False
        return True