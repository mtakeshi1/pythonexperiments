from typing import Optional


class Solution:
    # expression ::= factor | expression + factor | expression - factor | - expression
    # factor     ::= number | ( expression ) | - factor
    input = ''
    pos = 0
    numbers = set('0123456789')

    def trim(self):
        while self.pos < len(self.input) and self.input[self.pos] == ' ':
            self.pos += 1

    def peek(self) -> Optional[str]:
        self.trim()
        if self.pos >= len(self.input):
            return None
        return self.input[self.pos]

    def eof(self):
        return self.peek() is None

    def advance(self) -> Optional[str]:
        if self.eof():
            return None
        c = self.input[self.pos]
        self.pos += 1
        return c

    def parse_exp(self) -> int:
        lhs = self.parse_factor()
        if self.eof():
            return lhs
        while True:
            op = self.peek()
            if op == '+':
                self.advance()
                lhs += self.parse_factor()
            elif op == '-':
                self.advance()
                lhs -= self.parse_factor()
            else:
                break
        return lhs

    def parse_num(self) -> int:
        a = 0
        while self.peek() in self.numbers:
            a = 10 * a + ord(self.advance()) - ord('0')
        return a

    def parse_factor(self) -> Optional[int]:
        if self.peek() in self.numbers:
            return self.parse_num()
        elif self.peek() == '(':
            self.advance()
            v = self.parse_exp()
            if v is None:
                return None
            n = self.advance()
            if n != ')':
                raise Exception("exptected ')' but was: " + str(n))
            return v
        elif self.peek() == '-':
            self.advance()
            return -self.parse_factor()
        else:
            return None

    def calculate(self, s: str) -> int:
        self.input = s
        return self.parse_exp()
