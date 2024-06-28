class Solution {
    public long maximumImportance(int n, int[][] roads) {
        long[] degree=new long[n];
        for(int[] edge:roads){
            degree[edge[0]]++;
            degree[edge[1]]++;
        }
        Arrays.sort(degree);
        long value=1;
        long total=0;
        for(long d:degree){
            total+=(d*value);
            value++;
        }
        return total;
        
        
    }
}