class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            
        while k:
            ele,idx=heapq.heappop(heap)
            k-=1
        return -ele
