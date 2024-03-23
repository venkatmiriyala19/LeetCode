class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.reverse()
        arr=[]
        for i in range(len(nums)//2):
            alice=nums.pop()
            bob=nums.pop()
            arr.append(bob)
            arr.append(alice)
        return arr
