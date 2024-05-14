class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] ans=new int[k];
        HashMap<Integer,Integer> map=new HashMap<>();
        for(Integer ele:nums){
            map.put(ele,map.getOrDefault(ele,0)+1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
            (a, b) -> b.getValue() - a.getValue()); // Max heap based on frequency

        // Add entries to the priority queue
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            pq.offer(entry);
        }
        for(int i=0;i<k;i++){
            ans[i]=pq.poll().getKey();
        }
        return ans;
    }
}