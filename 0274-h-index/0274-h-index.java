class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        for (int i = 0; i < n / 2; i++) {
            int temp = citations[i];
            citations[i] = citations[n - 1 - i];
            citations[n - 1 - i] = temp;
        }
        for(int i=0;i<citations.length;i++){
            if(citations[i]>=i+1){
                continue;
            }
            return i;
        }
        return citations.length;
        
    }
}