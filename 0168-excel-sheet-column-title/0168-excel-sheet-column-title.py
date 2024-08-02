class Solution(object):
    def convertToTitle(self, columnNumber):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = ''
        while columnNumber != 0:
            columnNumber -= 1
            rem = columnNumber % 26
            s += alpha[rem]
            columnNumber //= 26
        return s[::-1]

        """
        :type columnNumber: int
        :rtype: str
        """
        