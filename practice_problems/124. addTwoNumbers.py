# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = end = ListNode()
        addends = l1, l2
        carry = 0
        while addends or carry:
            carry += sum([a.val for a in addends])
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry //= 10
        return dummy.next

