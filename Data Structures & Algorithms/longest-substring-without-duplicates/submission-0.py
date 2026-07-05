class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        sett=set()
        n=len(s)

        for right in range(n):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            curr_len=(right-left)+1
            max_len=max(curr_len,max_len)
            sett.add(s[right])

        return max_len



            