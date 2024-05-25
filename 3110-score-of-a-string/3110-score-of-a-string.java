class Solution {
    public int scoreOfString(String s) {
        int count=0;
        for(int i=1;i<s.length();i++){
            char ch1=s.charAt(i-1);
            char ch2=s.charAt(i);
            int ascii1=(int) ch1;
            int ascii2=(int) ch2;
            count=count+Math.abs(ascii1-ascii2);
        }
        return count;
        
    }
}