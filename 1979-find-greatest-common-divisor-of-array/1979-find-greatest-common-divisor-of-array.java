class Solution {
    public int findGCD(int[] nums) {
        Arrays.sort(nums);
        int a=nums[0];
        int b=nums[nums.length-1];
        for (int i=a;i>=1;i--){
            // System.out.println(b);
            if (b%i==0 && a%i==0){
                return i;
            }
        }
        return 1;
    }
}