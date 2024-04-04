lass Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        max=0
        for i in s:
            if i=='(':
                a+=1
            if max<a:
                max+=1
            if i==")":
                a-=1
        return max
        
        
