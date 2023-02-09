from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if p == s: return [0]
        word = dict()
        substrings = dict()
        res = list()
        for c in p:
            word[c] = word.get(c, 0) + 1
        for i in range(len(s)):
            c = s[i]
            substrings[c] = substrings.get(c, 0) + 1
            if i >= len(p):
                c = s[i - len(p)]
                n = substrings.pop(c) - 1
                if n > 0: substrings[c] = n
            if word == substrings:
                res.append(i - len(p) + 1)
        return res
