class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        step=0
        while(a!=1):
            if a%2==0:
                a=a//2
                
            else:
                a+=1
            step+=1
        return step

        