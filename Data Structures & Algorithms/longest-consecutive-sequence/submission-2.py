class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count=1
        maxi=1

        for i in range(len(nums)-1):
            if(nums[i+1]==nums[i]):
                continue
            
            elif(nums[i+1]==1+nums[i]):
                count+=1
            
            else:
                count=1
        
            maxi=max(maxi,count)


        return maxi
        
