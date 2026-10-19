# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the midpoint
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow

        # 2. Reverse the second half
        prev = None
        curr = mid.next

        mid.next = None  # Split the list

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 3. Weave the two halves
        start = head
        start2 = prev

        while start2:
            next1 = start.next
            next2 = start2.next

            start.next = start2
            start2.next = next1

            start = next1
            start2 = next2
        