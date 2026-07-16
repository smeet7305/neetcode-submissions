# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,node):
        if not node:
            return []

        cur=node
        st=[]
        res=[]
        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left
            cur=st.pop()
            res.append(cur.val)
            cur=cur.right
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None
        
        res=self.inorder(root)
        return res[k-1]




