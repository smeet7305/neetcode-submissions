class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2
            if target>=matrix[mid][0]:low=mid+1
            else: high=mid-1
        
        row=high

        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if target>matrix[row][mid]: low=mid+1
            elif target<matrix[row][mid]: high=mid-1
            else: return True

        return False

