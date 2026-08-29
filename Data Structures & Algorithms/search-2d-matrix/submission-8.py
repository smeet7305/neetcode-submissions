class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        l=0
        r=len(matrix)-1
        while l<=r:
            mid=l+(r-l)//2
            if target<matrix[mid][0]:
                r=mid-1
            else:
                l=mid+1
        
        row=r
        low=0
        high=cols-1

        while low<=high:
            mid=low+(high-low)//2
            if target==matrix[row][mid]: return True
            elif target<matrix[row][mid]:
                high=mid-1
            else:
                low=mid+1

        return False
            


            
        

        
        
