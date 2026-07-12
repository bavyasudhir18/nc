class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==0:
            return 0
        if len(tokens)==1:
            return int(tokens[0])
        stack=[]
        for i in tokens:
            if i=='+' or i=='-' or i=='*' or i=='/':
                a=int(stack.pop())
                b=int(stack.pop())
                if i=='+':
                    res=a+b
                elif i=='-':
                    res=b-a
                elif i=='*':
                    res=a*b
                elif i=='/':
                    res=b/a
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[0])       