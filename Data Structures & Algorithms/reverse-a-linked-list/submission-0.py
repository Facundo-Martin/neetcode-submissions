# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # traverse all the nodes of Linked List
        while curr:
            # store next before replacing it
            next_node = curr.next

            # reverse current node's next pointer
            curr.next = prev
        
            # move pointers one position ahead
            prev = curr
            curr = next_node

        return prev
