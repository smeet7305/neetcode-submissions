# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        ans=ListNode()
        curr=ans
        carry=0
        while curr1 or curr2:
            curr.next=ListNode()
            curr=curr.next
            
            if curr1:
                val1=curr1.val 
            else: val1=0
            if curr2:
                val2=curr2.val
            else: val2=0
            curr.val=(val1+val2+carry)%10
            carry=(val1+val2+carry)//10
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next

        if carry:
            carry1=ListNode()
            carry1.val=carry
            curr.next=carry1
        
        return ans.next