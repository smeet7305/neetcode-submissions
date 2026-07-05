# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prev=None

        if head is None:
            return None

        while current.next!= None:
            succ=current.next
            current.next=prev
            prev=current
            current=succ
        
        current.next=prev
        head=current

        return head

            
        