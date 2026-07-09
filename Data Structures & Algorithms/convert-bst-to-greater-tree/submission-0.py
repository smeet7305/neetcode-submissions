# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        st=[]
        res=[]
        cur=root
        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left
            cur=st.pop()
            res.append(cur)
            cur=cur.right
        
        running = 0
        for i in range(len(res) - 1, -1, -1):
            running += res[i].val
            res[i].val = running
        return root
