class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list=new ArrayList<>();
        int n=nums.length;
        for(int i=0;i<(1<<n);i++){
            List<Integer> dummy=new ArrayList<>();
            for(int j=0;j<n;j++){
                if(((1<<j)&i) !=0){
                    dummy.add(nums[j]);
                }
            }
            list.add(dummy);
        }
        return list;
        
    }
}