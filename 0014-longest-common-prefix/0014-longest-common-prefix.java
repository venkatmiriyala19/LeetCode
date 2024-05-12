class Solution {
    public String longestCommonPrefix(String[] strs) {
        String minWord=strs[0];
        for(String ele:strs){
            if (ele.length()<minWord.length()){
                minWord=ele;
            }
        }
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<minWord.length();i++){
            int flag=1;
            for(String str:strs){
                if (minWord.charAt(i)==str.charAt(i)){
                    continue;
                }
                else{
                    flag=0;
                    break;
                }
            }
            if(flag==0){
                break;
            }
            else{
                sb.append(minWord.charAt(i));
            }

        }
        String result=sb.toString();
        return result;
        
    }
}