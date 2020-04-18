/**
* Problem Statement: https://leetcode.com/problems/minimum-path-sum
*/
class Solution {
    public int minPathSum(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int[][] table = new int[row][col];
        table[0][0]=grid[0][0];
        for(int i=1;i<row;i++)
            table[i][0]=table[i-1][0]+grid[i][0];
        for(int j=1;j<col;j++)
            table[0][j]=table[0][j-1]+grid[0][j];
        for(int i=1;i<row;i++) {
            for(int j=1;j<col;j++) {
                table[i][j]=grid[i][j]+Math.min(table[i][j-1],table[i-1][j]);
            }
        }
        return table[row-1][col-1];
    }
}
