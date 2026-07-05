class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        l=0
        r=0
        n=len(nums)
        ans=float('inf')
        while r<n:
            sum+=nums[r]

            while sum>=target:
                ans=min(ans,r-l+1)
                sum-=nums[l]
                l+=1
            r+=1
        return 0 if ans == float('inf') else ans
            
                
                

        