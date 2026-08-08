# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum(self,node,cursum,targetSum):
        if not node:
            return False
        
        cursum+=node.val
        if not node.left and not node.right:
            return cursum==targetSum
        left=self.sum(node.left,cursum,targetSum)
        right=self.sum(node.right,cursum,targetSum)
        return left or right


        




    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        cursum=0
        return self.sum(root,0,targetSum)
        

            