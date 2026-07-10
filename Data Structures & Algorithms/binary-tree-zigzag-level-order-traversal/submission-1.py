# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=deque([root])
        level=1
        res=[]
        while q:
            cur=[]
            size=len(q)
            for i in range(size):
                node=q.popleft()
                cur.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level%2==0:
                    cur.reverse()


                
                       
            level+=1
            res.append(cur)

        return res


        