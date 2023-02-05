class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        word = dict()
        substrings = dict()
        for c in s1:
            word[c] = word.get(c, 0) + 1
        for i in range(len(s2)):
            c = s2[i]
            substrings[c] = substrings.get(c, 0) + 1
            if i >= len(s1):
                c = s2[i - len(s1)]
                n = substrings.pop(c) - 1
                if n > 0:
                    substrings[c] = n
            if word == substrings:
                return True

        return False
