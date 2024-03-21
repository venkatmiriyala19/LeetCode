class Solution(object):
    def squareIsWhite(self, coordinates):
        d=int(coordinates[-1])
        if (d%2==0):
            if coordinates[0] in 'aceg':
                return True
            return False
        else:
            if coordinates[0] in 'aceg':
                return False
            return True
        """
        :type coordinates: str
        :rtype: bool
        """
        
