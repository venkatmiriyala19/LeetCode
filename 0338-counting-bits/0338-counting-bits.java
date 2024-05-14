class Solution {
    public int[] countBits(int n) {
        int[] ans=new int[n+1];
        for(int i=0;i<=n;i++){
            String binString=Integer.toBinaryString(i);
            int count=0;
            for(int j=0;j<binString.length();j++){
                if (binString.charAt(j)=='1'){
                    count++;
                }
            }
            ans[i]=count;
        }
        return ans;
    }
}