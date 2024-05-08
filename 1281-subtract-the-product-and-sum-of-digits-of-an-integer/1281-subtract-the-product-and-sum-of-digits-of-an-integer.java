class Solution {
    public int subtractProductAndSum(int n) {
        int a=n;
        int prod=1;
        int rem=0;
        int sum=0;
        while(a>0){
            rem=a%10;
            prod*=rem;
            sum+=rem;
            a=a/10;
        }
        return prod-sum;
        
    }
}