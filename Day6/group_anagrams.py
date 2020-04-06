'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            key=str(sorted(word))
            dic[key]=dic.get(key,[])+[word]
        result=[]
        for i in dic.values():
            result.append(i)
        return result
