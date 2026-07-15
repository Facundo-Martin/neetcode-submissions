# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Extract all values from the linked list into a Python list
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        n = len(values)
        
        # Step 2: Reverse the values in chunks of size k
        # We loop from 0 to n, stepping by k
        for i in range(0, n, k):
            # Only reverse if we have a full group of size k remaining
            if i + k <= n:
                # Python slice assignment makes reversing in-place incredibly clean
                values[i : i + k] = reversed(values[i : i + k])
                
        # Step 3: Reconstruct the linked list using the modified values
        # We can reuse the existing node structures to save memory overhead
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next
            
        return head

        # Output:
        # Optional[ListNode] -> Head of the reversed linked list