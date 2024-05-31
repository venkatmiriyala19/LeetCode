class Solution {
    public int trailingZeroes(int n) {
        int trail=0;
        while(n>0){
            n=n/5;
            trail+=n;
        }
        return trail;
    }
}