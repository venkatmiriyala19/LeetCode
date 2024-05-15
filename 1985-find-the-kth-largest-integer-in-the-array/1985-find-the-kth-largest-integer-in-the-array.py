class Solution(object):
    def kthLargestNumber(self, nums, k):
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        # print(nums)
        return str(nums[-k])
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        