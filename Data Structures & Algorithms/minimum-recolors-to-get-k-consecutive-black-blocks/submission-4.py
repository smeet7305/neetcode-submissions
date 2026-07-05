class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites=blocks[:k].count('W')
        ans=whites
        l=0
        r=k-1
        n=len(blocks)
        while r<n:
            whites=blocks[l:r+1].count('W')
            if whites<ans:ans=whites
            r+=1
            l+=1
        return ans




            
