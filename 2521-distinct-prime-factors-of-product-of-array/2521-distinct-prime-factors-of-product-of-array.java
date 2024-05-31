class Solution {
    public int distinctPrimeFactors(int[] nums) {
        HashSet<Integer> pFact=new HashSet<>();

        for(int i=0;i<nums.length;i++){
        int j=2;
        int n=nums[i];
        while(j*j<=n){
            while(n%j==0){
                // System.out.println(prod);
                pFact.add(j);
                n=n/j;
            }
            j++;
        }
            if(n>1){
            pFact.add(n);
        }
        }
        return pFact.size();
        
    }
}