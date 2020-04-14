'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/'''
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for op in shift:
            #if left shift
            if op[0]==0:
                chars=s[0:op[1]]
                s=s[op[1]:]
                s+=chars
            else:
                chars=s[len(s)-op[1]:]
                s=s[0:(len(s)-op[1])]
                s=chars+s
        return s
                
