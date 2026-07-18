class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        for i in range(len(gifts)):
            heapq.heappush(heap,-gifts[i])
        
        while k:
            max=heapq.heappop(heap)
            heapq.heappush(heap,-floor(sqrt(abs(max))))
            k-=1
        
        ans=0
        for i in range(len(heap)):
            ans=ans-heap[i]
        return ans

