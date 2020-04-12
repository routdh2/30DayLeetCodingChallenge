'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            size=len(stones)
            max_1=stones[size-1]
            max_2=stones[size-2]
            stones.remove(max_1)
            stones.remove(max_2)
            if max_1!=max_2:
                stones.append(max_1-max_2)
        return stones[0] if len(stones)==1 else 0
        
