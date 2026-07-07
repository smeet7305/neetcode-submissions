# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self,root):
            if not root:
                return []
            ans=[]
            q=deque([root])

            while q:
                node=q.popleft()
                if node:
                    ans.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    ans.append(None)
            
            while ans and ans[-1] is None: ans.pop()
            return ans
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.serialize(p)==self.serialize(q):return True
        else: return False
        