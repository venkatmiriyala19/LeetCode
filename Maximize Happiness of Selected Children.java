class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        // System.out.println(happiness.length);
        int n=happiness.length;
        long sum=0;
        int j=0;
        for (int i=1;i<=k;i++){
            // if (i==1){
            //     sum+=happiness[n-i];
            //     continue;
            // }
            if (happiness[n-i]-j>=0){
                sum=sum+happiness[n-i]-j;
                j++;
            }
            else{
                break;
            }
        }
        return sum;
    }
}
