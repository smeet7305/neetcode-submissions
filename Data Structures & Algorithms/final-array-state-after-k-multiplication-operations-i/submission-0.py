import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))

        while k:
            ele,freq=heapq.heappop(heap)
            ele*=multiplier
            nums[freq]=ele
            heapq.heappush(heap,(ele,freq))
            k-=1
        return nums
    
