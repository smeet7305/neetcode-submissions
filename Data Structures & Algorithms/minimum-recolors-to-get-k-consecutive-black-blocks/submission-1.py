class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites=blocks[:k].count('W')
        ans=whites

        for r in range(k,len(blocks)):
            if blocks[r] is 'W':
                whites+=1
            if blocks[r-k] is 'W':
                whites-=1
            
            ans=min(whites,ans)
        return ans
         