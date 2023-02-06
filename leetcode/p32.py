class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = []
        found = [0] * len(s)

        for i, c in enumerate(s):
            if c == ')':
                if queue == [] or s[queue[-1]] != '(':
                    queue = []
                else:
                    prev = queue.pop()
                    found[prev] = 1
                    found[i] = 1
            elif c == '(':
                queue.append(i)

        global_max = 0
        local_max = 0
        for v in found:
            local_max += v
            global_max = max(local_max, global_max)
            if not v:
                local_max = 0
        return global_max
