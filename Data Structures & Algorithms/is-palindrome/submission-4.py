class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = s.replace(" ", "")
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.replace("'", "")
        s=s.replace(".","")
            
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            
            left=left+1
            right=right-1

    
        return True

        