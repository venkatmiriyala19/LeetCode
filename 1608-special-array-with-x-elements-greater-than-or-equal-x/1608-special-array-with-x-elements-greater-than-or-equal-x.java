class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        if(nums.length<=nums[0]){
            return nums.length;
        }
        for(int i=1;i<nums.length;i++){
            if((nums[n-i]>=i) && (n-i-1<0 || nums[n-i-1]<i))
            return i;
        }
        
        return -1;
        
    }
}