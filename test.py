# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        seen = []
        while head:
            if head in seen:
                return True
            seen.append(head)
            head = head.next

        return False

            
        
        

        return 

head = [3,2,0,-4]