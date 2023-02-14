class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxi = max(len(a), len(b))
        sum_bin = ''
        carry = 0
        for i in range(maxi):
            c = carry
            carry = 0
            if i < len(a) and a[-i-1] == '1':
                c += 1
            if i < len(b) and b[-i-1] == '1':
                c += 1
            if c >= 2:
                carry = 1
                c -= 2
            sum_bin = str(c) + sum_bin
        if carry == 1:
            sum_bin = '1' + sum_bin
        return sum_bin
