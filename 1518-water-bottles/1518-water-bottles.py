class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        empty=numBottles
        total=numBottles
        while(numBottles>=numExchange):
            total+=(numBottles//numExchange)
            empty=numBottles%numExchange
            numBottles=(numBottles//numExchange)+empty
        return total
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        