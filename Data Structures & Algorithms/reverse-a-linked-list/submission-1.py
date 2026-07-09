# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next     # 1. Save the next node in the original list
            curr.next = prev    # 2. Reverse the arrow to point backwards
            prev = curr         # 3. Shift 'prev' one step forward
            curr = nxt          # 4. Shift 'curr' one step forward

        return prev             # 'prev' ends up on the last node, which is the new head