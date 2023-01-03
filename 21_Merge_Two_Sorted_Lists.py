class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

list1 = [1,2,4]
list2 = [1,3,4]
print(Solution().mergeTwoLists(list1,list2))