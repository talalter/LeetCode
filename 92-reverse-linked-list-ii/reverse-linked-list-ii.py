# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Dummy node to handle edge cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Traverse to the node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # `prev` is the node before the start of the reversal segment
        # `current` is the first node in the segment to be reversed
        start = prev.next
        then = start.next

        # Step 2: Reverse the sublist
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next