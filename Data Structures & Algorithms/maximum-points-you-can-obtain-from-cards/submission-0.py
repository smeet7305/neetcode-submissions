class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        l=0
        cur_sum=0
        min_sum=float("inf")

        if(n==0): return 0
        if k == n: return sum(cardPoints)

        for r in range(len(cardPoints)):
            cur_sum+=cardPoints[r]



            if(r-l+1==n-k):
                min_sum=min(min_sum,cur_sum)

                cur_sum-=cardPoints[l]
                l+=1
        
        return sum(cardPoints)-min_sum

            
        