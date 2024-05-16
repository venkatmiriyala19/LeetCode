class Solution {
    public boolean canJump(int[] nums) {
        int jump=0;
        for(Integer ele:nums){
            if(jump<0){
                return false;
            }
            else if(jump<ele){
                jump=ele;
            }
            jump--;
        }
        return true;
        
    }
}