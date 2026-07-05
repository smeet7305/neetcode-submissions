class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        length=0
        maxlen=0
        zero=0
        for r in range(len(nums)):
            zero=nums[l:r+1].count(0)
            while zero>k:
                l+=1
                zero=nums[l:r+1].count(0)
            length=r-l+1
            maxlen=max(length,maxlen)
        return maxlen