class Solution:
    def lengthOfLongestSubstring(self, s2: str) -> int:
        substrings = dict()
        max_so_far = 0
        last_reset = 0
        for i, c in enumerate(s2):
            if c in substrings:
                max_so_far = max(max_so_far, i - last_reset)
                last_reset = substrings[c] + 1
                substrings = {cc: ii+last_reset for ii, cc in enumerate(s2[last_reset:i+1])}
            else:
                substrings[c] = i
        return max(max_so_far, len(s2) - last_reset)
