class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=1
        c=0
        for i in words:
            for j in i:
                if j not in allowed:
                    a=0
                    continue
            if (a!=0):
                c+=1
            else:
                a=1
        return c
        
