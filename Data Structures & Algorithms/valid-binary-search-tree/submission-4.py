# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root):
        if not root:
            return []
        st=[]
        cur=root
        res=[]
        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left
            cur=st.pop()
            res.append(cur.val)
            cur=cur.right
        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        sort=self.inorder(root)
        for i in range(len(sort)-1):
            if sort[i]>=sort[i+1]:
                return False
        return True


        