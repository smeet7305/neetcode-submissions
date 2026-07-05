class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=k-1
        n=len(arr)
        count=0
        window_sum=sum(arr[l:r+1])
        
        while r<n-1:
            if window_sum>=k*threshold:
                count=count+1
            
            window_sum=window_sum-arr[l]
            l=l+1
            r=r+1
            window_sum=window_sum+arr[r]

        if r==n-1:
            window_sum=window_sum+arr[r]-arr[l]
            if window_sum>=k*threshold:
                count=count+1


        return count



            
            
