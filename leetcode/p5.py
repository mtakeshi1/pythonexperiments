class Solution:

    @staticmethod
    def is_palindrome(s, f, to, memo) -> bool:
        if f >= to:
            return True
        key = (f, to)
        if key in memo:
            return memo[key]
        rec_pal = False
        if s[f] == s[to]:
            rec_pal = Solution.is_palindrome(s, f+1, to-1, memo)
        memo[key] = rec_pal
        return rec_pal

    def longestPalindrome(self, s: str) -> str:
        memo = dict()
        max_found = -1
        max_substring = ""
        for i in range(len(s)):
            j = len(s)-1
            while j >= i:
                if Solution.is_palindrome(s, i, j, memo):
                    if max_found < j-i:
                        max_substring = s[i:j+1]
                        max_found = max(max_found, j - i)
                    break
                j -= 1
        return max_substring
