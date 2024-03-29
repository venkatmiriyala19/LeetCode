class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=len(s)
        s1=s[:(a//2)]
        s2=s[(a//2):]
        s1=s1.lower()
        s2=s2.lower()
        c=0
        d=0
        for i in s1:
            if i in 'aeiou':
                c+=1
        for i in s2:
            if i in 'aeiou':
                d+=1
        if c==d:
            return True
        return False
        
