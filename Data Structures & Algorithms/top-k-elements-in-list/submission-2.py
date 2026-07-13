import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]
        ans=[]
        for key,val in count.items():
            heapq.heappush(heap,(-val,key))

        for i in range(k):
            freq,num=heapq.heappop(heap)
            ans.append(num)
        return ans