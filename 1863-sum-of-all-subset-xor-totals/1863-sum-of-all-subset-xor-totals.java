class Solution {
    public int subsetXORSum(int[] nums) {
        // ArrayList<ArrayList <Integer>> list=new ArrayList<>();
        int sum=0;
        for(int i=0;i<(1<<nums.length);i++){
            ArrayList<Integer> dummy=new ArrayList<>();
            for(int j=0;j<nums.length;j++){
                if(((1<<j)&i) !=0){
                    dummy.add(nums[j]);
                }
            }
            if (dummy.size()==0)
            continue;
            int total=dummy.get(0);
            for(int k=1;k<dummy.size();k++){
                total=total^dummy.get(k);
            }
            sum+=total;
        }
        return sum;
    }
}