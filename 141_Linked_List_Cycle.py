# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        # Initialize two pointers, "slow" and "fast"
        slow = head
        fast = head

        # Loop until either of the pointers reach the end of the list
        while fast and fast.next:
            # Move the "slow" pointer one node forward
            slow = slow.next

            # Move the "fast" pointer two nodes forward
            fast = fast.next.next

            # If the pointers meet, there is a cycle
            if slow == fast:
                return True

        # If the loop completed and the pointers never met, there is no cycle
        return False