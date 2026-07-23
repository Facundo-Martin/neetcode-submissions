# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []  

        # pushing the values of the first linked list
        while list1:
            arr.append(list1.data)
            list1 = list1.next

        # pushing the values of the second linked list
        while list2:
            arr.append(list2.data)
            list2 = list2.next

        # sorting the list
        arr.sort()

        # creating a new list with sorted values
        dummy = Node(-1)
        curr = dummy

        for value in arr:
            curr.next = Node(value)
            curr = curr.next

        return dummy.next 