# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0

        curr = dummy
        while l1 or l2 or carry:
            # Grab list's values
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            
            # Perform addittion
            sum = n1 + n2 + carry
            carry = sum // 10
            val = sum % 10

            # Create new node with value
            curr.next = ListNode(val)

            # Update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return curr.next


