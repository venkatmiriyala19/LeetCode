class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list=new ArrayList<>();
        HashSet<List<Integer>> set=new HashSet<>();
        int n=nums.length;
        for (int i=0;i<(1<<n);i++){
            List<Integer> dummy=new ArrayList<>();
            for(int j=0;j<n;j++){
                if(((1<<j)&i)!=0){
                    dummy.add(nums[j]);
                }
            }
            if(set.contains(dummy)){
                continue;
            }
            set.add(dummy);
            list.add(dummy);
        }
        
        return list;
    }
}