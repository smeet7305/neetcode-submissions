# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self,p,q):
        if not p and not q:return True
        elif not p or not q: return False
        elif p.val==q.val and self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right): return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:return False
        elif self.sameTree(root,subRoot):return True
        elif self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):return True
        else: return False
        