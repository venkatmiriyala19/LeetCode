class Solution {
    public int minOperations(String[] logs) {
        int child=0;
        for (int i=0;i<logs.length;i++){
            if( logs[i].equals("./")){
                continue;
            }
            else if (logs[i].equals("../")){
                if (child>0) child--;
            }
            else child++;
        }
        return child;
    }
}