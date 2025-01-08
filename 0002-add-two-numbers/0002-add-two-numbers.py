# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        v = (l1.val + l2.val)
        overflow = v // 10

        if overflow > 0:
            print(overflow)
            if l1.next == None:
                l1.next = ListNode(overflow, None)
            elif l2.next == None:
                l2.next = ListNode(overflow, None)
            else:
                l1.next.val = l1.next.val + overflow

        return ListNode(
            val = v % 10,
            next = self.addTwoNumbers(l1.next if l1 else 0, l2.next if l2 else 0)
        )
