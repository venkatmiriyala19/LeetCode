class Solution(object):
    def isMonotonic(self, nums):
        # flag=False       
        # for i in range(len(nums)-1):
        #     if nums[i]<nums[i+1]:
        #         flag=True
        #     elif nums[i]==nums[i+1]:
        #         if flag==False:
        #             flag=True
        #         continue
        #     else:
        #         if (flag==True):
        #             return False
        # return True
        a=nums[:]
        nums.sort()
        if a==nums:
            return True
        nums.reverse()
        if a==nums:
            return True
        return False
        
                
                
        """
        :type nums: List[int]
        :rtype: bool
        """
        
