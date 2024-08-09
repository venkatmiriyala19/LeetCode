class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        s=set(nums2)
        s1=set(nums1)
        c=0
        a=[]
        for i in nums1:
            if i in s:
                c+=1
        a.append(c)
        c=0
        for i in nums2:
            if i in s1:
                c+=1
        a.append(c)
        return a
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        