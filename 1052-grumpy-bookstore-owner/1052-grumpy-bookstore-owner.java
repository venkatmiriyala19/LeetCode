class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int i=0,j=0,sum=0,max=0;
        for(j=0;j<customers.length;j++){
            sum+=customers[j]*grumpy[j];
            max=Math.max(max,sum);
            if(j>=minutes-1){
                sum-=customers[i]*grumpy[i++];
            }
        }
        int res=max;
        for(i=0;i<grumpy.length;i++){
            res+=customers[i]*(1-grumpy[i]);
        }
        return res;
        }
}