/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface BinaryMatrix {
 *     public int get(int x, int y) {}
 *     public List<Integer> dimensions {}
 * };
 */
//Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/
class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> dims = binaryMatrix.dimensions();
        int row=dims.get(0);
        int col=dims.get(1);
        int start=0,end=col-1;
        int index=-1;
        while(start<=end) {
            int mid=start+(end-start)/2;
            boolean found=false;
            for(int i=0;i<row;i++) {
                if(binaryMatrix.get(i,mid)==1) {
                    found=true;
                    index=mid;
                    break;
                }
            }
            if(found) {
                end=mid-1;
            }
            else
                start=mid+1;
        }
        return index;
        
    }
}
