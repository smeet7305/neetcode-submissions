class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        l=0
        r=len(arr)-1
        while(l<=r):
            m=(l+r)//2

            if (arr[m]==target):
                return True
            
            if arr[l] == arr[m] == arr[r]:
                l += 1
                r -= 1
            
            elif(arr[m]<=arr[r]):
                if( arr[m]<target<=arr[r]):
                    l=m+1
                else:
                    r=m-1
            else:
                if(arr[l]<=target<arr[m]):
                    r=m-1
                
                else:
                    l=m+1
        
        return False