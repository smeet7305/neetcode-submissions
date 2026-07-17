import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        n=len(stones)
        for i in range(n):
            stones[i]=-stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            max1=-heapq.heappop(stones)
            max2=-heapq.heappop(stones)
            if max1==max2:
                continue
            if max1>max2:
                heapq.heappush(stones,-(max1-max2))
            #max2>max1 can never happen
        return -stones[0] if stones else 0
        
        