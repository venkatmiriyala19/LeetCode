class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for i in stones:
            if i in jewels:
                c+=1
        return c
