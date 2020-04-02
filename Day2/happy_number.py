#problem statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
'''Submission Detail:401 / 401 test cases passed.
Runtime: 28 ms
Memory Usage: 13.8 MB'''


class Solution:
    def isHappy(self, n: int) -> bool:
        nums=set()
        while True:
            if n not in nums:
                nums.add(n)
            else:
                return False
            
            sum=0
            for char in str(n):
                sum+=int(char)**2
            if sum==1:
                return True
            n=sum
