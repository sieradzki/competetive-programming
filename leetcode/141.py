# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        visited = []
        while head.next:
            visited.append(head)
            head = head.next
            if head in visited:
                return True

        return False
       