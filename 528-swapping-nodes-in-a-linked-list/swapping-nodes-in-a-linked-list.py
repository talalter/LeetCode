# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(k-1):
            first = first.next
        slow = head
        fast = first
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        first.val, slow.val = slow.val, first.val
        return head
        

        