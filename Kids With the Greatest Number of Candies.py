class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=max(candies)
        l=[]
        for i in candies:
            if i+extraCandies>=a:
                l.append(True)
                continue
            l.append(False)
        return l
