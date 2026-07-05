class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for curr in tokens:
            if curr not in "+-*/":
                st.append(int(curr))
            
            elif curr=="+":
                a=st.pop()
                b=st.pop()
                st.append(a+b)
            
            elif curr=="-":
                a=st.pop()
                b=st.pop()
                st.append(b-a)
            elif curr=="*":
                a=st.pop()
                b=st.pop()
                st.append(b * a)
            elif curr=="/":
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))

        return st[-1]
