class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        low=0
        high=rows*cols-1

        while low<=high:
            mid=low+(high-low)//2
            r=mid//cols
            c=mid%cols

            if target==matrix[r][c]:
                return True
            elif target<matrix[r][c]:
                high=mid-1
            else:
                low=mid+1
        return False


