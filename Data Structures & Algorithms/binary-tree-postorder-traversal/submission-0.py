# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        res=[]
        cur=root
        while cur or st:
            while cur:
                res.append(cur.val)
                st.append(cur)
                cur=cur.right
            cur=st.pop()
            cur=cur.left
        
        return res[::-1]
