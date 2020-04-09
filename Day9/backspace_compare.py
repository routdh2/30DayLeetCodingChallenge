'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        r1=[]
        r2=[]
        for char in S:
            if char=="#":
                if len(r1)!=0:
                    r1.pop()
            else:
                r1.append(char)
        for char in T:
            if char=="#":
                if len(r2)!=0:
                    r2.pop()
            else:
                r2.append(char)
        return r1==r2
        
