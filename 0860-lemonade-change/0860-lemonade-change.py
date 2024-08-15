class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        five=0
        ten=0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            elif bills[i]==20:
                if five>=1 and ten >=1:
                    five-=1
                    ten-=1
                elif five>=3 and ten==0:
                    five-=3
                else:
                    return False

        return True

        