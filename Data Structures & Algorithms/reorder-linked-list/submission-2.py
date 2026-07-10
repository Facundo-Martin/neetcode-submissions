# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the midle of our linked list (slow pointer)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Grab pointer of the second half and split list
        second_half_pointer = slow.next
        slow.next = None


        # Reverse the second half
        prev = None
        curr = second_half_pointer
        while curr:
            next_node = curr.next  # Save the rest of the list
            curr.next = prev       # Flip the pointer backwards
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward

        # Merge two halves
        # 'prev' is now the head of the reversed second half
        first, second = head, prev

        # Merge two halves
        while second:
            # Save the next steps for both lists
            tmp1, tmp2 = first.next, second.next
            
            # Rewire the connections
            first.next = second
            second.next = tmp1
            
            # Move our pointers forward
            first = tmp1
            second = tmp2
        
        # Input: LinkedList ??

        # Edge cases:
        # 1. 1 <= Length of the list <= 1000 -> If len == 1 then no need to reorder

        # Output: None!