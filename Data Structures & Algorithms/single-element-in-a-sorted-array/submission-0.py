from collections import defaultdict
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count=defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]]+=1
        
        for i in count:
            if count[i]==1:
                return i
        