//Problem Statement: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/
class Solution {
    public int search(int[] nums, int target) {
        if(nums==null || nums.length==0)
            return -1;
        int start=0,end=nums.length-1;
        while(start<=end) {
            int mid=start+(end-start)/2;
            if(target==nums[mid])
                return mid;
            //check which part is sorted
            if(nums[mid]>=nums[start]) {
                //left part is sorted
                //check if key  is present
                if(target>=nums[start] && target<nums[mid])
                    end=mid-1;
                else
                    start=mid+1;
            }
            else {
                //right part is sorted
                //check if key is present
                if(target>nums[mid] && target<=nums[end])
                    start=mid+1;
                else
                    end=mid-1;
            }
        }
        return -1;
        
    }
    

}
