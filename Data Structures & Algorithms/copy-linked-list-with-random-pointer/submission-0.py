"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        thead = Node(0)
        tp = thead
        nodes = {None : None}
        while p != None:
            tp.next = Node(p.val)
            tp = tp.next
            nodes[p] = tp
            p = p.next

        p = head
        tp = thead.next
        while p != None:
            tp.random = nodes[p.random]
            tp = tp.next
            p = p.next
        return thead.next
            
            

        