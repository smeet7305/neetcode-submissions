class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low=1
        high=max(piles)
        ans=high

        while low<=high:
            mid=low+(high-low)//2

            time=0
            for i in piles:
                time+=math.ceil(i/mid)
            
            if time<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans





        