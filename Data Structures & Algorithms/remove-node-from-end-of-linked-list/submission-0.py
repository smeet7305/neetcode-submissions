# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        p=count-n

        if p==0:
            return head.next

        #now I wanna remove pth node from the start
        curr=head
        prev=None
        i=0
        while curr:
            if i==p-1:
                curr.next=curr.next.next
                break
                
            curr=curr.next
            i+=1

        return head


        

        