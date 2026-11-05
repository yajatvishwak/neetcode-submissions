# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        for _ in range(n):
            r = r.next
        t = head
        if r is None:
            return head.next
        while  r.next != None:
            r = r.next
            t = t.next
        t.next = t.next.next
        return head
        