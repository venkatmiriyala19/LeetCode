class Solution {
    public boolean isGoodArray(int[] nums) {
        int tempGCD=nums[0];
        int i=0;
        while(i<nums.length){
            tempGCD=gcd(tempGCD, nums[i]);
            i++;
            if(tempGCD==1)return true;
        }
        return false;      
    }
    int gcd(int a,int b){
        if(b==0) return a;
        else return gcd(b,(a%b));
    }
}