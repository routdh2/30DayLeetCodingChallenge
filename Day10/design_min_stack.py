'''Problem Statement: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min_stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack)==0:
            self.min_stack.append(x)
        else:
            next_min=min(x,self.getMin())
            self.min_stack.append(next_min)
            
        

    def pop(self) -> None:
        size=len(self.stack)
        if size!=0:
            self.stack.pop()
            self.min_stack.pop()
        
        

    def top(self) -> int:
        size=len(self.stack)
        if size!=0:
            return self.stack[size-1]
        else:
            return -1
        

    def getMin(self) -> int:
        size=len(self.min_stack)
        if size!=0:
            return self.min_stack[size-1]
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
