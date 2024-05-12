class Solution {
    public int reverse(int x) {
        
        int n=x;
        if (x<0){
            n=n*-1;
        }
        int rem;
        long rev=0;
        while(n>0){
            rem=n%10;
            rev=rev*10+rem;
            n=n/10;
        }
        if (rev>Integer.MAX_VALUE || rev<Integer.MIN_VALUE){
            return 0;
        }
        if (x<0){
            return (int)rev*-1;
        }
        return (int)rev;
        
    }
}