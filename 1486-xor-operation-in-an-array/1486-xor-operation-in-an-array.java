class Solution {
    public int xorOperation(int n, int start) {
        int total=0;
        for (int i=0;i<n;i++){
            total^=start;
            start+=2;
        }
        return total;
        
    }
}