class Solution {
    public int countDistinctIntegers(int[] nums) {
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            list.add(nums[i]);
            list.add(rev(nums[i]));
        }
        HashSet<Integer> set=new HashSet<>(list);
        return set.size();
        
    }
    public int rev(int n){
        int sum=0;
        while(n!=0){
            int rem=n%10;
            sum=sum*10+rem;
            n=n/10;
        }
        return sum;
    }
}
