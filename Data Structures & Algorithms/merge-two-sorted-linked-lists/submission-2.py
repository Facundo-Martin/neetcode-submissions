class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base Cases: If either list is empty, return the other
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive Step: Point the smaller node to the result of merging the rest
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2