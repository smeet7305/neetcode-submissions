import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        n=len(nums)
        newlist=[]
        for i in range(n):
            newlist.append(heapq.heappop(nums))
        return newlist