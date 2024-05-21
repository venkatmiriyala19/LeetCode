class Solution {
    public boolean findSubarrays(int[] nums) {
        HashSet<Integer> set=new HashSet<>();
        for(int i=1;i<nums.length;i++){
            if (set.contains(nums[i]+nums[i-1])){
                // System.out.println()
                return true;
            }
            else{
                set.add(nums[i]+nums[i-1]);
            }
        }
        return false;
    }
}