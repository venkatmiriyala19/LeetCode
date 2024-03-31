class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n)
        a=str(a)
        c=0
        for i in a:
            if i=='1':
                c+=1
        # print(c)
        return c
