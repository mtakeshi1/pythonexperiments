# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        r = [self.val]
        if self.next is not None:
            r = r + self.next.to_list()
        return r

    @staticmethod
    def from_list(li: List[int]):
        if li:
            el = ListNode(li.pop(0))
            el.next = ListNode.from_list(li)
            return el
        return None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """add two numbers as linked list, starting with the least significant digits, without leading zeroes"""
        carry = 0
        root = None
        current = None
        while l1 is not None or l2 is not None:
            num = carry
            carry = 0
            if l1:
                num += l1.val
                l1 = l1.next

            if l2:
                num += l2.val
                l2 = l2.next

            if num > 9:
                num -= 10
                carry += 1

            el = ListNode(val=num)

            if root is None:
                root = el

            if current is None:
                current = el
            else:
                current.next = el
                current = el

        if carry > 0:
            current.next = ListNode(carry)

        return root


if __name__ == '__main__':
    print(ListNode.from_list([1, 2]).to_list())
