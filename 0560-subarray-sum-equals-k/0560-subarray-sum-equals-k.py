class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        prefix_sum=0
        prefix_map={0:1}
        for num in nums:
            prefix_sum+=num
            if(prefix_sum-k in prefix_map):
                count+=prefix_map[prefix_sum-k]
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum]=1
            else:
                prefix_map[prefix_sum]+=1
        return count
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        