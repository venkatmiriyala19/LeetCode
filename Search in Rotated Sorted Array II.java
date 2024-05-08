class Solution {
    public boolean search(int[] nums, int target) {
        for (int a:nums){
            if (a==target){
                return true;
            }
        }
        return false;
        
    }
}
