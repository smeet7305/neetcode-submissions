class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={')':'(' , '}':'{', ']':'['}
        for ch in s:
            if ch not in mapping:
                st.append(ch)
            else:
                if not st or st[-1] != mapping[ch]:
                    return False
                st.pop()
        return not st
                
      