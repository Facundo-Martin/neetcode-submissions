# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Dummy node points to the head of the list
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 2. Find the k-th node from our current position
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break  # Fewer than k nodes left; we are done!
                
            groupNext = kth.next
            
            # 3. Reverse the k-group in-place
            # We initialize 'prev' to 'groupNext' so the tail of our 
            # reversed chunk automatically links to the rest of the list.
            prev = groupNext
            curr = groupPrev.next
            
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # 4. Reconnect the reversed group back into the chain
            # 'groupPrev.next' still points to the old start (now the end) of the group.
            temp = groupPrev.next
            groupPrev.next = kth  # Point the previous group's end to the new head (kth)
            groupPrev = temp      # Move groupPrev to the end of our newly reversed group
            
        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to jump k steps ahead
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        # Output:
        # Optional[ListNode] -> Head of the reversed linked list