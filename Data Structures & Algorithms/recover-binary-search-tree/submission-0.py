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
        cur=root
        st=[]
        res=[]
        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left
            cur=st.pop()
            res.append(cur)
            cur=cur.right
        return res

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        
        nodes=self.inorder(root)

        vals=[]
        for i in nodes:
            vals.append(i.val)

        sorted_vals=sorted(vals)

        wrong = []

        for i in range(len(nodes)):
            if nodes[i].val != sorted_vals[i]:
                wrong.append(nodes[i])
        
        wrong[0].val, wrong[1].val = wrong[1].val, wrong[0].val

        





        