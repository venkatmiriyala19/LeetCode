class Solution {
    public int minPartitions(String n) {
        int max=0;
        for(int i=0;i<n.length();i++){
            int s=n.charAt(i)-'0';
            if (s>max){
                max=s;
            }
        }
        return max;
    }
}