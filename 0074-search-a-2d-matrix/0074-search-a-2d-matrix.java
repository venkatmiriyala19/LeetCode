class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r=0,c=matrix[0].length-1;
        while(r<matrix.length && c>-1){
            int curr=matrix[r][c];
            if (curr==target) return true;
            if(target>curr) r++;
            else c--;
        }
        return false;
        
    }
}