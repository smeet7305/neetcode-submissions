class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for m in range(k+1,len(nums)):
                        if target==nums[i]+nums[j]+nums[k]+nums[m]:
                            res.add((nums[i],nums[j],nums[k],nums[m]))
        
        return list(res)