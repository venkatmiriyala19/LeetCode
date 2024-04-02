class Solution:
    def countAsterisks(self, s: str) -> int:
        a=s.split('|')
        c=0
        for i in range(0,len(a),2):
            b=a[i].count('*')
            c+=b
        return c
