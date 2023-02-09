class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = []
        max_len = 0
        len_so_far = 0
        for c in s:
            if c == ')':
                if queue == [] or queue[-1] != '(':
                    max_len = max(max_len, len_so_far)
                    queue = []
                    len_so_far = 0
                else:
                    queue.pop()
                    len_so_far += 2
            elif c == '(':
                queue.append(c)
        return max(max_len, len_so_far)
