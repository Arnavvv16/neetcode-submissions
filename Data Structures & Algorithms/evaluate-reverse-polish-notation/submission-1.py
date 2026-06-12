class Solution:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def evalRPN(self, tokens: List[str]) -> int:
        
        for token in tokens:
            if (token !='+') and (token !='/') and (token !='-') and (token !='*'):
                self.stack.append(int(token))
            else:
                second=int(self.stack.pop())
                first=int(self.stack.pop())
                if (token =='+'):
                    self.stack.append(first+second)
                if (token =='-'):
                    self.stack.append(first-second)
                if (token =='*'):
                    self.stack.append(first*second)
                if (token =='/'):
                    self.stack.append(int(first/second))
        return int(self.stack.pop())