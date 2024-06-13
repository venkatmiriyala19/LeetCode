class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        sum=0
        for i in range(len(seats)):
            sum+=abs(seats[i]-students[i])
        return sum
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        