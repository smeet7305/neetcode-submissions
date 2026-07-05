class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        max_len=0
        l=0
        seen=set()

        for r in range(len(s)):
            length=r-l+1

            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                length=r-l+1
            seen.add(s[r])
            max_len=max(max_len,length)
        
        return max_len
        
        