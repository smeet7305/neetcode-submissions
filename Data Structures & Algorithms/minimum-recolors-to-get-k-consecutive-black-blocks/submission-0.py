class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        r=k-1
        n=len(blocks)
        min_w=float('inf')
        while r<n:
            no=blocks[l:r+1].count('W')
            min_w=min(min_w,no)
            
            l=l+1
            r=r+1
        return min_w