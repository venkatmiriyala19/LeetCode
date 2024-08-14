class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res=[]
        x=0
        for i in range(len(pref)):
            res.append(pref[i]^x)
            x=pref[i]
        return res

        