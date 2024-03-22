class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
                continue
            pos.append(i)
        a=[]
        for i in range(len(nums)//2):
            a.append(pos[i])
            a.append(neg[i])
        return a
