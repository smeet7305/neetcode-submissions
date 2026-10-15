class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)    
        longest=0

        for num in numset:
            if num-1 not in numset:
                incr_fact=1

                while(num+incr_fact) in numset:
                    incr_fact+=1
                
                longest=max(longest,incr_fact)
        
        return longest