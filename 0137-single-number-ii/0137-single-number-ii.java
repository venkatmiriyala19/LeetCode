class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(Integer ele:nums){
            if(map.containsKey(ele)){
                map.put(ele,map.get(ele)+1);
            }
            else{
                map.put(ele,1);
            }
        }
        for (Integer key:map.keySet()){
            if(map.get(key)==1){
                return key;
            }
        }
        return 1;
    }
}