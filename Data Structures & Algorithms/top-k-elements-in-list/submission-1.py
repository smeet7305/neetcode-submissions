class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        desc=sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans=[]
        for i in range(k):
            ans.append(desc[i][0])
        return ans